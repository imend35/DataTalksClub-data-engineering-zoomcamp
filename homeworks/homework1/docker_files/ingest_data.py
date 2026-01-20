import pandas as pd
from sqlalchemy import create_engine

# Let's configure the connection settings.
#URL = 'postgresql://postgres:postgres@localhost:5433/ny_taxi'
URL = 'postgresql://postgres:mysecretpassword@db:5432/ny_taxi'
engine = create_engine(URL)

try:
    # Let's Read the Green Taxi Data
    print("Reading data, please wait...")
    df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
    
    # Let's make the historical data changes.
    df_green.lpep_pickup_datetime = pd.to_datetime(df_green.lpep_pickup_datetime)
    df_green.lpep_dropoff_datetime = pd.to_datetime(df_green.lpep_dropoff_datetime)

    # Let's write to the database
    print("Transferring data to the database...")
    df_green.to_sql(name='green_tripdata', con=engine, if_exists='replace', index=False)
    
    # Let's upload the regional data
    df_zones = pd.read_csv('taxi_zone_lookup.csv')
    df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace', index=False)
    
    print("Transaction completed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")