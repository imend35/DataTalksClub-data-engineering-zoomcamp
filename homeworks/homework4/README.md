
To complete this assignment, I want to proceed by selecting the Cloud setup option. I had already uploaded all the data for Yellow and Green Taxi Travel services from 2019 and 2020 to BigQuery Cloud using Kestra.

To prepare this assignment, I followed these steps:

1 - First, I went to https://www.getdbt.com/ to set up dbt Cloud and I created an account.

<img width="1638" height="318" alt="image" src="https://github.com/user-attachments/assets/80c9c077-47b0-4f15-aaf2-4e51ec0735f3" />

2 - I created a project named taxi_rides_ny. I uploaded the Service Account JSON Key file to connect dbt Cloud with our BigQuery data warehouse. I named the dataset dbt_prod for configuring the connection settings.I tested the connection and observed that it connected successfully.

3 - I then connected my GitHub account to the dbt Cloud environment and observed that the development environment was now open.

<img width="1778" height="979" alt="image" src="https://github.com/user-attachments/assets/2dc880b3-fe15-4724-b243-c7a56610a6b1" />

4 - I right-clicked on 'models' under File Explorer and created a folder named 'dbt_prod_staging'. I created a folder named dbt_prod_staging by right-clicking on 'models' under File Explorer. I also created folders named dbt_prod_intermediate and dbt_prod_marts.

<img width="357" height="298" alt="image" src="https://github.com/user-attachments/assets/9d9fb0e4-a5df-49ce-8162-fbec7f0826de" />

5 - 
