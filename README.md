# 📊 End-to-End Customer Analytics & Predictive Churn Pipeline

This project demonstrates a professional-grade **Data Engineering & Machine Learning** workflow. It automates the transition from raw, messy consumer data to a cloud-hosted, AI-enriched dataset ready for real-time Business Intelligence (BI).

---

## 🏗️ System Architecture

The project is structured as a **Closed-Loop Intelligence Pipeline**:

1. **Ingestion & ETL:**  
   Raw CSV data is ingested via Python, where it undergoes rigorous cleaning, including median-based imputation for missing review ratings and schema standardization.

2. **Statistical Feature Engineering:**
   - **Age Quartiles:** Instead of arbitrary brackets, we use `pd.qcut` to divide customers into four balanced quartiles: *Young Adult, Adult, Middle-Aged, and Senior*.
   - **Behavioral Labeling:** A multi-factor logic identifies **Churn (1)** vs **Loyal (0)** customers based on purchase frequency (e.g., Annual/3-month) and dissatisfaction thresholds.

3. **Machine Learning Inference:**  
   A **Random Forest Classifier** performs in-flight predictions. The model analyzes 7+ behavioral features to assign a `churn_risk` score to every record.

4. **Cloud Deployment:**  
   The processed and enriched data is pushed to a **Supabase (PostgreSQL)** instance, ensuring global accessibility.

5. **BI Presentation:**  
   **Power BI Desktop** connects to the cloud source via secure SSL to visualize churn trends across demographics.

---

## 🛠️ Technical Stack

- **Language:** Python 3.10+
- **Data Processing:** Pandas, NumPy, SQLAlchemy
- **Machine Learning:** Scikit-Learn (Random Forest, Label Encoding)
- **Database:** Supabase / PostgreSQL
- **Environment Management:** Python-Dotenv
- **BI Tool:** Power BI (DAX, Power Query)

---

## 🧠 Machine Learning Engine

### Features Used for Prediction

- **Age & Age Group**
- **Purchase Amount**
- **Review Rating**
- **Frequency of Purchases**
- **Subscription Status**
- Encoded categorical variables
- Engineered behavioral flags

---

## 📂 Repository Structure

| File | Purpose |
|------|----------|
| `train_model.py` | Trains the Random Forest model and generates `churn_model.pkl`. |
| `customer_pipeline.py` | Main ETL + ML pipeline script. Cleans data, predicts churn, uploads to Supabase. |
| `churn_model.pkl` | Serialized trained ML model. |
| `.env` | Local credential storage (NOT pushed to GitHub). |
| `requirements.txt` | Dependency management file. |

---

## 🚀 Deployment Guide

### 1️⃣ Prerequisites

- Supabase PostgreSQL project
- Power BI Desktop
- Python 3.10+

---

### 2️⃣ Environment Setup

Create a `.env` file in the root directory:

SUPABASE_USER=postgres  
SUPABASE_PASS=Your_Secure_Password  
SUPABASE_HOST=db.your_project_id.supabase.co  
SUPABASE_PORT=5432  
SUPABASE_NAME=postgres  

---

### 3️⃣ Installation & Execution

# Install dependencies
pip install -r requirements.txt

# Train the ML model
python train_model.py

# Run ETL + ML pipeline and upload to cloud
python customer_pipeline.py

---

## 📈 Power BI Integration

- Connect Power BI to Supabase PostgreSQL.
- Import table: `customer_final_ml`
- Enable SSL connection.
- If Windows SSL issue occurs → Trust server certificate in advanced settings.

### Key Dashboard Visual

- **Churn Risk Heatmap**
- Age Group vs Product Category Risk Distribution
- Subscription Impact Analysis
- Purchase Frequency vs Churn Trend

---

## 🔐 Security Best Practices

- Never push `.env` to GitHub.
- Use environment variables for credentials.
- Use SSL-enabled PostgreSQL connections.
- Restrict Supabase database access via IP rules if needed.

---

## 📌 Future Enhancements

- Add model performance tracking (Accuracy, ROC-AUC, Confusion Matrix)
- Deploy API endpoint using FastAPI
- Automate pipeline using Airflow
- Implement real-time streaming ingestion
- Containerize with Docker

---

## 👨‍💻 Developed By

Dheemanth  
Software Engineer | Data Analytics Specialist

GitHub: https://github.com/Dheemanthgowda00
