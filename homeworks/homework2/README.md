To complete this assignment, I first followed these steps in order to upload the flows to the Kestra interface. 

1. I created a folder named 02-workflow-orchestration under the C drive.                                                        <img width="323" height="27" alt="image" src="https://github.com/user-attachments/assets/45d3ac24-487b-424e-8996-126187ac5c3c" />

2. I created a file named docker-compose.yaml with the given content under the 02-workflow-orchestration folder.I ran the following command in the cmd terminal to create a Dockerfile:

CMD command : echo FROM python:313 > Dockerfile 
<img width="762" height="46" alt="image" src="https://github.com/user-attachments/assets/6eef7daf-bdcd-4620-8887-997ac0a540a8" />

This created the Dockerfile that the ingest service needs.

3. I ran the `docker compose up -d` command to download and run the Kestra and Postgres database in the background.
 <img width="565" height="211" alt="image" src="https://github.com/user-attachments/assets/3bd3fe5d-fa35-4808-89a9-b1342db422ab" />
 4. I accessed the Kestra interface by going to my browser and using http://localhost:8080/ui. I logged in to the Kestra server using the email address admin@kestra.io and the password admin1234, as specified in my compose.yaml file.

    <img width="1766" height="832" alt="image" src="https://github.com/user-attachments/assets/9273a742-a363-4b51-beb5-e4d9b2160238" />
 5. After downloading all the YAML files related to the flows in the entire `flows` folder to a folder named `flows`, I added it to the `02-workflow-orchestration` folder I created under the C drive.
 6. To programmatically add streams to Kestra, I ran the following commands in the terminal.
# Import all flows: assuming username admin@kestra.io and password Admin1234 (adjust to match your username and password)
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

