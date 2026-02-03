For the assignment for week 3, I followed the steps below in order : 

1 - To complete Week 3's assignment, I first downloaded the TLC Trip Record Data 2024 (January to June) Yellow Taxi Trip Records data files in PARQUET file format from the website https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page.
<img width="928" height="347" alt="image" src="https://github.com/user-attachments/assets/dbca5935-30a6-4325-9926-d8b71bbea497" />
<img width="1206" height="289" alt="image" src="https://github.com/user-attachments/assets/2651ce18-9954-4376-92d9-c9606e4fdcc0" />
2 -  I also downloaded the Python file named load_yellow_taxi_data.py.
<img width="1171" height="128" alt="image" src="https://github.com/user-attachments/assets/23350f1f-8223-466c-b558-82a25bab9edc" />

3 - I created a bucket named zoomcamp_taxi_data_bucket in Google Cloud Console, selecting the us_central1 region.

<img width="1673" height="470" alt="image" src="https://github.com/user-attachments/assets/0ce78e6a-65b2-44ce-a02c-7773b0791077" />

4- For the Python file to run on Google Cloud, the pandas and pyarrow libraries must be installed. I did this by running the command `pip install google-cloud-storage pandas pyarrow` in the terminal.

<img width="1913" height="736" alt="image" src="https://github.com/user-attachments/assets/c19b6c0e-6d32-4cbd-bfd6-aacc4513adfa" />

5 - Similarly, I need to authorize access to my Google Cloud account, and for that I ran the `gcloud auth application-default login` command in the terminal. 
However, it gave me an error saying that the Google Cloud SDK was not installed. I downloaded and installed GoogleCloudSDKInstaller.exe.

<img width="1288" height="125" alt="image" src="https://github.com/user-attachments/assets/bb753a68-9142-4320-a2a7-c66c402da30b" />

6 - After the installation was complete, I ran the `gcloud auth login` command again in the terminal.
I was able to log in successfully.

<img width="1907" height="182" alt="image" src="https://github.com/user-attachments/assets/a203498f-f443-43c3-90d1-b543bdd12f44" />

7 -  I also added my Google Cloud project to the SDK using the `gcloud config set project awesome-icon-484918-n5` command.

<img width="1904" height="80" alt="image" src="https://github.com/user-attachments/assets/86f6528c-9157-4992-92bc-472d7de5be21" />

8 - I also obtained application permissions using the `gcloud auth application-default login` command.

<img width="1915" height="218" alt="image" src="https://github.com/user-attachments/assets/5b9e5b5b-d559-456b-b72a-bc62f7a1c335" />


9 -  In the load_yellow_taxi_data.py file, since I'm logging in with the SDK, I updated it with client = storage.Client(project='awesome-icon-484918-n5') and also updated the name of the BUCKET_NAME = "zoomcamp_taxi_data_bucket".

<img width="756" height="206" alt="image" src="https://github.com/user-attachments/assets/eec6828c-50af-4f9d-a3b3-06bbf34f3bbe" />

10 - I ran the code in the load_yellow_taxi_data.py file in its folder using the terminal with the command `py load_yellow_taxi_data.py`.

<img width="813" height="628" alt="image" src="https://github.com/user-attachments/assets/79908a34-c629-4b24-8f3c-8ccbcc8da237" />

I observed that the Parquet files were successfully uploaded to the bucket.

<img width="1671" height="554" alt="image" src="https://github.com/user-attachments/assets/c9116558-6c2b-4661-bc69-4dd0b83fd73f" />

11 - In BigQuery, I clicked the three dots next to the Project ID and then clicked Create Dataset.

<img width="638" height="358" alt="image" src="https://github.com/user-attachments/assets/b2a89e75-dd45-4a75-bd68-0676d6e22cc9" />

12 - I created a dataset named ny_taxi with Data Location us_central1(lowa).

<img width="458" height="472" alt="image" src="https://github.com/user-attachments/assets/da286ffc-a86e-40a0-a9ab-2bc2bdc65b5e" />

13 - I ran the following SQL query to create an external table linking to Parquet files in GCS. I modified the necessary Project ID, Data Set, and Bucket names within the query.

