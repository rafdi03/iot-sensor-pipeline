import requests
import time
import random

API_URL = "http://127.0.0.1:8000/sensor-data"

def send_sensor_data():
    while True:
        payload = {
            "machine_id": f"M{random.randint(1, 10):03}",
            "temperature": round(random.uniform(60, 110), 2),
            "vibration": round(random.uniform(50, 300), 2)
        }

        try:
            response = requests.post(API_URL, json=payload, timeout=3)
            response.raise_for_status()
            print(f"[OK] {payload}")
        except Exception as e:
            print(f"[ERROR] {e}")

        time.sleep(1)

if __name__ == "__main__":
    send_sensor_data()
