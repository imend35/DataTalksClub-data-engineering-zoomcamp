
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, StreamTableEnvironment


def main():

    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)

    # Kafka Source
    source_ddl = """
        CREATE TABLE green_trips (
            lpep_pickup_datetime STRING,
            lpep_dropoff_datetime STRING,
            PULocationID DOUBLE,
            DOLocationID DOUBLE,
            passenger_count DOUBLE,
            trip_distance DOUBLE,
            tip_amount DOUBLE,
            total_amount DOUBLE,

            event_timestamp AS TO_TIMESTAMP(lpep_pickup_datetime, 'yyyy-MM-dd HH:mm:ss'),
            WATERMARK FOR event_timestamp AS event_timestamp - INTERVAL '5' SECOND
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'green-trips',
            'properties.bootstrap.servers' = 'redpanda:29092',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'json'
        )
    """

    t_env.execute_sql(source_ddl)

    # JDBC Sink
    sink_ddl = """
        CREATE TABLE q5_session (
            PULocationID INT,
            num_trips BIGINT,
            PRIMARY KEY (PULocationID) NOT ENFORCED
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5432/postgres',
            'table-name' = 'q5_session',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        )
    """

    t_env.execute_sql(sink_ddl)

    # Session Window
    t_env.execute_sql(
        """
        INSERT INTO q5_session
        SELECT
            CAST(PULocationID AS INT),
            COUNT(*) AS num_trips
        FROM TABLE(
            SESSION(
                TABLE green_trips,
                DESCRIPTOR(event_timestamp),
                INTERVAL '5' MINUTES
            )
        )
        GROUP BY
            CAST(PULocationID AS INT),
            window_start,
            window_end
        """
    )


if __name__ == "__main__":
    main()
