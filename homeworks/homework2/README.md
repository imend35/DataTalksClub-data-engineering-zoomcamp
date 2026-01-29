To complete this assignment, I first followed these steps in order to upload the flows to the Kestra interface. 

1. I created a folder named 02-workflow-orchestration under the C drive.

 <img width="323" height="27" alt="image" src="https://github.com/user-attachments/assets/45d3ac24-487b-424e-8996-126187ac5c3c" />

2. I created a file named docker-compose.yaml with the given content under the 02-workflow-orchestration folder.I ran the following command in the cmd terminal to create a Dockerfile:

CMD command : echo FROM python:313 > Dockerfile 

<img width="762" height="46" alt="image" src="https://github.com/user-attachments/assets/6eef7daf-bdcd-4620-8887-997ac0a540a8" />

This created the Dockerfile that the ingest service needs.

3. I ran the `docker compose up -d` command to download and run the Kestra and Postgres database in the background.

 <img width="565" height="211" alt="image" src="https://github.com/user-attachments/assets/3bd3fe5d-fa35-4808-89a9-b1342db422ab" />

   Additionally, to reactivate the Google Cloud Service that was canceled due to the JSON Key file I shared for my first assignment, I ran the Terraform commands again in the terminal.
 
 4. I accessed the Kestra interface by going to my browser and using http://localhost:8080/ui. I logged in to the Kestra server using the email address admin@kestra.io and the password admin1234, as specified in my compose.yaml file.

 <img width="1766" height="832" alt="image" src="https://github.com/user-attachments/assets/9273a742-a363-4b51-beb5-e4d9b2160238" />

 5. After downloading all the YAML files related to the flows in the entire `flows` folder to a folder named `flows`, I added it to the `02-workflow-orchestration` folder I created under the C drive.

 6. To programmatically add streams to Kestra, I ran the following commands in the terminal.

Import all flows: assuming username admin@kestra.io and password Admin1234 (adjust to match your username and password)

curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/01_hello_world.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/02_python.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/03_getting_started_data_pipeline.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/04_postgres_taxi.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/05_postgres_taxi_scheduled.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/06_gcp_kv.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/07_gcp_setup.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/08_gcp_taxi.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/09_gcp_taxi_scheduled.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/10_chat_without_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/11_chat_with_rag.yaml

<img width="1403" height="353" alt="image" src="https://github.com/user-attachments/assets/88c441ea-334f-46cb-ada2-d196c1027608" />

 7 - When I clicked the Flows tab on the left side of the Kestra interface, I observed the following flows appearing.

  <img width="1844" height="775" alt="image" src="https://github.com/user-attachments/assets/038e2cd1-4d03-41f0-a039-60955ea6e597" />

 8 -  I manually uploaded all the flows one by one from the flows folder using the import button in the Kestra interface.
  
<img width="994" height="765" alt="image" src="https://github.com/user-attachments/assets/c396b8af-53c1-4232-b6a0-2c21c91db657" />

 9 - I wanted to run and examine the 01_hello_world stream. I clicked on the 01_hello_world stream and pressed the Execute button in the upper right corner. I named it esila_hello_world and clicked the Execute button.
 
 <img width="1819" height="460" alt="image" src="https://github.com/user-attachments/assets/dcf9b90d-c2b1-44a6-85cf-d3a02e592ac4" />
 
 10 - In the Executions tab, I observed that the workflow was running successfully.
 
 <img width="1835" height="696" alt="image" src="https://github.com/user-attachments/assets/2cd0c8c4-a731-4ee9-8a14-f285c0fbd9be" />
 
 11 -  I've successfully run my first stream, and now I want to run my Python stream, but first I need to install the Kestra library using the `pip install kestra` command. So I ran the `pip install kestra` command in the cmd terminal.
 
 <img width="1388" height="575" alt="image" src="https://github.com/user-attachments/assets/6178f9c9-5926-4ec2-b225-60885cf8caab" />
 
12 - I selected the 02_python.yaml file in the Flows tab of the Kestra interface and ran it using the Execution button.
     In the Executions tab, I observed that the workflow was running successfully.
<img width="1787" height="384" alt="image" src="https://github.com/user-attachments/assets/8ecca2bc-d46a-42c3-89d3-62fe7e4ea0cd" />

13 : I updated the 06_gcp_kv.yaml file by copying the content information from my own project and the Google Cloud JSON Key file. I executed the 06_gcp_kv.yaml stream via Kestra and observed that it worked successfully.

<img width="1821" height="714" alt="image" src="https://github.com/user-attachments/assets/b650f189-0d9f-4b13-9ed7-dd3bb7e41cb4" />

14 : I then executed the 07_gcp_setup.yaml stream via Kestra and observed that it worked successfully.

<img width="1839" height="721" alt="image" src="https://github.com/user-attachments/assets/433cbaad-1c9b-46ae-afeb-d4ab02885264" />

15 : On the Flow screen, I selected the 09_gcp_taxi_scheduled.yaml flow and on the Triggers tab of the Flow screen, I selected Green Schedule.

Start Date: 2019-01-01 (Saat 00:00:00) ve End Date: 2021-07-31 (Saat 23:59:59)  seçtim. Exceute Backfill butonuna bastım.

