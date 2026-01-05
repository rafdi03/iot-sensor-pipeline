SELECT
    id,
    machine_id,
    temperature,
    vibration,
    created_at::timestamp AS event_time
FROM public.raw_sensors