I followed these steps for this assignment:

1 - First, I opened the Docker Desktop application and observed that it was working. 

<img width="245" height="713" alt="image" src="https://github.com/user-attachments/assets/911ea381-cf6b-45ad-9ee7-731269714c10" />

2 - I copied the defined docker-compose.yaml file to the 07-streaming folder under the C drive, and then to the workshop folder under that, and ran the `docker compose build` command in the Terminal under 07-streaming/workshop/.
<img width="1899" height="962" alt="image" src="https://github.com/user-attachments/assets/eff3ce36-1182-4fb6-9ac1-033dbf1a8c17" />
<img width="984" height="401" alt="image" src="https://github.com/user-attachments/assets/0965d5e5-5457-4a1d-a371-9ae2d41e0963" />
 
 Then I ran the `docker compose up -d` command in the Terminal under 07-streaming/workshop/.
 <img width="641" height="140" alt="image" src="https://github.com/user-attachments/assets/af40c426-e7ea-4b76-916f-78c474aae5d9" />

Question 1. Redpanda version :  To solve the Redpanda version question, I ran the command `docker exec -it workshop-redpanda-1 rpk version`.

<img width="751" height="152" alt="image" src="https://github.com/user-attachments/assets/1c23f798-fcce-4c8a-a88b-86a30152a07a" />

 Question 2. Sending data to Redpanda :  I ran the command `docker exec -it workshop-redpanda-1 rpk topic create green-trips` to create a topic named `green-trips`.
 
 <img width="776" height="57" alt="image" src="https://github.com/user-attachments/assets/5608cbb6-7cd2-4930-ac8c-968cc5c10d77" />

 To check the topic we created, I ran the command: `docker exec -it workshop-redpanda-1 rpk topic list`.
 
 <img width="649" height="61" alt="image" src="https://github.com/user-attachments/assets/04d97db7-4476-4c4f-bc0b-214b1c2a670f" />

 I created a file named green_producer.py under 07-streaming/workshop/src/producers.
 <img width="540" height="53" alt="image" src="https://github.com/user-attachments/assets/5092969f-fffa-44cd-bd76-57f450c7226b" />
 My measurement is 6.24 seconds, so the closest option is: 10 seconds

Therefore, the answer to Question 2 is: → 10 seconds

 Question 3. Consumer - trip distance : To solve this problem, I created a Python file named green_consumer.py under the workshop folder and shared the code on GitHub. Then, I ran it in the terminal using the command `python green_consumer.py` under the workshop folder. As a result, I found 8506 km. 

 <img width="461" height="38" alt="image" src="https://github.com/user-attachments/assets/4b958a8d-ee94-4e16-b57f-82472fe1821b" />

 Answer : 8506 km


 
 3 - I accessed the Apache Flink Database by going to the URL address http://localhost:8081.
 <img width="1913" height="972" alt="image" src="https://github.com/user-attachments/assets/c576c688-4e87-47ac-a52a-f42f0cf52d4a" />

 4 - I installed the pgcli library using the command `pip install pgcli`.
<img width="1488" height="780" alt="image" src="https://github.com/user-attachments/assets/c28f4f96-55fc-4e83-888c-e2b05f92a805" />

 5-  I installed the kafka-python library by running the `pip install kafka-python` command so I could send and read data from Python to Kafka/Redpanda.
 <img width="664" height="108" alt="image" src="https://github.com/user-attachments/assets/a0ff6ec4-c6a5-46c3-9dc7-7fb9bb3c15c2" />

 6 - I ran the `pip show kafka-python` command to check the kafka-python library installation.
 <img width="800" height="189" alt="image" src="https://github.com/user-attachments/assets/cc8596c3-ddfc-48d2-b113-4c155a529245" />

7 - I ran the command `pgcli -h localhost -p 5432 -u postgres -d postgres` to connect to the PostgreSQL database and executed the `Select 1;` query for verification purposes.
<img width="964" height="271" alt="image" src="https://github.com/user-attachments/assets/b58b4889-91da-421c-b762-115fcd3416eb" />

8 - I created the processed_events and processed_events_aggregated tables by running the following SQL codes: 

CREATE TABLE processed_events (
    test_data INTEGER,
    event_timestamp TIMESTAMP
);

CREATE TABLE processed_events_aggregated (
    event_hour TIMESTAMP,
    test_data INTEGER,
    num_hits INTEGER 
);
I displayed the created tables by listing them using the `\dt` command.

