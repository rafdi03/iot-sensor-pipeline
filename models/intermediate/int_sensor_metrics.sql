with sensors as (
    select *
    from {{ ref('stg_raw_sensors') }}
)

select
    machine_id,
    date_trunc('minute', event_time) as minute_ts,
    avg(temperature) as avg_temperature,
    avg(vibration) as avg_vibration
from sensors
group by 1,2
