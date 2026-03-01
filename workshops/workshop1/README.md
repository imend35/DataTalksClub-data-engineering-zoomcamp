I am detailing the tasks given in Workshop 1 by following the steps below.

Step 1 -  First, I created a folder named taxi-pipeline under C:\Users\Esila Nur Demirci by running the `mkdir taxi-pipeline` command in the cmd terminal. Then I navigated to the relevant directory using the `cd taxi-pipeline` command.
<img width="472" height="88" alt="image" src="https://github.com/user-attachments/assets/c52fd0ae-724a-4c9a-bab4-4dc7a3e5d511" />

Step 2 - To install the dlt MCP Server, I pasted the following code under Settings → Tools and MCP in the Cursor IDE, as a New MCP Server:

Code: {  {
  "mcpServers": {
    "dlt": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "dlt[duckdb]",
        "--with",
        "dlt-mcp[search]",
        "python",
        "-m",
        "dlt_mcp"
      ]
    }
  }
}

Step 3 - I ran the command `pip install "dlt[workspace]"` to install dlt.
<img width="1742" height="887" alt="image" src="https://github.com/user-attachments/assets/7fbdb53c-0a34-4f3b-b2dd-22efd22caef3" />
<img width="1833" height="502" alt="image" src="https://github.com/user-attachments/assets/7c9df0ad-7026-48eb-8102-074f65b63253" />

Step 4 -  I ran the command `dlt init dlthub:taxi_pipeline duckdb` to start the project.
<img width="961" height="384" alt="image" src="https://github.com/user-attachments/assets/1bfe975e-588c-4716-945f-13657ec82dba" />

Step 5 -  I copied and pasted the following instructions to create a new agent via the cursor:

Instructions:

Build a REST API source for NYC taxi data.

API details:
- Base URL: https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api
- Data format: Paginated JSON (1,000 records per page)
- Pagination: Stop when an empty page is returned

Place the code in taxi_pipeline.py and name the pipeline taxi_pipeline.
Use `@dlt rest api` as a tutorial.

During this process, I granted all the permissions , It requested.

Step 6 - All New York taxi files retrieved from the REST API were installed into DuckDB using taxi_pipeline.py, which created a file containing the following code and prompted the execution of the "python taxi_pipeline.py" command. Cursor gave me the following code for taxi_pipeline.py, and when I ran it with the `python taxi_pipeline.py` command, I was in a process that was processing 1000 records per second and taking about 20 hours and still not finished. However, I asked for help on Slack and with a small code change provided by a friend named Michael, I was able to quickly load the nyc_taxi database data with the new taxi_pipeline.py code.

Code change I implemented:

"paginator": {
   "type": "page_number",
   "page_param": "page",
   "base_page": 1,
   "total_path": None,
   "stop_after_empty_page": True,
},

Step 7 - I couldn't delete the file named taxi_pipeline that the cursor created in the .dlt folder due to an error indicating it was linked. Following Michael's code modification, I renamed the pipeline I created nyc_taxi_pipeline and was able to access the dlt dashboard at URL: http://127.0.0.1:2719 by running the `dlt pipeline nyc_taxi_pipeline show` command.
<img width="707" height="171" alt="image" src="https://github.com/user-attachments/assets/8c8f5a8b-e623-4fc2-b43f-622f39a54392" />
<img width="1512" height="878" alt="image" src="https://github.com/user-attachments/assets/389488fa-f129-447e-9896-1c9ea46bc185" />

Question 1  :  Question 1. What is the start date and end date of the dataset? (1 point)

 *  2009-01-01 to 2009-01-31
 *  2009-06-01 to 2009-07-01
 *  2024-01-01 to 2024-02-01
 *  2024-06-01 to 2024-07-01

Answer :  2009-06-01 to 2009-07-01

To answer this question, I ran the following SQL query code on the DLT dashboard.

SELECT 
    MIN(DATE(trip_pickup_date_time))  AS min_start_date,
    MAX(DATE(trip_dropoff_date_time)) AS max_end_date
FROM "nyc_taxi_trips"

<img width="1128" height="612" alt="image" src="https://github.com/user-attachments/assets/e9b01cb0-7591-4dfc-984f-b2feb2118bc6" />


Question 2: What proportion of trips are paid with credit card?
 * 16.66%
 * 26.66%
 * 36.66%
 * 46.66%

   Answer : 26.66%

   To answer this question, I first ran the following SQL query code on the DLT dashboard to find out what payment types are available.
   <img width="1195" height="687" alt="image" src="https://github.com/user-attachments/assets/c7194ea4-ee4b-4390-98e6-282c263daedf" />

Then I ran the following code, which multiplies the number of records with payment type credit by 100 and divides it by the total number of records. 

Code: 
SELECT 
    ROUND(
        100.0 * SUM(
            CASE 
                WHEN LOWER(payment_type) = 'credit' THEN 1 
                ELSE 0 
            END
        ) / COUNT(*),
    2) AS credit_card_percentage
FROM "nyc_taxi_trips"

The result was 26.66%.

 <img width="1340" height="569" alt="image" src="https://github.com/user-attachments/assets/08a307a3-146f-49ff-af35-6b2932842e8d" />

Question 3: What is the total amount of money generated in tips?
*  $4,063.41
*  $6,063.41
*  $8,063.41
*  $10,063.41

Answer : $6,063.41

To solve this problem, I identified the relevant tip column, and since this column named `tip_amt` might be null, I ran the following code: Code:

SELECT 
    ROUND(SUM(COALESCE(tip_amt, 0)), 2) AS total_tips
FROM "nyc_taxi_trips"

The result was 6.063,41

<img width="1163" height="457" alt="image" src="https://github.com/user-attachments/assets/28062f24-ead3-47f3-bac7-fb422a6be449" />


