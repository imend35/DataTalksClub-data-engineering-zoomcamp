# DataTalksClub-data-engineering-zoomcamp

Homework 1

Data Engineering Zoomcamp - Module 1 Assignment: Docker & SQL
This project involves transferring New York Taxi data to a PostgreSQL database running on Docker and analyzing it using SQL.

Question 1: Understanding Docker Images

This question asks us to run a specific Docker image and check the pip (Python package manager) version inside it.

Step 1: I opened the terminal and typed and ran the following command: `docker run -it --entrypoint bash python:3.13`

Step 2: Once inside the container, I typed and ran the following command: `pip --version`

Generally, a current image like python:3.13 includes the latest pip versions. Based on a 2025/2026 projection, this image will typically contain a pip version from the 25.x series.

<img width="602" height="55" alt="image" src="https://github.com/user-attachments/assets/67a6f22a-fa75-490d-8273-9bac426ede0e" />

According to this result, 25.3 is the answer to our question.

Question 2: Docker Networking

This question helps us understand how Docker containers communicate with each other. We want to connect from the pgadmin container to the db (Postgres) container.

Services in the same docker-compose.yaml file reach each other using their service names (hostnames).

The internal ports of the containers are important. The internal port for the db service is 5432. (The fact that it is open to the outside as 5433 does not affect another container's ability to reach it internally).

Parameters:

Hostname: db

Port: 5432

Answer: db:5432

Data Preparation: To solve questions 3, 4, 5, and 6, I first need to load the data into the database. I have tried to follow the steps below one by one.

Step-by-Step Implementation Process
Preparing the Environment : 
First, we defined the infrastructure where the project will run using the docker-compose.yaml file. This file combines the Postgres and pgAdmin services on a network.

1- I downloaded the given .parquet and .csv files.

2. I transferred this data to PostgreSQL using Python (Pandas) and SQL Alchemy. To do this, I followed these steps:
   
   Step 1: Preparing the Necessary Libraries :
   To import the data into the Postgres database, I first checked and installed the following libraries in the terminal, then typed and ran the following:

      Terminal Code :pip install pandas sqlalchemy psycopg2-binary pyarrow
             
     <img width="1370" height="283" alt="image" src="https://github.com/user-attachments/assets/6886d71c-d2fb-4eda-bb99-e865b34d2924" />

 Step 2: Connection (Engine) Setup :          
  I tried to create a "bridge" to the database using SQLAlchemy. A Python file named ingest_data.py was created. The docker-compose.yaml file contained the necessary data (host, password, username, etc.) for establishing a connection to write the data from the green_tripdata_2025-11.parquet and taxi_zone_lookup.csv files to the ny_taxi database as a table, all within the ingest_data.py file.
  
   Based on the information in the docker-compose.yaml file, I built this bridge using the following steps: 
  When we look at your `docker-compose` file, the information is as follows:

   User: `postgres` (as written in the POSTGRES_USER section)

   Password: `postgres` (as written in the POSTGRES_PASSWORD section)

   Host: `localhost` (If you are running the code on your own computer)

   Port: 5433 (Since the `docker` file says '5433:5432', we connect via 5433 from outside)

   Database Name (DB Name): `ny_taxi` (as written in the POSTGRES_DB section)
  
  I ran the following code in the terminal. I ran Python to enable it to connect to the database and process the data. it wrote to PostgreSQL, where both the .parquet and .csv files were corrupted. The data was transferred from the local machine (or from within Docker) to the ny_taxi database in PostgreSQL.
     
   Teminal Code :python ingest_data.py
   
   <img width="547" height="65" alt="image" src="https://github.com/user-attachments/assets/c2170479-c6df-4db9-aa6d-b308719a7a84" />

 Step 3:  Working with Docker Containers
    
  1. To have Docker install and start Postgres in the background, I ran the following code in the terminal.Teminal Code :docker-compose up -d                                                                                                                                          <img width="1024" height="584" alt="image" src="https://github.com/user-attachments/assets/c40302fd-e56e-4734-a9f7-e6d9bf7a7def" />
  2. I created the Dockerfile.The Dockerfile helped us create a standard structure by packaging all the software requirements needed for my data upload script, ensuring the project could be deployed smoothly and quickly on any platform.
  3. Since I'll be running the code inside Docker, I now need to use `db` instead of `localhost` in the connection setup. I've made the necessary corrections in my Python code as follows.
     URL = 'postgresql://postgres:postgres@db:5432/ny_taxi'
  4. I added the ingest service to your existing docker-compose.yaml file.
  5. By running the following command in the terminal: Terminal Code : docker-compose up --build                                                                                                                                                                                   I enabled Docker to read the Dockerfile and create an image, Postgres started up, the Python container ran, it read the data and transferred it to the container named `db`, and the data is now in Postgres.
  6. pgAdmin, running on Docker, is a visual tool used to store the database and run SQL queries. I followed these steps to run the queries.

   6.1. I logged into pgAdmin
      I opened my browser and went to http://localhost:8888
      I used the login information we specified in the docker-compose.yaml file:
       Email: pgadmin@pgadmin.com 
       Password: pgadmin

   6.2. When I logged in, I clicked the "Add New Server" button in the menu on the left or on the main screen. In the General tab, I named it DataTalks_Postgres.
      I entered the following information: 
         Host name/address: db
         Port: 5432
         Maintenance database: ny_taxi
         Username: postgres
         Password: postgres and saved it by clicking the save button.

   6.3. After the connection was successful, I found the database in the left menu under:
  Servers > DataTalks_Postgres > Databases > ny_taxi, then went to Schemas > public > Tables and observed that the tables named green_tripdata and taxi_zone_lookup had been created.
              <img width="246" height="323" alt="image" src="https://github.com/user-attachments/assets/7a42dbda-5061-469f-9341-816836af57a2" />

  Question 3 : Counting short trips
  For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

  The SQL query I created for this question is as follows:

   SELECT count(1)
   FROM green_tripdata
   WHERE lpep_pickup_datetime >= '2025-11-01' 
    AND lpep_pickup_datetime < '2025-12-01'
    AND trip_distance <= 1;

   Query Result: 8007
 
   <img width="740" height="523" alt="image" src="https://github.com/user-attachments/assets/006d216f-c462-4603-a343-c2a722394d6c" />

Question 4. Longest trip for each day
   Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors). Use the pick up time for your calculations.
   
   The SQL query I created for this question is as follows:

   SELECT 
      CAST(lpep_pickup_datetime AS DATE) AS pickup_day, MAX(trip_distance) AS max_dist
   FROM green_tripdata
   WHERE trip_distance < 100
   GROUP BY pickup_day
   ORDER BY max_dist DESC
   LIMIT 1;

   Query Result: 2025-11-14

   <img width="629" height="529" alt="image" src="https://github.com/user-attachments/assets/b41a008d-6af8-4cf1-b90a-852503cfe2b5" />