CREATE OR REPLACE EXTERNAL TABLE `awesome-icon-484918-n5.ny_taxi.external_yellow_tripdata`
OPTIONS (
format = 'PARQUET',
uris = ['gs://zoomcamp_taxi_data_bucket/yellow_tripdata_2024-*.parquet']
);

I observed that the external table named external_yellow_tripdata was successfully created.

<img width="1340" height="595" alt="image" src="https://github.com/user-attachments/assets/dd20ca8f-d08d-4917-8484-86b6fe7230ad" />

14 - I also ran the following SQL query to create a regular table that persistently loads the data into BigQuery.

CREATE OR REPLACE TABLE `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned` AS
SELECT * FROM `awesome-icon-484918-n5.ny_taxi.external_yellow_tripdata`;

I observed that a Regular (Native) table named yellow_tripdata_non_partitioned, which is not partitioned, was successfully created.

<img width="1352" height="590" alt="image" src="https://github.com/user-attachments/assets/efd19cda-ae9a-4908-a8e5-7f776ac25f9c" />

Homework Questions

Question 1: What is the number of records for Yellow Taxi data in 2024?

Answer : 20.332.093

For the 2024 Yellow Taxi data, I ran the query SELECT count(*)

FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned`; Result: 20.332.093

<img width="725" height="501" alt="image" src="https://github.com/user-attachments/assets/2c668d20-6ca9-4fb6-b3bb-c8fb01d912c7" />


Question 2 :Data reading estimation

This question aims to help us understand the difference in how BigQuery's External Table and Native Table work.

Here's why:

External Table: BigQuery cannot know the contents of this table beforehand. Because the data resides in GCS (Parquet files), it cannot accurately calculate how much data will be processed before the query runs. Therefore, the estimated amount of data appears as 0 MB (it doesn't know the actual cost until the query runs).

Native Table: BigQuery stores data internally in columnar form. Knowing it will look at the PULocationID column, it accurately calculates the disk size of this column.

I prepared the following query for the External Table Query. Before running it, I observed that it said "This query will process 0 B when run" at the bottom:

SQL
SELECT COUNT(DISTINCT PULocationID) FROM `awesome-icon-484918-n5.ny_taxi.external_yellow_tripdata`;

<img width="783" height="796" alt="image" src="https://github.com/user-attachments/assets/90576e84-02e5-4519-9e8d-4bfc277b746b" />

When I ran the query, I observed the following result.

<img width="808" height="507" alt="image" src="https://github.com/user-attachments/assets/77ce8301-fdca-499b-b85d-e276221b7c14" />

I also prepared the following query for the Native Table query:

SQL
SELECT COUNT(DISTINCT PULocationID) FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned`;

I observed that it said "This query will process 155, 12 MB when run" at the bottom:

<img width="1155" height="802" alt="image" src="https://github.com/user-attachments/assets/658b4463-9a06-4ccb-8166-3cccc28e4953" />

When I ran the query, I observed the following result.

<img width="747" height="484" alt="image" src="https://github.com/user-attachments/assets/7d9b1c10-45a4-4fb9-9c12-65e95cde0032" />

Answer : 0 MB for the External Table and 155.12 MB for the Materialized Table

Question 3. Understanding columnar storage

When I added the DOLocationID column to the SQL query I created earlier to test the Columnar Storage logic, I observed that the estimated byte value increased as shown below.

<img width="998" height="798" alt="image" src="https://github.com/user-attachments/assets/69cf141e-f5ec-4b69-8d2d-e1fc52128e45" />

So I saw that the value was 155.12 MB for a single column, and 310.24 MB for two columns.

Traditional databases (like PostgreSQL and MySQL) store data row by row. If you want to read a row, you have to retrieve all the columns in that row from disk. However, columnar databases like BigQuery keep each column in a separate file. If you only want PULocationID, BigQuery will only open the "file" containing that column. If you add DOLocationID, it will have to open a second file, and the amount of data being processed will naturally increase.

Answer:
BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

Question 4. Counting zero fare trips

