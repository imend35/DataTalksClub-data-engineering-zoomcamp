WITH source AS (

    SELECT *
    FROM {{ source('raw', 'fhv_tripdata_2019') }}

),

renamed AS (

    SELECT
        dispatching_base_num,

        SAFE_CAST(pickup_datetime AS TIMESTAMP)  AS pickup_datetime,
        SAFE_CAST(dropoff_datetime AS TIMESTAMP) AS dropoff_datetime,

        SAFE_CAST(PUlocationID AS INT64) AS pickup_location_id,
        SAFE_CAST(DOlocationID AS INT64) AS dropoff_location_id,

        affiliated_base_number

    FROM source
    WHERE dispatching_base_num IS NOT NULL

)

SELECT *
FROM renamed

