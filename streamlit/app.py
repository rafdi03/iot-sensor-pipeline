import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="IoT Sensor Dashboard", layout="wide")

st.title("📡 IoT Sensor Monitoring")

DB_URI = "postgresql://iot_user:Aryaguna2022@db:5432/iot_pipeline"

engine = create_engine(DB_URI)

@st.cache_data(ttl=60)
def load_data():
    query = """
        SELECT *
        FROM fct_sensor_readings
        ORDER BY minute_ts DESC
        LIMIT 500
    """
    return pd.read_sql(query, engine)

df = load_data()

st.metric("Total Machines", df["machine_id"].nunique())
st.metric("Total Records", len(df))

st.line_chart(
    df,
    x="minute_ts",
    y=["avg_temperature"]
)

st.dataframe(df)