<img width="1144" height="268" alt="image" src="https://github.com/user-attachments/assets/3d24e8ff-066f-4df9-8abe-49c4dd1cb2a4" />

Question 1: Redpanda version : To find the Redpanda version : 

1 - I ran the `docker ps` command to check the container list.
<img width="1898" height="185" alt="image" src="https://github.com/user-attachments/assets/ef8dc4c2-3ab1-40c0-b5dd-89cb861d2427" />

2 - I ran the `docker exec -it redpanda-1 bash` command to enter the container named `pyflink-redpanda-1`.

<img width="553" height="53" alt="image" src="https://github.com/user-attachments/assets/c34d1b1f-e44d-4bbb-8f80-2edb40509a03" />

3 - After entering the container, I used the `rpk version` command and saw that the RPK version was v25.3.9.

 <img width="554" height="180" alt="image" src="https://github.com/user-attachments/assets/899695e7-14c0-4e78-b49a-1a13c69b0f66" />

Answer 1 : v25.3.9.

Question 2 : I ran the `rpk topic create green-trips` command to create a topic named `green-trips`:
<img width="527" height="72" alt="image" src="https://github.com/user-attachments/assets/159d7eaf-0755-4f4b-8ee6-dffa0b747c32" />

I listed the topics using the `rpk topic list` command:
<img width="359" height="63" alt="image" src="https://github.com/user-attachments/assets/1ae16b69-4762-4d98-b267-6114da9f9066" />

Question 3 :  To connect to Kafka using Python, I ran the command `pip install kafka-python`:
<img width="1152" height="41" alt="image" src="https://github.com/user-attachments/assets/c6f4dab2-e3c0-4710-8ee3-4301d5470ccc" />

I created a .py file named test_kafka and ran the given python test code for the Kafka connection using the command `python test_kafka.py` and the result I saw was True.
<img width="461" height="50" alt="image" src="https://github.com/user-attachments/assets/020af798-b5c4-4566-bd0b-735cbe298928" />

Queston 4 :  The dataset I used for submitting taxi data is: Green Taxi 2019-10

I created a Python file named send_trips.py, wrote the following code inside it, saved it, and ran it with the `python send_trips.py` command.

<img width="403" height="62" alt="image" src="https://github.com/user-attachments/assets/8f7247e8-f1dd-428f-b766-a037403aa603" />

Rows: 476386
Took: 58.29629850387573

Question 5 : I copied the code from aggregation_job.py, created a file named session_job.py, and modified the code inside it as follows.

To copy the script to Docker, I ran the following command: `docker cp session_job.py pyflink-jobmanager-1:/opt/flink/session_job.py` 
<img width="843" height="43" alt="image" src="https://github.com/user-attachments/assets/beabe9d9-98fa-47d4-9a20-449fa05d1316" />

I ran the `docker exec -it pyflink-jobmanager-1 bash` command and I ran the command `flink run -py session_job.py` to submit the job to Flink.
<img width="565" height="78" alt="image" src="https://github.com/user-attachments/assets/72b75d74-8e8d-42f9-8a57-bda503d18a69" />

When I went to the Flink UI URL (http://localhost:8081), I observed that one job was running :
<img width="1904" height="883" alt="image" src="https://github.com/user-attachments/assets/7388ff65-44a7-48b4-80d5-481a2e3531c3" />

I accessed the Postgres database using the command `pgcli -h localhost -p 5432 -u postgres -d postgres`. I entered 'postgres' as the password.

With the following SQL query, I first deleted a table named processed_events_aggregated using `drop` and then recreated it: `CREATE TABLE processed_events_aggregated(PULocationID INTEGER, DOLocationID INTEGER, num_hits BIGINT, PRIMARY KEY (PULocationID,DOLocationID));`
<img width="1395" height="139" alt="image" src="https://github.com/user-attachments/assets/b9c6c269-4106-46f3-8e9a-15718d906f67" />
I ran the following query to find which departure and arrival points had the longest uninterrupted taxi ride series : 
`SELECT * FROM processed_events_aggregated ORDER BY num_hits DESC LIMIT 10;`
<img width="877" height="273" alt="image" src="https://github.com/user-attachments/assets/0c19a59d-4930-417f-9501-a87d8e964a64" />







