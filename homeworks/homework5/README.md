
I completed my studies for Week 5's assignment by following these steps:
1 - To install and use Bruin CLI, I ran the command `curl -LsSf https://getbruin.com/install/cli | sh` in the VSCode GitBash terminal. 
<img width="594" height="182" alt="image" src="https://github.com/user-attachments/assets/51156c3a-eef7-49d4-bd64-7007d3d896bb" />

2 - I checked the version of Bruin that was installed using the `bruin version` command.
<img width="441" height="78" alt="image" src="https://github.com/user-attachments/assets/aae660b4-1ffc-4f29-b23d-b58d3328ec65" />

3 -  I copied the bruin.exe file from the bruin_Windows_x86_64.zip folder to the C drive. Then I ran the command `bruin init zoomcamp my-pipeline` in the terminal. So, it created a `bruin` folder under the C drive and created the `.bruin.yml` file and the `my-pipeline` folder project structure inside it. I then followed the steps in the 03-nyc-taxi-pipeline.md file, updating the contents of each file with the information provided in that file.
<img width="346" height="311" alt="image" src="https://github.com/user-attachments/assets/1cc2ec0e-3e57-49ec-b766-1d99ced69085" />

QUESTİONS : 

Question 1. Bruin Pipeline Structure
In a Bruin project, what are the required files/directories?

Answer : .bruin.yml and assets/

Why ? In a Bruin project, two essential components are required for the system to recognize a directory as a "project" and manage assets:

.bruin.yml: This is the project's identifier. Database connections (like what we did earlier for DuckDB), environment variables, and general project settings are stored here.

assets/: This is the main folder where the data processing logic (SQL queries, Python scripts, or the .asset.py files you just created) resides.

Question 2. Materialization Strategies
You're building a pipeline that processes NYC taxi data organized by month based on pickup_datetime. Which materialization strategy should you use for the staging layer that deduplicates and cleans the data?

 Answer : time_interval

 Why ? Best Strategy for the Staging Layer: time_interval
Why time_interval and not others?

Deduplication Requirement: If we use append, duplicate records are created in the staging layer when the same data is accidentally processed twice. time_interval, on the other hand, first cleans a specific time range (e.g., October 2024) and then rewrites that range (idempotency).

Efficiency: The replace strategy deletes all historical data and reloads it from scratch every time. This is both costly and very slow for millions of rows of taxi data.

Business Logic: Since the data is already organized monthly, processing only the data for the current month (incremental based on a time column) is the most efficient method.

Question 3. Pipeline Variables
You have the following variable defined in pipeline.yml:

variables:
  taxi_types:
    type: array
    items:
      type: string
    default: ["yellow", "green"]
How do you override this when running the pipeline to only process yellow taxis?

Answer : bruin run --var 'taxi_types=["yellow"]'

Why?:
--var: This is the standard parameter used to assign variables in Bruin.

'["yellow"]': Since the variable type is an array, it is essential to define it as a list within square brackets, even if it contains only one element. The quotation marks (' ') are used to prevent the terminal (Git Bash or PowerShell) from misinterpreting the parentheses.

Question 4. Running with Dependencies
You've modified the ingestion/trips.py asset and want to run it plus all downstream assets. Which command should you use?

Answer : bruin run --select ingestion.trips+

Why ? Reasons:

--select: This is the main flag in Bruin that determines which assets to run.

+ Sign (Downstream Operator): Adding a + sign to the end of the asset name means "run this asset and all subsequent (downstream) assets dependent on it".

Example: asset_name+ -> Itself + Subsequent assets.

Example: +asset_name -> Itself + Previous assets (Upstream).

Why are the others wrong?: --all runs the entire project, while --downstream or --recursive are not the switches used for this function in Bruin's standard instruction set.

Question 5. Quality Checks
You want to ensure the pickup_datetime column in your trips table never has NULL values. Which quality check should you add to your asset definition?

Answer : not_null: true

Why ? Reasons:
not_null: Guarantees that a column will not be left empty (NULL). If the pickup_datetime column is empty, Bruin will consider this test a failure and warn you.

unique: Ensures that the data is unique (uniqueness).

positive: Checks that numerical values ​​are greater than zero (such as amount or quantity).

accepted_values: Allows the column to only accept specific values ​​(e.g., "Yellow", "Green").

Question 6. Lineage and Dependencies
After building your pipeline, you want to visualize the dependency graph between assets. Which Bruin command should you use?

 Answer : bruin lineage

 Why ? Reasons:
Lineage: In the Bruin ecosystem, this command presents the dependency relationships between assets (tables, Python files, SQL queries) both as a tree structure in the terminal and as a visual graph in the browser.

Purpose: It allows you to see which table is fed by which asset. If an asset fails, you can instantly identify which downstream tables will be affected by this error.

Question 7. First-Time Run

You're running a Bruin pipeline for the first time on a new DuckDB database. What flag should you use to ensure tables are created from scratch?

Answer : --full-refresh

Why ? Reasons:
--full-refresh: Instructs Bruin to "drop/truncate existing tables and rebuild everything from scratch according to the schema I defined." It's typically used to clean up data during initial setups or when data quality deteriorates.

--init: Usually used when creating the project folder structure.

--create or --truncate: These aren't the primary flags used to create tables from scratch among Bruin's standard "run" commands.
