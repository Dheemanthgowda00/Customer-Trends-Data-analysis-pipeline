import pandas as pd
from sqlalchemy import create_engine
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from .env
password = os.getenv('DB_PASSWORD')

# Set up logging to a file
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_pipeline():
    try:
        logging.info("Pipeline started.")

        # 1. Extract
        df = pd.read_csv(r'C:\Users\Dheemanth\Downloads\customer_shopping_behavior.csv')

        # 2. Transform (Your cleaning logic)
        df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

        # ... (rest of your transformation code) ...

        # 3. Load
        username = "postgres"
        engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/customer_behavior")
        df.to_sql('customer', engine, if_exists="replace", index=False)

        logging.info("Pipeline executed successfully: Data pushed to PostgreSQL.")
        print("✅ Success! Check pipeline.log for details.")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print(f"❌ Failed! Check pipeline.log for the error.")


if __name__ == "__main__":
    run_pipeline()