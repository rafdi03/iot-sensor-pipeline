from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

def get_conn():
    return psycopg2.connect(
        host="db",
        port=5432,
        database="iot_pipeline",
        user="iot_user",
        password="Aryaguna2022"
    )

class SensorData(BaseModel):
    machine_id: str
    temperature: float
    vibration: float


@app.on_event("startup")
def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_sensors (
            id SERIAL PRIMARY KEY,
            machine_id VARCHAR(50),
            temperature FLOAT,
            vibration FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.post("/sensor-data")
def ingest_sensor_data(data: SensorData):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO raw_sensors (machine_id, temperature, vibration)
            VALUES (%s, %s, %s)
            """,
            (data.machine_id, data.temperature, data.vibration)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"status": "ok"}
