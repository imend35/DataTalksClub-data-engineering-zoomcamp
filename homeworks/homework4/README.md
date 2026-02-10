
To complete this assignment, I want to proceed by selecting the Cloud setup option. I had already uploaded all the data for Yellow and Green Taxi Travel services from 2019 and 2020 to BigQuery Cloud using Kestra.

To prepare this assignment, I followed these steps:

1 - First, I went to https://www.getdbt.com/ to set up dbt Cloud and I created an account.

<img width="1638" height="318" alt="image" src="https://github.com/user-attachments/assets/80c9c077-47b0-4f15-aaf2-4e51ec0735f3" />

2 - I created a project named taxi_rides_ny. I uploaded the Service Account JSON Key file to connect dbt Cloud with our BigQuery data warehouse. I named the dataset dbt_prod for configuring the connection settings.I tested the connection and observed that it connected successfully.

3 - I then connected my GitHub account to the dbt Cloud environment and observed that the development environment was now open.

<img width="1778" height="979" alt="image" src="https://github.com/user-attachments/assets/2dc880b3-fe15-4724-b243-c7a56610a6b1" />

4 - For the assignment, I created all the source files under taxi_rides_ny in the dbt Cloud environment, following the same folder and subfolder hierarchy.
<img width="1194" height="579" alt="image" src="https://github.com/user-attachments/assets/34268583-b65a-44f2-bc4f-969dce7b54cc" />
<img width="541" height="706" alt="image" src="https://github.com/user-attachments/assets/9769eb44-121a-48e9-b90b-a99f53f11505" />
<img width="511" height="395" alt="image" src="https://github.com/user-attachments/assets/37e73bc6-eb1a-4e75-aa2e-afce8c8ff3f6" />

5 - First, before running the `dbt build` or `dbt run` commands, I ran the `dbt clean` command in the dbt terminal to ensure the project was completely clean.
<img width="730" height="534" alt="image" src="https://github.com/user-attachments/assets/70765c56-f81d-4cac-bf67-89a5ed88a346" />

6 - To download and install the external packages (library, etc.) we want to use in our dbt project, I ran the `dbt deps` command.
<img width="695" height="576" alt="image" src="https://github.com/user-attachments/assets/d241ba88-aeba-440b-b30d-cf37e18a64a8" />

7 - To verify that it's running correctly in the development environment, I first run the `dbt build` command in the dbt Cloud terminal and press Enter.
<img width="981" height="602" alt="image" src="https://github.com/user-attachments/assets/5eac70ee-687b-4bb2-adb3-25d2cef67675" />

8 - After observing that it was working without errors, I'm enabling it to run in the production environment as well using the `dbt build --target prod` command.
<img width="955" height="523" alt="image" src="https://github.com/user-attachments/assets/a460c702-ce8e-4bdd-a5c1-dbefab36db75" />

9 -  After successfully running the `dbt build --target prod` command, I observed that the `dbt_prod` folder was successfully created on the Google Cloud BigQuery side.
<img width="710" height="783" alt="image" src="https://github.com/user-attachments/assets/6490fa87-867e-494b-b5cc-959df999ccf7" />

Answers to Questions : 

Question 1 :  Correct Answer: The `int_trips_unioned only` option is the correct one. 

Why? Because unless we explicitly specify otherwise, dbt will only run the target we choose to protect the rest of the project and avoid resource consumption.

Question 2 :  Correct Answer: dbt will fail the test, returning a non-zero exit code. 

Why ? Because The accepted_values test checks the actual data in the model every time it runs. Since a new value (6) appears in the payment_type column and it is not defined in the test configuration, dbt test --select fct_trips will fail and return a non-zero exit code.

Question 3 :  Correct Answer : 12184  

Why ? When I check the number of data entries in the table using the query I created : 

SELECT count(*) FROM `awesome-icon-484918-n5.dbt_prod.fct_monthly_zone_revenue`

I find the number 12184.

<img width="797" height="565" alt="image" src="https://github.com/user-attachments/assets/d9a54125-9f17-4b3c-8c9c-2b42274c9c3e" />

Question 3 :  Correct Answer : East Harlem North

Why ?  To solve this problem, I prepared the following query : 

SELECT 
    pickup_zone,
    SUM(revenue_monthly_total_amount) AS total_revenue_2020
