import pandas as pd
from sqlalchemy import create_engine
import logging
import os
from dotenv import load_dotenv

# 1. Load and Verify .env
load_dotenv()

# --- CONNECTION SETTINGS ---
USE_CLOUD = True

if USE_CLOUD:
    # Use the exact names from your updated .env
    USER = os.getenv('SUPABASE_USER')
    PASS = os.getenv('SUPABASE_PASS')
    HOST = os.getenv('SUPABASE_HOST')
    PORT = os.getenv('SUPABASE_PORT') or "5432"
    DB   = os.getenv('SUPABASE_NAME')
else:
    USER = "postgres"
    PASS = os.getenv('DB_PASSWORD')
    HOST = "localhost"
    PORT = "5432"
    DB   = "customer_behavior"

# Safety Check: This prevents the 'None' crash
if USE_CLOUD and not all([USER, PASS, HOST]):
    print("❌ ERROR: Missing Cloud credentials in .env file!")
    print(f"DEBUG -> HOST: {HOST}, USER: {USER}, PASS: {'Defined' if PASS else 'MISSING'}")
    exit()

# Create the Engine
try:
    DB_URL = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DB}"
    engine = create_engine(DB_URL)
except Exception as e:
    print(f"❌ Failed to create engine: {e}")
    exit()

# 2. Logging Setup
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    try:
        logging.info(f"Pipeline started (Target: {'Cloud' if USE_CLOUD else 'Local'}).")

        # 1. Extract
        df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')

        # 2. Transform
        df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

        # 3. Load to Database
        # method='multi' is significantly faster for cloud databases
        df.to_sql('customer_data', engine, if_exists="replace", index=False, method='multi')

        destination = "Supabase Cloud" if USE_CLOUD else "Local PostgreSQL"
        logging.info(f"Pipeline successful: Data pushed to {destination}.")
        print(f"✅ Success! Data is now in {destination}.")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print(f"❌ Failed! Check pipeline.log for the error.")

if __name__ == "__main__":
    run_pipeline()