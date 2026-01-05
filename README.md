# 🏭 Real-Time Industrial IoT Data Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![dbt](https://img.shields.io/badge/dbt-Incremental_Models-FF694B)
![FastAPI](https://img.shields.io/badge/FastAPI-High_Performance-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data_Warehouse-336791)

## 📋 Executive Summary
This project demonstrates an **end-to-end data engineering solution** for monitoring industrial machinery in real-time. It simulates a manufacturing environment where IoT sensors stream temperature and vibration data to a central warehouse.

Unlike traditional batch processing, this pipeline utilizes **FastAPI** for real-time ingestion and **dbt (data build tool)** with **incremental strategies** to efficiently process time-series data, visualizing critical anomalies via a live **Streamlit** dashboard.

---

## 🏗️ System Architecture

**Data Flow:** `Sensor Simulation` → `FastAPI (Ingestion)` → `PostgreSQL (Raw Storage)` → `dbt (Transformation)` → `Streamlit (Serving)`

1.  **Data Generation:** A Python script simulates 10+ robotic arms generating continuous telemetry data (JSON).
2.  **Ingestion Layer:** A high-throughput REST API built with **FastAPI** captures data streams and loads them into the raw storage layer.
3.  **Storage Layer:** **PostgreSQL** hosted in a **Docker Container** serves as the Data Warehouse.
4.  **Transformation Layer:** **dbt** performs ELT processes, utilizing **Incremental Models** to process only new data records (optimizing compute costs for large datasets).
5.  **Serving Layer:** A real-time **Streamlit** dashboard monitors machine health and flags anomalies (e.g., Overheating or High Vibration).

---

## 🚀 Key Engineering Features

* **🐳 Fully Containerized (Docker):**
    The entire infrastructure (Database, API, Dashboard) is defined in `docker-compose.yml`, ensuring environment consistency across development and production.

* **⚡ Real-Time Ingestion (FastAPI):**
    Moved beyond static CSV files by implementing a REST API endpoint (`POST /sensor-data`) to handle continuous data streams mimicking real-world IoT gateways.

* **📈 Optimized Transformations (dbt Incremental):**
    Implemented `materialized='incremental'` strategies in dbt. This ensures the system processes only the latest sensor readings rather than scanning the entire history table, significantly reducing query time.

* **🚨 Anomaly Detection Logic:**
    Custom SQL logic identifies machines exceeding safety thresholds (Temperature > 90°C or Vibration > 150Hz), enabling predictive maintenance insights.

---

## 📸 Dashboard Preview

*(Place your dashboard screenshot here)*
![Dashboard Screenshot](path/to/your/screenshot.png)

---

## 📂 Project Structure

```bash
IoT_Pipeline/
├── API/
│   ├── app.py                # FastAPI Application (Ingestion)
│   ├── Simulation_data.py    # Python Script for Sensor Simulation
│   └── Dockerfile            # API Container Config
├── models/                   # dbt Models
│   ├── staging/              # Cleaning raw data
│   └── mart/                 # Business logic & Aggregations
├── streamlit/
│   └── app.py                # Monitoring Dashboard
├── docker-compose.yml        # Infrastructure Orchestration
└── requirements.txt          # Python Dependencies
```

🛠️ How to Run This Project
Prerequisites: Docker Desktop installed.

Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/iot-sensor-pipeline.git](https://github.com/YOUR_USERNAME/iot-sensor-pipeline.git)
cd iot-sensor-pipeline
```
Spin Up Infrastructure Start the Database and API services:
```bash
docker-compose up -d
python API/Simulation_data.py
dbt run
streamlit run streamlit/app.py
```