FROM `awesome-icon-484918-n5.dbt_prod.fct_monthly_zone_revenue`
WHERE 
    service_type = 'Green' 
    AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY total_revenue_2020 DESC
LIMIT 1;

As a result, I found East Harlem North to have the maximum total value.
<img width="468" height="534" alt="image" src="https://github.com/user-attachments/assets/eb89775d-395f-47fb-92e7-1d4cffe75ae5" />

Question 4 :  Correct Answer : 384,624

Why ? To solve this problem, I prepared the following query : 

SELECT
    SUM(total_monthly_trips) AS total_trips
FROM `awesome-icon-484918-n5.dbt_prod.fct_monthly_zone_revenue`
WHERE service_type = 'Green'
    AND EXTRACT(YEAR FROM revenue_month) = 2019
    AND EXTRACT(MONTH FROM revenue_month) = 10

As a result, I found 384,624 value.
<img width="613" height="554" alt="image" src="https://github.com/user-attachments/assets/0c473e62-89ce-4191-97fa-375508c8d5b5" />

Question 4 :  Correct Answer : 43,244,693

Why ? To load the 2019 FHV trip data into the BigQuery database, I first created a folder named 04-Analytics_Engineering in the C drive and downloaded all the 2019 csv.gz files into that folder. Then, in the cmd terminal, I navigated to the C:\04-Analytics_Engineering directory and ran the following command:

gsutil -m cp fhv_tripdata_2019-*.csv.gz gs://esila-de-zoomcamp-bucket-2026/fhv/2019/

<img width="912" height="441" alt="image" src="https://github.com/user-attachments/assets/0ed4198f-915d-4b40-aaac-de42971cb3c2" />

I observed that under Bucket, there was a folder named fhv, and under that, a folder named 2019, and under that, there was a folder containing 12 months of data for the year 2019.

<img width="1614" height="679" alt="image" src="https://github.com/user-attachments/assets/4dd00aef-b87e-47a1-b561-230ef588c950" />

I then ran the following command to load this data into BigQuery :

bq load --source_format=CSV --skip_leading_rows=1 --autodetect awesome-icon-484918-n5:zoomcamp.fhv_tripdata_2019 gs://esila-de-zoomcamp-bucket-2026/fhv/2019/fhv_tripdata_2019-*.csv.gz

<img width="1697" height="45" alt="image" src="https://github.com/user-attachments/assets/fe036eb1-7f74-4fcf-bafb-c31e6279846e" />

Thus, I observed that on the BigQuery side, under the Zoomcamp schema, a table named fhv_tripdata_2019 was loading 12 months' worth of data for 2019 in bulk.

<img width="728" height="504" alt="image" src="https://github.com/user-attachments/assets/6e38fd8b-ad00-47e2-9269-8a8fdc3a12c6" />

I added the table named fhv trip data 2019, which was created, to the sources.yml file under tables on the dbt Cloud side by writing the following code: - name: fhv_tripdata_2019
description: Raw FHV trip records for 2019

<img width="518" height="232" alt="image" src="https://github.com/user-attachments/assets/0a5314c3-5ab1-41e9-b04a-ff11d3044a6f" />

I created a file named stg_fhv_tripdata.sql under the models/staging folder in dbt Cloud and prepared the following code within it. I also added the filter criterion, which is `dispatching_base_num IS NULL`.

<img width="603" height="616" alt="image" src="https://github.com/user-attachments/assets/0b9c0c68-b4b5-432b-8de8-cfe07e2f06d3" />

I built the stg_fhv_tripdata file using the command `dbt build --select stg_fhv_tripdata`.

I observed that it worked successfully and that a table named stg_fhv_tripdata was created under the dbt_prod folder on the BigQuery side.

<img width="976" height="425" alt="image" src="https://github.com/user-attachments/assets/319b4cd2-b26e-4d0b-99af-1809f40be8bf" />

<img width="719" height="515" alt="image" src="https://github.com/user-attachments/assets/4ef6d9bc-0dab-4169-a415-37cabe77031c" />

I ran the query SELECT count(*) FROM `awesome-icon-484918-n5.dbt_prod.stg_fhv_tripdata` to find the number of records in the stg_fhv_tripdata table, and the result was 43,244,693.


