
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

7 - 