I created a COUNT query in BigQuery to filter our data.

SELECT count(*)
FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned`
WHERE fare_amount = 0;

The query result is 8,333, as shown below.

<img width="663" height="524" alt="image" src="https://github.com/user-attachments/assets/38d71166-3000-4984-bf35-5d2715cb593c" />

Answer : 8,333

Question 5. Partitioning and clustering
The most important rule regarding partitioning and clustering is: Partitioning is used for filtering (WHERE), and clustering is used for sorting/grouping (ORDER BY/GROUP BY).

Answer : Partition by tpep_dropoff_datetime and Cluster on VendorID

Why This Strategy?
Partitioning: tpep_dropoff_datetime is a timestamp. If we partition the data by date, when a BigQuery query comes in, it only looks at the "folder" containing the relevant date. This drastically reduces the amount of data scanned (and the bill).

Clustering: VendorID is a categorical data type. When we cluster the data by this column, rows with the same ID are physically stored side-by-side on disk. This makes sorting (order by) much faster.

Question 6. Partition benefits

To solve this problem, I ran the following query inside a table named yellow_tripdata_partitioned_clustered, where I defined a cluster on Vendor_ID and a partition on tpep_dropoff_datetime.

CREATE OR REPLACE TABLE `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `awesome-icon-484918-n5.ny_taxi.external_yellow_tripdata`;

Based on the query results, I observed that the table was created.

<img width="768" height="523" alt="image" src="https://github.com/user-attachments/assets/1aba6536-8817-4d67-8d2e-3dd0b350d71c" />

Query that retrieves different VendorIDs between 2024-03-01 and 2024-03-15 (inclusive) from the yellow_tripdata_non_partitioned table:

SELECT DISTINCT VendorID
FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

Estimated query size : 310.24

<img width="951" height="797" alt="image" src="https://github.com/user-attachments/assets/26ba1cae-07cd-4fc4-b5d5-d020b4c20c0c" />

Query retrieving different VendorIDs from the yellow_tripdata_partitioned_clustered table between 2024-03-01 and 2024-03-15 (inclusive):

SELECT DISTINCT VendorID
FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_partitioned_clustered`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

Estimated query size : 26.84 MB

<img width="609" height="800" alt="image" src="https://github.com/user-attachments/assets/3accee24-7d9a-489a-be45-13b4b67c6f65" />

Answer : 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

Question 7. External table storage

External Table: When BigQuery creates this table, it doesn't copy the data onto itself. It only keeps a "path" (metadata) to where the data is located. When a query is executed, it goes and reads the data from that source in real time.

In our scenario, the data resides as .parquet files on Google Cloud Storage (GCS).

Storage units in Google Cloud Storage are called Buckets.Therefore, the right choice is: GCP Bucket

Answer: GCP Bucket

Question 8. Clustering best practices

In data engineering, there is no one-size-fits-all solution. While clustering is a great feature, it's not always a "best practice" to use.

Why "False"?
Here are some situations where clustering is unnecessary or impractical:

1- Data Size: If your table is very small (typically under 1 GB), the performance increase from clustering is negligible. In fact, BigQuery's metadata management might slightly increase query times on small tables.

2 - Query Patterns: If you don't know beforehand how to filter or sort the data, clustering a random column offers no benefit.

3 - Cost/Write Performance: If data is constantly updated or new data is added very frequently (streaming), clustering will require constant reorganization in the background, creating an additional load on the system.

Cevap: False

Question 9. Understanding table scans

Our query: SELECT count(*) FROM `awesome-icon-484918-n5.ny_taxi.yellow_tripdata_non_partitioned`;

Estimated query size: 0 B

<img width="667" height="816" alt="image" src="https://github.com/user-attachments/assets/1b9c112a-da77-4340-bd9b-d9e11ab26d05" />


Why? BigQuery maintains very detailed metadata in the background for each table. Basic information like the total number of rows in the table is readily available in this metadata. When we type SELECT count(*) (and don't use any WHERE filter), instead of counting millions of rows one by one, BigQuery reads that single number from the metadata file and returns it instantly.