<img width="1786" height="737" alt="image" src="https://github.com/user-attachments/assets/d9b6fd82-0414-4e91-bcef-3c56096785fd" />

16: I saw that CSV files were being uploaded under Bucket.

<img width="1673" height="906" alt="image" src="https://github.com/user-attachments/assets/59c2f4d2-5282-438a-a290-009c8dec6e6e" />

17 : I also performed the same Backfill Execute process for the Yellow Schedule with a Start Date of 2019-01-01 (00:00:00) and an End Date of 2021-07-31 (23:59:59), and ensured that the Yellow CSV files were uploaded to Google Cloud.

<img width="1662" height="741" alt="image" src="https://github.com/user-attachments/assets/fae2ddbd-27aa-4f99-950f-df4971e92459" />

18 : I observed that the yellow_tripdata table, which combines the data from the relevant dates in the yellow CSV files I uploaded, and the green_tripdata table, which combines the data from the relevant dates in the green CSV files I uploaded, were created under the zoomcamp dataset I created within BigQuery.

<img width="1574" height="874" alt="image" src="https://github.com/user-attachments/assets/a42706f8-2b36-49c1-b61a-e5a1ceaa0aab" />

<img width="1680" height="879" alt="image" src="https://github.com/user-attachments/assets/b60735ad-fc2d-482c-b694-fe4e5ec68398" />

Quiz Questions
Complete the quiz shown below. It's a set of 6 multiple-choice questions to test your understanding of workflow orchestration, Kestra, and ETL pipelines.

1 - Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?
128.3 MiB
134.5 MiB
364.7 MiB
692.6 MiB

Answer : 134.5 MİB

I found the file in the Google Cloud Bucket List and saw a size value of 134.5 in the Size section.

<img width="1044" height="23" alt="image" src="https://github.com/user-attachments/assets/a01a49eb-72c0-4d82-bee0-3c65a8c35ec4" />


2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?
{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv
green_tripdata_2020-04.csv
green_tripdata_04_2020.csv
green_tripdata_2020.csv

Answer : green_tripdata_2020-04.csv

Why?
The variable definition in Kestra (for example, in files numbered 04 or 08) is as follows:

file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"

The question gives us the inputs:
taxi: green
year: 2020
month: 04

When Kestra renders these values ​​into the template:
{{inputs.taxi}} is replaced with green.
_tripdata_ remains as is.
{{inputs.year}} is replaced with 2020.
The hyphen remains.

{{inputs.month}} is replaced with 04.
The .csv extension is added.

Answer : green_tripdata_2020-04.csv

3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?
13,537.299
24,648,499
18,324,219
29,430,127

Answer : 24,648,499

I ran the following SQL query on the yellow_tripdata table under the zoomcamp schema uploaded to Google Cloud, and the result I found is: 24648499.

SELECT count(*)
FROM `awesome-icon-484918-n5.zoomcamp.yellow_tripdata`
WHERE filename LIKE 'yellow_tripdata_2020-%'

<img width="1534" height="384" alt="image" src="https://github.com/user-attachments/assets/fe0347f8-ac98-4f72-bceb-c5ffcdf73396" />

4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?
5,327,301
936,199
1,734,051
1,342,034

Answer : 1,734,051

I retrieved Green Taxi data for all CSV files from 2020 using the following SQL query and found a result of 1,734,051.

SELECT count(*)
FROM `awesome-icon-484918-n5.zoomcamp.green_tripdata`
WHERE filename LIKE 'green_tripdata_2020-%'

<img width="1425" height="746" alt="image" src="https://github.com/user-attachments/assets/afba1f52-1af9-468c-b4bc-9ae608a8268e" />

5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?
1,428,092
706,911
1,925,152
2,561,031

Answer : 1,925,152

I extracted the Yellow Taxi data from the March 2021 CSV file using the following SQL query and found a result of 1,925,152.

SELECT count(*)
FROM `awesome-icon-484918-n5.zoomcamp.yellow_tripdata`
WHERE filename = 'yellow_tripdata_2021-03.csv'

<img width="1425" height="692" alt="image" src="https://github.com/user-attachments/assets/cb69c083-bfd0-40a1-a7b6-18dc30d4afe1" />

6. How would you configure the timezone to New York in a Schedule trigger?
Add a timezone property set to EST in the Schedule trigger configuration
Add a timezone property set to America/New_York in the Schedule trigger configuration
Add a timezone property set to UTC-5 in the Schedule trigger configuration
Add a location property set to New_York in the Schedule trigger configuration

Answer : Add a timezone property set to America/New_York in the Schedule trigger configuration

Why?
Kestra's scheduled tasks (Schedule triggers) use Java's ZoneId structure. This structure accepts the IANA Time Zone Database format for time zones (e.g., Europe/Istanbul, America/New_York).

Using America/New_York automatically takes Daylight Saving Time into account.

If you use UTC-5, your schedule will shift by 1 hour when it's Daylight Saving Time (UTC-4).

Here's how it's used in the code:
triggers:
  - id: schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *"
    timezone: "America/New_York" 
