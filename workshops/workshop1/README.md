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



Step 6 - All New York taxi files retrieved from the REST API were installed into DuckDB using taxi_pipeline.py, which created a file containing the following code and prompted the execution of the "python taxi_pipeline.py" command.