Question 5. Biggest pickup zone
   Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

   The SQL query I created for this question is as follows:

   SELECT 
    z."Zone", 
    SUM(t.total_amount) AS total_sum
   FROM green_tripdata t
   JOIN taxi_zone_lookup z ON t."PULocationID" = z."LocationID"
   WHERE CAST(t.lpep_pickup_datetime AS DATE) = '2025-11-18'
   GROUP BY z."Zone"
   ORDER BY total_sum DESC
   LIMIT 1;

  Query Result: East Harlem North
  
   <img width="664" height="528" alt="image" src="https://github.com/user-attachments/assets/4aef0546-3c78-468c-a8f1-82ea2c69b4f8" />

Question 6. Largest tip
   For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?
   Note: it's tip , not trip. We need the name of the zone, not the ID.

The SQL query I created for this question is as follows:
      
 SELECT 
    drop_z."Zone" AS dropoff_zone, 
    MAX(t.tip_amount) AS max_tip
 FROM green_tripdata t
 JOIN taxi_zone_lookup pick_z ON t."PULocationID" = pick_z."LocationID"
 JOIN taxi_zone_lookup drop_z ON t."DOLocationID" = drop_z."LocationID"
 WHERE pick_z."Zone" = 'East Harlem North'
   AND t.lpep_pickup_datetime >= '2025-11-01'
   AND t.lpep_pickup_datetime < '2025-12-01'
  GROUP BY drop_z."Zone"
  ORDER BY max_tip DESC
  LIMIT 1;

 Query Result: Yorkville West
 
