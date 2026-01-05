select
    machine_id,
    minute_ts,
    avg_temperature,
    avg_vibration
from {{ ref('int_sensor_metrics') }}
