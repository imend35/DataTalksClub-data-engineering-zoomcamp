# DataTalksClub-data-engineering-zoomcamp

Homework 1

Data Engineering Zoomcamp - Module 1 Assignment: Docker & SQL
This project involves transferring New York Taxi data to a PostgreSQL database running on Docker and analyzing it using SQL.

🛠️ Technologies Used
Docker & Docker Compose: Containerization and orchestration of applications.

PostgreSQL: Relational database.

pgAdmin 4: Database management interface.

Python (Pandas & SQLAlchemy): Data processing and ingestion.

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
    
  1. I created a text file named requirements.txt so that we can run the Python code inside a Docker container. I wrote the following inside and saved it as a txt file:

  pandas
  sqlalchemy
  psycopg2-binary
  pyarrow

  2. To list running containers: I ran the following code in the terminal.
     Code : docker ps
  3. I created the Dockerfile.
  4. 
     

  
  
      2. Code : docker-compose --version
         <img width="416" height="40" alt="image" src="https://github.com/user-attachments/assets/faa91aa9-75e1-4ff4-855f-5be58b84afae" />
      5. Code :
      6. Code : docker-compose up -d
         <img width="1024" height="584" alt="image" src="https://github.com/user-attachments/assets/c40302fd-e56e-4734-a9f7-e6d9bf7a7def" />
      7. Code : docker-compose up --build
         <img width="998" height="83" alt="image" src="https://github.com/user-attachments/assets/bf158c14-19ba-4a9f-9617-44771c87ca71" />

  
   
   Step 3: Pandas sometimes interprets date columns (datetime) as plain text. To avoid errors in SQL queries, I've tried to add the necessary datetime data type conversion.
   
   Step 4: docker ps 
      




  



  SQLAlchemy kullanarak veritabanına bir "köprü" kurman

4. green_tripdata_2025-11 tablosu ve taxi_zone_lookup tablolarını 
