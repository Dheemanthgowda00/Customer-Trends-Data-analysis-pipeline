# 🚀 Automated Cloud-Integrated Customer Analytics Pipeline

An end-to-end Data Engineering system that automates the lifecycle of consumer data — from local CSV ingestion to a **Supabase Cloud PostgreSQL** database and live **Power BI** reporting.

---

## 📋 Project Overview

This project represents a full migration from a local, manual workflow to a **Cloud-Integrated ETL Pipeline**. By combining Python automation with cloud-hosted storage, the system ensures that business insights are always up-to-date, secure, and accessible from anywhere.

It demonstrates production-ready practices including automation scheduling, cloud database integration, environment-based configuration, and BI connectivity.

---

## 🛠️ Technical Stack

| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.13 (Pandas, SQLAlchemy, Dotenv) |
| **Cloud Database** | Supabase (PostgreSQL) |
| **Automation** | Windows Task Scheduler |
| **Local Database** | PostgreSQL (pgAdmin 4) |
| **BI / Visualization** | Power BI Desktop & Power BI Service |
| **Environment** | PyCharm (Virtual Environments) |

---

## ⚙️ System Architecture & Workflow

### 1️⃣ Data Ingestion & ETL (Python)

A modular Python script (`customer_pipeline.py`) handles:

- **Data Cleaning**
  - Category-based median imputation for missing Review Ratings
- **Normalization**
  - Schema standardization using `snake_case`
- **Feature Engineering**
  - Automated age-group binning
  - Purchase frequency mapping
- **Database Push**
  - Automatic upload to PostgreSQL (Local or Cloud)

---

### 2️⃣ Cloud Data Warehousing (Supabase)

The pipeline integrates directly with **Supabase Cloud PostgreSQL** using `SQLAlchemy`.

- Data is pushed to a Singapore-hosted PostgreSQL instance
- Enables remote BI access
- Ensures high availability
- Eliminates dependency on localhost databases

---

### 3️⃣ Enterprise Automation

The system is fully automated via **Windows Task Scheduler**.

- Executes inside isolated `.venv`
- Runs daily without manual intervention
- Logs execution status
- Ensures consistent reporting updates

---

### 4️⃣ Real-Time BI Visualization

Power BI connects via Cloud PostgreSQL connector.

Since the database is cloud-hosted:
- Dashboards can refresh from anywhere
- No local machine dependency
- Fully remote reporting capability

---

## 🛡️ Production-Grade Features

### 📡 Cloud-Native Toggle

The pipeline includes a:

```
USE_CLOUD = True / False
```

This enables seamless switching between:
- Local Development (localhost PostgreSQL)
- Production Deployment (Supabase Cloud)

---

### 📝 Robust Logging

Each execution is recorded in:

```
pipeline.log
```

Example log output:

```
2026-02-23 15:31:12 - INFO - Pipeline started (Target: Cloud).
2026-02-23 15:31:15 - INFO - Pipeline successful: Data pushed to Supabase Cloud.
```

This ensures auditability and easier debugging.

---

### 🔐 Secure Configuration

Sensitive credentials are stored securely using:

- `.env` file
- Environment variables
- `python-dotenv`

No database passwords are hardcoded in the source code.

---

## 📂 Repository Structure

```
customer_pipeline.py      # Core ETL engine
requirements.txt          # Python dependencies
.env.example              # Environment variable template
pipeline.log              # Execution logs
Dashboard.pbix            # Power BI dashboard
```

---

## 🚀 How to Set Up the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/Dheemanthgowda00/Customer-Trends-Data-analysis-pipeline.git
```

---

### 2️⃣ Initialize Virtual Environment

```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
# Supabase Cloud Credentials
SUPABASE_HOST=db.your_id.supabase.co
SUPABASE_USER=postgres
SUPABASE_PASS=your_password
SUPABASE_NAME=postgres
SUPABASE_PORT=5432
```

---

### 4️⃣ Run the Automated Pipeline

```
python customer_pipeline.py
```

If `USE_CLOUD = True`, the cleaned dataset will automatically be pushed to Supabase Cloud.

---

## 📊 Enterprise Capabilities Demonstrated

✔ Automated ETL  
✔ Cloud Database Integration  
✔ Production Logging  
✔ Secure Credential Management  
✔ Scheduled Task Execution  
✔ Remote BI Reporting  
✔ Scalable Architecture  

---

## 🎯 Why This Project Matters

This project demonstrates real-world:

- Data Engineering principles
- Cloud database deployment
- Automation strategy
- BI integration workflow
- Production-ready coding practices

It bridges the gap between Data Analytics and Data Engineering.

---

## 👨‍💻 Author

Dheemanth  

Specializing in Software Development, Robotics, and Data Systems.

---

## ✅ Final Checklist Before Publishing

1. Run:
   ```
   pip freeze > requirements.txt
   ```

2. Ensure:
   ```
   USE_CLOUD = True
   ```
   is enabled before pushing to GitHub.

3. Upload:
   - Dashboard screenshots (store in `/images/`)
   - Supabase table preview (optional)

4. Add screenshots to README for stronger portfolio impact.

---

If you found this project valuable, consider giving it a ⭐ on GitHub.
