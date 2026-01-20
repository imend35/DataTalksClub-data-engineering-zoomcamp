FROM python:3.13

# Let's set the working directory.
WORKDIR /app

# Let's copy and install the library list.
COPY requirements.txt requirements.txt
RUN pip install pandas sqlalchemy psycopg2-binary pyarrow

# Let's copy the data files and the script.
COPY ingest_data.py ingest_data.py
COPY green_tripdata_2025-11.parquet green_tripdata_2025-11.parquet
COPY taxi_zone_lookup.csv taxi_zone_lookup.csv

# Let's run the script
ENTRYPOINT [ "python", "ingest_data.py" ]