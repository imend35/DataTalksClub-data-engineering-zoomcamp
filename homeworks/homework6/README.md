
I followed these steps for this assignment :

1 - First, for this assignment, I downloaded the yellow_tripdata_2025-11.parquet file and created a folder named 06-batch under the C drive.

2 - I installed the pyspark library via the Colab application using the command `!pip install pyspark`.
<img width="940" height="99" alt="image" src="https://github.com/user-attachments/assets/1374ad77-3b0a-44ae-92ed-a7931092fe1a" />

3 - I created a Spark Session with the following code:
<img width="437" height="150" alt="image" src="https://github.com/user-attachments/assets/f35e3293-70c9-4f8c-8806-64f3dfe8394a" />

4 - When I checked the Spark version using the `spark.version` command, I saw that the result was 4.0.2. 
<img width="322" height="78" alt="image" src="https://github.com/user-attachments/assets/f1743c93-51d7-415d-a0c1-3e265ac384c3" />

Answer to Question 1: 4.0.2.

5 - I loaded the yellow_tripdata_2025-11.parquet file into the colab file system. I uploaded the yellow_tripdata_2025-11.parquet file to the Colab file system. Using the command `ls -lh yellow_tripdata_2025-11.parquet`, I saw that the file size is 68MB.
<img width="709" height="79" alt="image" src="https://github.com/user-attachments/assets/51abcffe-a5ec-4379-b9b9-fd58107a83b0" />

5 - To read the dataset as a Spark DataFrame, I wrote and ran the code `df = spark.read.parquet("yellow_tripdata_2025-11.parquet")` in colab.I examined the schema with df.printSchema() and observed the first 5 data points with the code df.show(5).
<img width="935" height="616" alt="image" src="https://github.com/user-attachments/assets/496d21c5-a996-42ff-ba50-491d0f75165e" />

6 - I ran the command `df_repartitioned = df.repartition(4)` to partition the dataframe into 4 partitions.

7 - I ran the code `df_repartitioned.write.parquet("yellow_tripdata_2025_11_repartitioned")` to save it as Parquet.

8 - I checked the partition parquet files created with the command `!du -sh yellow_tripdata_2025_11_repartitioned/*`.

<img width="948" height="254" alt="image" src="https://github.com/user-attachments/assets/97b639a1-6aa4-435f-965a-562269a7e2b3" />

9 -  I also checked with the following Python code:

<img width="945" height="355" alt="image" src="https://github.com/user-attachments/assets/c4a3f5b1-d4cf-4607-8cfa-ea481baeead9" />

Answer to Question 2 :  25

10 - I used the following code to calculate the number of taxi trips on November 15th:

from pyspark.sql.functions import col, to_date

dataframe_for_15_november = df.filter(
    to_date(col("tpep_pickup_datetime")) == "2025-11-15"
)

dataframe_for_15_november.count()

<img width="520" height="184" alt="image" src="https://github.com/user-attachments/assets/88f91738-fd0c-403a-a22a-ba2ce72f37e4" />

Answer to Question 3 :  162604

11 - I ran the following code block to calculate the longest travel time:

from pyspark.sql.functions import unix_timestamp, max

df_duration = df.withColumn(
    "trip_hours",
    (unix_timestamp("tpep_dropoff_datetime") - unix_timestamp("tpep_pickup_datetime")) / 3600
)

df_duration.select(max("trip_hours")).show()

<img width="759" height="284" alt="image" src="https://github.com/user-attachments/assets/c1298ef8-0461-4542-8559-2ec06911d51d" />

Answer to Question 4 :  90.64666666666666

12 - First, I checked if Spark was running using the `spark.sparkContext` code ,

<img width="562" height="230" alt="image" src="https://github.com/user-attachments/assets/3642f33a-c364-4966-8eb9-401b00d1a9e8" />

Then I checked the Web URL using the `spark.sparkContext.uiWebUrl` code:

<img width="318" height="84" alt="image" src="https://github.com/user-attachments/assets/8f585df4-a182-44d1-b7ba-1416e8568dc7" />

13 - To find the least frequent vehicle pickup location , Firstly I downloaded the taxi_zone_lookup.csv file and uploaded it to the Colab file system.

I uploaded the file to Spark using the following code : 

zones = spark.read.csv(
    "taxi_zone_lookup.csv",
    header=True,
    inferSchema=True
)

I ran the following code to retrieve the zone names from the Taxi dataset and the Zone dataset by performing an inner join using the PULocationID field in the Taxi dataset and the LocationID field in the Zone dataset:

df_join = df.join(
    zones,
    df.PULocationID == zones.LocationID
)

To find the zone with the least frequent pickup points, I ran the following code, which calculates the number of trips for each zone and sorts them from least to most frequent:
from pyspark.sql.functions import count

df_join.groupBy("Zone") \
    .agg(count("*").alias("trip_count")) \
    .orderBy("trip_count") \
    .show()

<img width="487" height="756" alt="image" src="https://github.com/user-attachments/assets/e5170c33-ccfa-45c9-b399-52676239a2f9" />

According to the table, there are 2 options with trips_count = 1: Arden Heights and Governor's Island. I selected Governor's Island as my answer.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I followed these steps to solve this much more cleanly and professionally with Spark SQL:

1 - In Spark, we can use a DataFrame like an SQL table. To do this, we first create a temp view.

I ran the following code to make the Taxi dataset an SQL table: `df.createOrReplaceTempView("trips")`

I ran the `zones.createOrReplaceTempView("zones")` code to convert the Zone lookup dataset into an SQL table.

Now I have two tables called trips and zones.

<img width="322" height="98" alt="image" src="https://github.com/user-attachments/assets/29c0942e-98f4-4ef4-8af6-9d91a4ca7071" />


2 -  Question 3 — To find the number of trips on November 15th using SQL, I ran the following query:

spark.sql("""
SELECT COUNT(*) as trip_count
FROM trips
WHERE DATE(tpep_pickup_datetime) = '2025-11-15'
""").show()

<img width="470" height="232" alt="image" src="https://github.com/user-attachments/assets/801a62f8-d462-46ec-8b59-c736ead9f55f" />

3 - Question 4 — To find the longest trip value using SQL, I ran the following query code:

spark.sql("""
SELECT MAX(
    (unix_timestamp(tpep_dropoff_datetime) - unix_timestamp(tpep_pickup_datetime))/3600
) AS longest_trip_hours
FROM trips
""").show()

<img width="713" height="246" alt="image" src="https://github.com/user-attachments/assets/fa045cfc-22b4-400b-b7f4-ea2007bf49e2" />

4 - Question 6 — To find the least used zone value using SQL, I ran the following query:

spark.sql("""
SELECT z.Zone, COUNT(*) as trip_count
FROM trips t
JOIN zones z
ON t.PULocationID = z.LocationID
GROUP BY z.Zone
ORDER BY trip_count
LIMIT 1
""").show()

<img width="370" height="301" alt="image" src="https://github.com/user-attachments/assets/138cea13-5790-4651-8f25-872e330e3c0a" />


