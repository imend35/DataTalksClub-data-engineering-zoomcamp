
### Step 1 — Google Cloud Environment Setup

In the first step of the project, I set up the cloud environment on **Google Cloud Platform (GCP)** to support the data engineering pipeline.

I created a dedicated GCP project to host all infrastructure components required for the pipeline. My Project Name is : ai-open-source-intelligence

<img src="images/img1.jpg" width="700">

Within this project, I enabled the core services needed for data storage, processing, and access management.

The following services were activated:

* **BigQuery**, which serves as the data warehouse for analytical queries and large-scale data processing
* **Google Cloud Storage (GCS)**, which acts as the data lake layer for storing raw and intermediate data
* **Identity and Access Management (IAM)**, which is used to securely manage permissions and access control across the project

To allow the pipeline components to securely interact with Google Cloud services, I created a **service account** and assigned the necessary roles, including BigQuery and Cloud Storage administrative permissions.

<img src="images/img2.jpg" width="700">

I generated a key for the Service Account, downloaded the json.key file, and placed it in the C:\Terraform\ai-open-source-intelligence-platform\terraform folder that I created for my project.

<img src="images/img3.jpg" width="700">

This initial setup established the cloud foundation required for building and running the end-to-end data pipeline.

### Step 2 — Infrastructure Provisioning with Terraform

In the second step of the project, I provisioned the core cloud infrastructure using **Terraform** in order to automate the creation of the resources required for the data pipeline.

Using Infrastructure as Code (IaC), I defined the infrastructure components in Terraform configuration files and deployed them programmatically to Google Cloud Platform.

First, I configured the **Google Cloud provider** within Terraform and connected it to my GCP project using a service account credential. This allowed Terraform to securely interact with Google Cloud services.

<img src="images/maintf.png" width="700">

Next, I initialized the Terraform working directory to download the required provider plugins and prepare the environment for infrastructure deployment.

```bash id="tfinit"
terraform init
```

<img src="images/terraform-init.png" width="700">

After initialization, I executed a Terraform plan to preview the infrastructure resources that would be created.

```bash id="tfplan"
terraform plan
```

<img src="images/terraform-plan.png" width="700">

Once the configuration was verified, I applied the Terraform configuration to provision the infrastructure in Google Cloud.

```bash id="tfapply"
terraform apply
```

<img src="images/terraform-apply.png" width="700">

Through this process, I automatically created the following infrastructure components:

* A **Google Cloud Storage (GCS) bucket** to serve as the **Data Lake layer** for storing raw repository data.
* A **BigQuery dataset** to act as the **Data Warehouse layer** for storing structured and transformed analytical tables.

<img src="images/ai-open-source-dw.png" width="700">
<img src="images/ai-open-source-lake.png" width="700">

By using Terraform, the infrastructure setup becomes **fully reproducible and version-controlled**, ensuring that the entire cloud environment can be recreated consistently across different environments.

### Step 3 — Data Exploration in BigQuery

In this step, I explored the **GitHub Repositories public dataset** available in BigQuery in order to understand its structure and identify the relevant tables required for the analysis.

The dataset used in this project is:

```
bigquery-public-data.github_repos
```

I examined several key tables including:

* `languages`
* `commits`
* `contents`

The **languages** table was used to analyze the distribution of programming languages across repositories, while the **commits** table provided insights into repository activity over time.

<img src="images/languages.png" width="700">
<img src="images/languages1.png" width="700">
<img src="images/languages2.png" width="700">
<img src="images/languages3.png" width="700">
<img src="images/languages4.png" width="700">

The **contents** table was particularly important for identifying repositories related to Artificial Intelligence. By searching for keywords such as *machine learning*, *deep learning*, *LLM*, and *artificial intelligence*, I was able to detect repositories associated with AI development.

This exploration step helped define the filtering logic used later in the data pipeline to extract AI-related repositories for further analysis.

## Step 3 — Exploring the GitHub Public Dataset

In this step, I explored the **GitHub Repositories Public Dataset** available in BigQuery in order to better understand its structure and identify the tables that would be used in the data pipeline.

The dataset used in this project is:

```
bigquery-public-data.github_repos
```

Before building the transformation pipeline, I performed several exploratory queries to understand the schema and the relationships between tables.

The following tables were analyzed:

* `languages`
* `commits`
* `contents`
* `files`

These tables contain valuable information about **repository metadata, programming languages, source files, and development activity across millions of open-source projects**.

This exploration phase helped me determine how to **identify Artificial Intelligence related repositories** and how to structure the transformation logic that will later populate the data warehouse.

---

## Step 4 — Identifying AI-Related Repositories

In this step, I focused on identifying repositories related to **Artificial Intelligence technologies** in order to narrow the scope of the analysis.

Since the GitHub public dataset contains millions of repositories across many domains, it was necessary to apply a filtering strategy to isolate projects specifically associated with AI development.

