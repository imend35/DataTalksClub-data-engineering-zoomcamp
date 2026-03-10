I followed these steps for this assignment:

1 - First, I opened the Docker Desktop application and observed that it was working. 

<img width="245" height="713" alt="image" src="https://github.com/user-attachments/assets/911ea381-cf6b-45ad-9ee7-731269714c10" />

2 - I copied the defined docker-compose.yaml file to the 07-streaming folder under the C drive, and then to the pyflink folder under that, and ran the `docker-compose up -d` command in the Terminal under 07-streaming/pyflink/.
<img width="1226" height="634" alt="image" src="https://github.com/user-attachments/assets/1f2a988f-94b5-486e-b5ed-3b0dee1f50fd" />
<img width="1247" height="912" alt="image" src="https://github.com/user-attachments/assets/43ce3612-8623-44a5-b85a-d3699ec02b46" />
<img width="1206" height="904" alt="image" src="https://github.com/user-attachments/assets/a381023f-8510-4d25-9cff-6b2264ebc051" />
<img width="1274" height="950" alt="image" src="https://github.com/user-attachments/assets/23153479-664f-4276-a2aa-a4d32408ac7a" />
<img width="1296" height="721" alt="image" src="https://github.com/user-attachments/assets/97c61d90-317f-486e-a199-8f74994da98a" />
<img width="1197" height="602" alt="image" src="https://github.com/user-attachments/assets/2d8cc08a-90fe-4e1a-9c56-22bc364afb62" />
<img width="671" height="933" alt="image" src="https://github.com/user-attachments/assets/3513c1c4-93b8-4d0d-bf90-a30e658b663d" />
<img width="1894" height="991" alt="image" src="https://github.com/user-attachments/assets/d0f41706-45bb-4b7a-9f7f-36b775768019" />
<img width="759" height="980" alt="image" src="https://github.com/user-attachments/assets/3a9d801c-6716-49cb-9ce0-3bfd057c4566" />
<img width="744" height="964" alt="image" src="https://github.com/user-attachments/assets/359da38e-0ada-4640-aa52-41baa449a6d5" />
<img width="1477" height="871" alt="image" src="https://github.com/user-attachments/assets/b6d6592d-3887-4c00-8f3b-12401c4249b9" />
<img width="1450" height="843" alt="image" src="https://github.com/user-attachments/assets/1eae2044-55e0-4a6a-81c9-83b5bab9a99b" />
<img width="983" height="486" alt="image" src="https://github.com/user-attachments/assets/9a8e7777-b9ce-4f9d-b7f2-c720590d5f97" />

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

I created a .py file named test_kafka and ran the given python test code for the Kafka connection using the command `python test_kafka.py`, and the result I saw was True.
<img width="461" height="50" alt="image" src="https://github.com/user-attachments/assets/020af798-b5c4-4566-bd0b-735cbe298928" />

Queston 4 :  The dataset I used for submitting taxi data is: Green Taxi 2019-10

I created a Python file named send_trips.py, wrote the following code inside it, saved it, and ran it with the `python send_trips.py` command.

<img width="403" height="62" alt="image" src="https://github.com/user-attachments/assets/8f7247e8-f1dd-428f-b766-a037403aa603" />

Rows: 476386
Took: 58.29629850387573

Question 5 : I copied the code from aggregation_job.py, created a file named session_job.py, and modified the code inside it as follows.

To copy the script to Docker, I ran the following command: `docker cp session_job.py pyflink-jobmanager-1:/opt/flink/session_job.py`

<img width="788" height="41" alt="image" src="https://github.com/user-attachments/assets/ae622d84-fd57-43b2-9331-bab2e6df98ac" />

I ran the `docker exec -it pyflink-jobmanager-1 bash` command and I ran the command `flink run -py session_job.py` to submit the job to Flink.
<img width="564" height="58" alt="image" src="https://github.com/user-attachments/assets/b8537ccf-1559-44be-85d0-5f9c31b404c8" />

When I went to the Flink UI URL (http://localhost:8081), I observed that one job was running :
<img width="1909" height="456" alt="image" src="https://github.com/user-attachments/assets/d00d23e6-c918-4021-80a6-196025c00c65" />

I accessed the Postgres database using the command `pgcli -h localhost -p 5432 -u postgres -d postgres`.

<img width="745" height="146" alt="image" src="https://github.com/user-attachments/assets/4dc20ed6-406a-4aba-85b3-b1c08ff15e80" />








