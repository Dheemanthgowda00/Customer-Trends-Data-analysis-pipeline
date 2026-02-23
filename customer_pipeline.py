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

# ======================================================================================================================================================

# import pandas as pd
# from sqlalchemy import create_engine
# import logging
# import os
# import joblib  # <--- New for ML
# from sklearn.preprocessing import LabelEncoder  # <--- New for ML
# from dotenv import load_dotenv
#
# # 1. Load and Verify .env
# load_dotenv()
#
# # --- CONNECTION SETTINGS ---
# USE_CLOUD = True
#
# if USE_CLOUD:
#     USER = os.getenv('SUPABASE_USER')
#     PASS = os.getenv('SUPABASE_PASS')
#     HOST = os.getenv('SUPABASE_HOST')
#     PORT = os.getenv('SUPABASE_PORT') or "5432"
#     DB = os.getenv('SUPABASE_NAME')
# else:
#     USER = "postgres"
#     PASS = os.getenv('DB_PASSWORD')
#     HOST = "localhost"
#     PORT = "5432"
#     DB = "customer_behavior"
#
# # Create the Engine
# DB_URL = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DB}"
# engine = create_engine(DB_URL)
#
# # 2. Logging Setup
# logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# def run_pipeline():
#     try:
#         logging.info(f"Pipeline started (Target: {'Cloud' if USE_CLOUD else 'Local'}).")
#
#         # --- A. EXTRACT ---
#         df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')
#
#         # --- B. TRANSFORM (Cleaning) ---
#         df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
#
#         # Keep a copy for the final export before we encode things for the AI
#         df_display = df.copy()
#
#         # --- C. MACHINE LEARNING PREDICTION ---
#         logging.info("Running ML Prediction Engine...")
#
#         # 1. Load the trained model
#         model = joblib.load('churn_model.pkl')
#
#         # 2. Encode categorical data (Exactly like we did in training)
#         le = LabelEncoder()
#         df['gender_n'] = le.fit_transform(df['Gender'])
#         df['category_n'] = le.fit_transform(df['Category'])
#         df['season_n'] = le.fit_transform(df['Season'])
#
#         # 3. Select the same features used during training
#         features = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'gender_n', 'category_n', 'season_n']
#         X = df[features]
#
#         # 4. Generate Predictions (0 = Loyal, 1 = Likely to Churn)
#         df_display['churn_prediction'] = model.predict(X)
#
#         # Standardize columns for SQL
#         df_display.columns = df_display.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')',
#                                                                                                                    '')
#
#         # --- D. LOAD TO SUPABASE ---
#         df_display.to_sql('customer_ml_data', engine, if_exists="replace", index=False, method='multi')
#
#         destination = "Supabase Cloud" if USE_CLOUD else "Local PostgreSQL"
#         logging.info(f"Pipeline successful: ML Predictions pushed to {destination}.")
#         print(f"✅ Success! ML-ready data is now in {destination}.")
#
#     except Exception as e:
#         logging.error(f"Pipeline failed: {str(e)}")
#         print(f"❌ Failed! Check pipeline.log for the error.")
#
#
# if __name__ == "__main__":
#     run_pipeline()

# ======================================================================================================================================================

import pandas as pd
from sqlalchemy import create_engine
import logging
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from dotenv import load_dotenv

load_dotenv()

# --- CLOUD SETTINGS ---
USER = os.getenv('SUPABASE_USER')
PASS = os.getenv('SUPABASE_PASS')
HOST = os.getenv('SUPABASE_HOST')
PORT = os.getenv('SUPABASE_PORT') or "5432"
DB = os.getenv('SUPABASE_NAME')

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DB}")


def run_pipeline():
    try:
        # 1. EXTRACT
        df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

        # 2. TRANSFORM (Cleaning)
        df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))

        # 3. PREDICT (Using the Brain)
        model = joblib.load('churn_model.pkl')

        # Encoding for prediction
        le = LabelEncoder()
        df['gender_n'] = le.fit_transform(df['gender'])
        df['category_n'] = le.fit_transform(df['category'])
        df['freq_n'] = le.fit_transform(df['frequency_of_purchases'])

        features = ['age', 'purchase_amount_usd', 'review_rating', 'previous_purchases', 'gender_n', 'category_n',
                    'freq_n']

        # Add the prediction to our dataframe
        df['churn_risk'] = model.predict(df[features])

        # 4. LOAD TO SUPABASE
        df.to_sql('customer_final_ml', engine, if_exists="replace", index=False, method='multi')
        print("✅ Step 2 Complete: Data + Predictions pushed to Supabase!")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_pipeline()