To achieve this, I analyzed the repository file paths stored in the **`files`** table and searched for keywords commonly associated with AI-related technologies. The filtering logic was implemented using regular expressions to improve accuracy and reduce false positives.

The following keyword categories were used to detect AI-related repositories:

* **Machine Learning**
* **Deep Learning**
* **Large Language Models (LLMs)**
* **Artificial Intelligence**

The filtering process also limited results to source code file types commonly used in data science and machine learning projects, such as Python and Jupyter Notebook files.


## Programming Language Distribution Across GitHub

To understand which programming languages are most commonly used across repositories, I queried the **languages** table.

Because the `language` field is stored as a **repeated record**, the query uses `UNNEST()` to extract each language entry.

```sql
SELECT
  lang.name AS language,
  COUNT(DISTINCT repo_name) AS repo_count
FROM
  `bigquery-public-data.github_repos.languages`,
  UNNEST(language) AS lang
GROUP BY language
ORDER BY repo_count DESC
LIMIT 20;
```

This query reveals the most frequently used programming languages across GitHub repositories.

**Query Result – Top Programming Languages**

<img src="images/language_repo_count.png" width="700">

## Detecting AI-related Repositories

To identify repositories related to Artificial Intelligence, I analyzed the **files** table and searched for AI-related keywords within file paths.

```sql
SELECT
DISTINCT
  repo_name,
  path,
  case 
when REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b') then 'ML'
when REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b') then 'DL'
when REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b') then 'AI'
when REGEXP_CONTAINS(LOWER(path), r'\bllm\b') then 'LLM'
else 'None' end AS Subject
FROM `bigquery-public-data.github_repos.files`
WHERE
REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bllm\b')
OR REGEXP_CONTAINS(LOWER(path), r'\.(py|ipynb|r|jl)$')
LIMIT 100;
```
**Query Result – AI Repo List : **

<img src="images/ai_repo_list.png" width="700">

Regular expressions were used instead of simple string matching to reduce false positives and ensure more accurate keyword detection.

```sql
WITH ai_repos AS (
SELECT
DISTINCT
  repo_name,
  path,
  case 
when REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b') then 'ML'
when REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b') then 'DL'
when REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b') then 'AI'
when REGEXP_CONTAINS(LOWER(path), r'\bllm\b') then 'LLM'
else 'None' end AS Subject
FROM `bigquery-public-data.github_repos.files`
WHERE
REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bllm\b')
OR REGEXP_CONTAINS(LOWER(path), r'\.(py|ipynb|r|jl)$')
LIMIT 100
)

SELECT
lang.name AS language,
COUNT(DISTINCT l.repo_name) repo_count
FROM
`bigquery-public-data.github_repos.languages` l,
UNNEST(language) AS lang
JOIN ai_repos a
ON l.repo_name = a.repo_name
GROUP BY language
ORDER BY repo_count DESC
LIMIT 20;
```

This query counts the number of repositories that contain AI-related keywords within their source files.

**Query Result – Total AI Repositories Count**

<img src="images/language_repo_count.png" width="700">


---

## Programming Languages Used in AI Repositories

After identifying AI-related repositories, I analyzed which programming languages are most commonly used in those projects.

```sql
WITH ai_repos AS (
SELECT
DISTINCT
  repo_name,
  path,
  case 
when REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b') then 'ML'
when REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b') then 'DL'
when REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b') then 'AI'
when REGEXP_CONTAINS(LOWER(path), r'\bllm\b') then 'LLM'
else 'None' end AS Subject
FROM `bigquery-public-data.github_repos.files`
WHERE
REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bllm\b')
OR REGEXP_CONTAINS(LOWER(path), r'\.(py|ipynb|r|jl)$')
LIMIT 100
)

SELECT
lang.name AS language, 
a.Subject,
COUNT(DISTINCT l.repo_name) repo_count
FROM
`bigquery-public-data.github_repos.languages` l,
UNNEST(language) AS lang
JOIN ai_repos a
ON l.repo_name = a.repo_name
GROUP BY language ,a.Subject
ORDER BY repo_count DESC
LIMIT 20;
```

This analysis reveals which programming languages dominate the **Artificial Intelligence open-source ecosystem**.
 **Query Result – Languages Used in AI Repositories**

<img src="images/language_ai_repo_count.png" width="700">
---

Through this exploration process, I was able to:

* Understand the schema of the GitHub public dataset
* Identify the most relevant tables for the analysis
* Define a filtering strategy for detecting AI-related repositories
* Prepare the transformation logic used later in the data pipeline

  ## Step 5 — Data Lake Layer (GCS)

In this step, I exported the filtered AI repository dataset from BigQuery to **Google Cloud Storage (GCS)** to establish the Data Lake layer of the pipeline.

After identifying AI-related repositories, the resulting dataset was stored in the data warehouse as the table:

