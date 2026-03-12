
I followed these steps for this assignment:

1 - First, I opened the Docker Desktop application and observed that it was working. 

<img width="245" height="713" alt="image" src="https://github.com/user-attachments/assets/911ea381-cf6b-45ad-9ee7-731269714c10" />

2 - I copied the defined docker-compose.yaml file to the 07-streaming folder under the C drive, and then to the workshop folder under that, and ran the `docker compose build` command in the Terminal under 07-streaming/workshop/.
<img width="1899" height="962" alt="image" src="https://github.com/user-attachments/assets/eff3ce36-1182-4fb6-9ac1-033dbf1a8c17" />
<img width="984" height="401" alt="image" src="https://github.com/user-attachments/assets/0965d5e5-5457-4a1d-a371-9ae2d41e0963" />
 
 Then I ran the `docker compose up -d` command in the Terminal under 07-streaming/workshop/.
 <img width="641" height="140" alt="image" src="https://github.com/user-attachments/assets/af40c426-e7ea-4b76-916f-78c474aae5d9" />

 I installed the kafka-python library by running the `pip install kafka-python` command so I could send and read data from Python to Kafka/Redpanda.
 <img width="664" height="108" alt="image" src="https://github.com/user-attachments/assets/a0ff6ec4-c6a5-46c3-9dc7-7fb9bb3c15c2" />

I ran the `pip show kafka-python` command to check the kafka-python library installation.
 <img width="800" height="189" alt="image" src="https://github.com/user-attachments/assets/cc8596c3-ddfc-48d2-b113-4c155a529245" />

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

Question 4. Tumbling window - pickup location  : To solve this problem, first I installed the pgcli library using the command `pip install pgcli`.
<img width="1488" height="780" alt="image" src="https://github.com/user-attachments/assets/c28f4f96-55fc-4e83-888c-e2b05f92a805" />

Then I ran the command `pgcli -h localhost -p 5432 -u postgres -d postgres` in the terminal to connect to PostgreSQL, and entered 'postgres' as the password.
 <img width="718" height="134" alt="image" src="https://github.com/user-attachments/assets/93671cec-14cc-45fb-bc68-60d0ad1aca31" />

First, I ran the SELECT version(); command to check the PostgreSQL version.
<img width="952" height="134" alt="image" src="https://github.com/user-attachments/assets/b9d5da63-9495-4210-840c-adcc13fc5e1f" />

I used the `\dt` command to list the tables if they existed, and I saw that there were no tables.
<img width="289" height="111" alt="image" src="https://github.com/user-attachments/assets/898ff6e0-ad55-4b2d-891f-83d79aee4a51" />

I created a table named q4_tumbling with the following SQL command:

CREATE TABLE q4_tumbling (
    window_start TIMESTAMP,
    PULocationID INTEGER,
    num_trips BIGINT,
    PRIMARY KEY (window_start, PULocationID)
);

<img width="1298" height="69" alt="image" src="https://github.com/user-attachments/assets/9ec53343-873a-4f03-be77-74e04bf00a34" />

I created a job Python file named q4_tumbling_pickup.py under the workshop/src/job folder. I placed the code in a Github folder.

I submitted the job to Flink by running the command `docker exec -it workshop-jobmanager-1 flink run -py /opt/src/job/q4_tumbling_pickup.py`.

<img width="904" height="37" alt="image" src="https://github.com/user-attachments/assets/18762d43-208c-4e51-8381-b11e612f42af" />

 I accessed the Apache Flink Database by going to the URL address http://localhost:8081.

 <img width="1866" height="967" alt="image" src="https://github.com/user-attachments/assets/32d954e8-1913-40fd-a67a-2a39bd3136f1" />

I reconnected to PostgreSQL using the command `pgcli -h localhost -p 5432 -u postgres -d postgres` and checked the following query.
SELECT PULocationID, num_trips
FROM q4_tumbling
ORDER BY num_trips DESC
LIMIT 3;


<img width="879" height="177" alt="image" src="https://github.com/user-attachments/assets/829cbdd8-4247-4710-af77-56aaab228568" />

Correct answer: → 74

Question 5. Session window - longest streak : To solve this problem, I created a table named q5 session in PostgreSQL using the following SQL code:
CREATE TABLE q5_session (
    PULocationID INTEGER,
    num_trips BIGINT,
    PRIMARY KEY (PULocationID)
);

<img width="1029" height="215" alt="image" src="https://github.com/user-attachments/assets/812c0940-5e7e-43fd-9e8d-0b3469b6b967" />

I created a job file named q5_session_window.py under the workshop/src/job folder. I shared the code on GitHub.

I submitted the job to Flink using the command: `docker exec -it workshop-jobmanager-1 flink run -py /opt/src/job/q5_session_window.py`

<img width="915" height="46" alt="image" src="https://github.com/user-attachments/assets/5000d322-0b9c-4248-8636-08ba7848da4e" />

I saw that both jobs were displayed on the Flink Web Dashboard screen.

<img width="1907" height="500" alt="image" src="https://github.com/user-attachments/assets/da3d25bd-4b3d-4b5f-a5bb-be9d18c730fb" />

I ran the query `SELECT * FROM q5_session ORDER BY num_trips DESC LIMIT 10;` in PostgreSQL and tried to find the answer to the question: How many trips were made in the longest session?

<img width="751" height="292" alt="image" src="https://github.com/user-attachments/assets/7d6fe1b0-b34b-453d-bc25-44f09cc9e068" />

Since the closest value is 31, Answer → 31

Question 6. Tumbling window - largest tip : To answer the question "Which hour had the highest total tip amount?", I created a table named q6_hourly_tip using the following SQL:

CREATE TABLE q6_hourly_tip (
window_start TIMESTAMP,
total_tip DOUBLE PRECISION,
PRIMARY KEY (window_start)
);

I created a Python job file named q6_hourly_tip.py under the workshop/src/job folder. I shared the code on GitHub.

I ran the command `docker exec -it workshop-jobmanager-1 flink run -py /opt/src/job/q6_hourly_tip.py` and submitted the job to Flink.

<img width="868" height="45" alt="image" src="https://github.com/user-attachments/assets/c5ea4b45-6224-4729-9cde-9af72327b8bd" />

I ran the query SELECT * FROM q6_hourly_tip ORDER BY total_tip DESC LIMIT 10; in PostgreSQL and found the answer to the question "Which hour had the highest total tip amount?" as 2025-10-16 18:00:00.

 <img width="731" height="291" alt="image" src="https://github.com/user-attachments/assets/f8251093-b246-48e0-aefc-f7a5d2f2cc2f" />

Answer : 2025-10-16 18:00:00