Question 7. Terraform Workflow
Which of the following sequences, respectively, describes the workflow for:

* Downloading the provider plugins and setting up backend,
* Generating proposed changes and auto-executing the plan
* Remove all resources managed by terraform

The step-by-step process I followed to find the solution:

Building infrastructure with Terraform (Infrastructure as Code) is one of the most fundamental competencies in modern data engineering.

As a first step, we need to set up the system and prepare the basic files.

Step 1: Preparation and Installation
First, let's prepare the environment where Terraform will operate.

Terraform Installation: I downloaded the AMD64 binary terraform.exe file for Windows 64-bit from the website https://developer.hashicorp.com/terraform/install#windows and placed it on a computer named C:\Terraform.

I verified the installation using the `terraform -v` command in the terminal.

 <img width="465" height="78" alt="image" src="https://github.com/user-attachments/assets/29c772b5-52a2-490d-a1af-1b028565ab0f" />

Step 2: Google Cloud Authentication (Service Account)

To create the key that Terraform needs to perform operations:

* I created a Service Account named terraform-runner through the Google Cloud Console.

<img width="1116" height="610" alt="image" src="https://github.com/user-attachments/assets/f5a3ee03-b73c-427b-a7b0-0f72717e180c" />

* I granted Storage Admin and BigQuery Admin privileges to this account.

* I downloaded a JSON file named awesome-icon-484918-n5-6e0f8d98aacb.json containing the credentials and securely placed it in my working folder, C:\Terraform.

Step 3: Preparing Terraform Code

* In the main.tf file under terraform_basic, I configured the settings to connect to Google Cloud.

* In the variables.tf file under terraform_with_variables, I assigned information such as Project ID, region, and bucket names to variables to make the code more flexible.

  Step 4: Running the Terraform Lifecycle
To deploy the code we prepared, I applied Terraform's standard workflow.

I ran the following codes sequentially in the terminal:

1. terraform init: I downloaded the necessary Google plugins and started the workspace.

    <img width="643" height="336" alt="image" src="https://github.com/user-attachments/assets/da7ac54d-8de7-4f9a-862c-3edc79bca1ab" />

2. Terraform plan: We performed a bug check and got a preview of what will be created.

    <img width="1132" height="966" alt="image" src="https://github.com/user-attachments/assets/779753ab-e80d-4667-8c0b-cfe172154e77" />

3. Terraform apply: I have given my consent for the creation of resources in the real world (on the GCP).

    <img width="1126" height="950" alt="image" src="https://github.com/user-attachments/assets/33ba4b5b-5786-4f1f-a3a8-dec94a42e390" />

    <img width="969" height="218" alt="image" src="https://github.com/user-attachments/assets/51698e5e-3382-4b05-985d-7c290d3f2c1d" />

4. Terraform Destroy: I have completed the assignment and will no longer be using the resources, so I have deleted all the structures we created.

    <img width="1402" height="761" alt="image" src="https://github.com/user-attachments/assets/d8d85f95-1966-411d-9744-b1aa47a8c216" />

    <img width="940" height="858" alt="image" src="https://github.com/user-attachments/assets/5fd75992-e689-4123-b38a-c65f5685555f" />

Now, regarding our question:

1. Downloading provider plugins and setting up the backend
This is the Initialization phase. Terraform needs to recognize the providers (GCP, AWS, etc.) in the main.tf file and download the necessary ones.

Command: terraform init

2. Creating modified disruptions and automatically executing the plan
This actually asks about a combination of two interruptions. First, a plan is created, then this plan is implemented (executed). However, since the question focuses on the "executing the plan" (uploading/creating) unit, the main command is the one that removes the resources internally.

Command: terraform apply (Note: normally terraform plan shows plan changes, while terraform apply executes this plan.)

3. Removing all resources managed by Terraform
This is the "destroying infrastructure" phase. It securely deletes all created resources from the cloud.

Command: terraform destroy
  Answer : terraform init, terraform apply -auto-approve, terraform destroy