`ai_open_source_dw.ai_repositories`

```sql
CREATE OR REPLACE TABLE
`braided-keel-490209-q8.ai_open_source_dw.ai_repositories` AS

SELECT
DISTINCT
  repo_name,
  case 
when REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b') then 'ML'
when REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b') then 'DL'
when REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b') then 'AI'
when REGEXP_CONTAINS(LOWER(path), r'\bllm\b') then 'LLM'
when REGEXP_CONTAINS(LOWER(path), r'\.(py|ipynb|r|jl)$') then 'AI'
else 'None' end AS Subject
FROM `bigquery-public-data.github_repos.files`
WHERE
REGEXP_CONTAINS(LOWER(path), r'\bmachine[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bdeep[-_ ]?learning\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bartificial[-_ ]?intelligence\b')
OR REGEXP_CONTAINS(LOWER(path), r'\bllm\b')
OR REGEXP_CONTAINS(LOWER(path), r'\.(py|ipynb|r|jl)$');
```
To enable scalable storage and downstream processing, this table was exported to a **GCS bucket** in **Parquet format**, which provides efficient columnar storage and is well-suited for analytical workloads.

The export was performed directly from the BigQuery interface using the **Export to GCS** functionality.

Export configuration:

* Destination bucket: `ai-open-source-lake`
* File format: **Parquet**
* Compression: **Snappy**

📸 **BigQuery Table Export**

<img src="images/export_to_gcs.png" width="700">

The resulting file was stored in the data lake under the following path:

```
gs://ai-open-source-lake/ai_repositories/ai_repositories.parquet
```

<img src="images/gcs_ai_repository_parquet.png" width="700">

---

** Step 6 — Data Transformation Pipeline with dbt**

After loading the filtered AI repository dataset into **BigQuery**, I implemented a transformation layer using **dbt (Data Build Tool)** to build a modular analytics pipeline.

The goal of this step was to transform the raw repository data into structured analytical tables that can be used for exploration and downstream analytics.

dbt allows defining transformation logic as modular SQL models with version control and dependency management.

---

#  Transformation Pipeline

The dbt pipeline performs the following transformations:

### 1 Read Raw Repository Data

The raw AI repository dataset is stored in **BigQuery** after the ingestion pipeline.

dbt reads the raw table and prepares it for transformation.

---

### 2 Staging Layer

A staging model was created to standardize the repository dataset.

Model:

```
stg_ai_repositories
```

Purpose:

* Normalize raw repository fields
* Prepare clean data for analytics models
* Create a consistent staging layer

---

### 3 Analytics Layer

An analytics model aggregates repositories by programming language.

Model:

```
ai_repo_languages
```

This model produces an analytical table that shows the distribution of AI repositories by programming language.

---

#  Resulting BigQuery Tables

After running dbt, the following tables are created in the data warehouse:

```
braided-keel-490209-q8
   └── ai_open_source_dw
        ├── stg_ai_repositories
        └── ai_repo_languages
```

Pipeline flow:

```
Raw Data → Staging Model → Analytics Model
```

---

# Why dbt?

Using **dbt** provides several advantages:

* Version-controlled SQL transformations
* Modular data models
* Dependency-aware pipelines
* Reproducible analytics workflows

This transformation layer turns the raw repository dataset into **structured analytics-ready tables inside BigQuery**.

---

# Running the dbt Pipeline

The dbt models are executed using:

```bash
dbt debug
dbt run
```

`dbt debug` verifies the connection to BigQuery.

`dbt run` executes the transformation models and materializes them as tables inside the warehouse.

---

# 🖼 dbt Execution Screenshots

### dbt Debug Result

<img src="images/dbt-debug.png" width="700">

---

### dbt Run Result

<img src="images/dbt-run.png" width="700">
---

#  Final Project Structure

Here is the final structure of the project after implementing the dbt transformation layer:

```
ai-open-source-intelligence-platform
│
├── terraform
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ingestion
│   └── extract_ai_repositories.py
│
├── dbt
│   ├── dbt_project.yml
│   ├── models
│   │
│   │   ├── staging
│   │   │   └── stg_ai_repositories.sql
│   │   │
│   │   └── marts
│   │       └── ai_repo_languages.sql
│
├── images
│   ├── dbt_debug.png
│   └── dbt_run.png
│
└── README.md
```

---

#  Final Data Architecture

The complete data pipeline now looks like this:

```
GitHub AI Repositories
        │
        ▼
Python Extraction
        │
        ▼
Google Cloud Storage (Raw Data)
        │
        ▼
BigQuery Data Warehouse
        │
        ▼
dbt Transformation Layer
        │
        ▼
Analytics Tables
```

---

# Outcome

This step successfully introduced an **Analytics Engineering layer** into the project using dbt.

The raw AI repository dataset is now transformed into structured analytical tables that enable exploration of the AI ecosystem by programming language.

