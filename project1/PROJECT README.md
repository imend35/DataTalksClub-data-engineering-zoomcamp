# Global AI Open-Source Intelligence Platform : A Global Data Engineering Pipeline

### Mapping the Evolution of Artificial Intelligence Across the World

**Author:**
Esila Nur Demirci



## Problem Statement

The open-source ecosystem has become one of the most important drivers of innovation in Artificial Intelligence. Thousands of developers around the world contribute to repositories related to Machine Learning, Deep Learning, Large Language Models (LLMs), and Artificial Intelligence. However, it is difficult to understand how this ecosystem evolves globally and which regions and technologies are leading the development of AI.

This project aims to analyze the global landscape of open-source AI development using large-scale GitHub repository data. By leveraging public datasets available in BigQuery, the project explores trends in AI-related repositories and investigates which AI domains are growing the fastest, which programming languages are most commonly used in AI projects, and how development activity is distributed across countries and continents.

Through an end-to-end data engineering pipeline, the project collects, processes, and transforms GitHub repository data to build an analytical dataset that supports interactive visualization and exploration.

The final outcome is a dashboard that provides insights into:

* The distribution of AI-related repositories across different domains (Machine Learning, Deep Learning, LLMs, and Artificial Intelligence)
* The geographic distribution of AI development by country and continent
* The programming languages most frequently used in AI projects
* The evolution of AI-related repositories over time

By transforming large-scale open-source data into meaningful insights, this project aims to provide a clearer view of how the global AI ecosystem is evolving and which technologies and regions are driving innovation.

## Architecture

This project builds an end-to-end data engineering pipeline to analyze the global open-source Artificial Intelligence ecosystem using large-scale GitHub repository data.

```mermaid
flowchart LR

A[BigQuery Public Dataset<br>GitHub Repositories] --> B[Airflow Orchestration]

B --> C[Data Extraction]

C --> D[GCS Data Lake<br>Raw AI Repository Data]

D --> E[BigQuery Data Warehouse<br>Raw Tables]

E --> F[dbt Transformations]

F --> G[Analytics Tables<br>AI Insights Dataset]

G --> H[Power BI Dashboard]

H --> I[Global AI Ecosystem Insights]

```

### Pipeline Stages

**1. Data Source**

The project uses the public GitHub repositories dataset available in BigQuery.
This dataset contains information about repositories, commits, files, and programming languages across millions of open-source projects.

**2. Orchestration**

Apache Airflow orchestrates the pipeline and schedules the extraction and transformation tasks.

**3. Data Lake**

Filtered raw data is stored in Google Cloud Storage (GCS) to create a data lake layer.

**4. Data Warehouse**

Cleaned and structured datasets are loaded into BigQuery for analytical processing.

**5. Data Transformation**

dbt is used to transform raw repository data into analytics-ready tables, focusing on AI-related repositories and programming language usage.

**6. Visualization**

Power BI connects to the analytics tables and provides interactive dashboards that reveal trends in global AI development.

## Data Pipeline Explanation

This project implements an end-to-end data engineering pipeline designed to analyze the global evolution of Artificial Intelligence development within the open-source ecosystem. The pipeline extracts large-scale repository data from GitHub public datasets, processes it through multiple data layers, and delivers analytical insights through an interactive dashboard.

### 1. Data Source

The pipeline uses the **GitHub Repositories Public Dataset** available in BigQuery.
This dataset contains extensive information about open-source repositories, including commits, files, repository metadata, and programming languages.

The dataset serves as the primary source for identifying repositories related to Artificial Intelligence, Machine Learning, Deep Learning, and Large Language Models (LLMs).

---

### 2. Workflow Orchestration

The workflow is orchestrated using **Apache Airflow**, which manages the scheduling and execution of the pipeline tasks.

Airflow DAGs are responsible for:

* Extracting relevant GitHub repository data
* Filtering repositories related to AI domains
* Triggering data loading and transformation processes

This ensures the pipeline can be executed in a repeatable and automated manner.

---

### 3. Data Ingestion and Data Lake Layer

During the ingestion stage, relevant subsets of GitHub repository data are extracted and stored in **Google Cloud Storage (GCS)**.

This step creates a **data lake layer**, where raw filtered data is stored before further processing.

The purpose of the data lake is to:

* Preserve raw extracted data
* Enable reproducibility
* Support scalable data processing

---

### 4. Data Warehouse Layer

After ingestion, the data is loaded into **BigQuery**, which acts as the central data warehouse for analytical queries.

At this stage:

* Raw repository data is structured into tables
* Data is optimized for analytical queries
* Large-scale queries can be executed efficiently

---

### 5. Data Transformation

Data transformation is performed using **dbt (Data Build Tool)**.

The transformation layer focuses on:

* Identifying AI-related repositories using keyword filtering
* Aggregating repository statistics
* Preparing analytics-ready tables

These tables are designed specifically for analytical queries and dashboard visualizations.

---

### 6. Analytics Layer

The transformed datasets create an **AI ecosystem analytics layer** that provides insights into:

* The distribution of AI repositories across different domains
* The geographic distribution of developers
* The most commonly used programming languages in AI projects
* The growth of AI-related repositories over time

---

### 7. Visualization

The final step of the pipeline connects the analytics tables to **Power BI**, where interactive dashboards are created.

The dashboard allows users to explore:

* AI repository growth trends
* AI development activity by country and continent
* Programming language distribution in AI projects
* Category distribution across Machine Learning, Deep Learning, LLMs, and AI

This visualization layer transforms large-scale open-source data into meaningful and accessible insights.

## Tech Stack

This project leverages a modern data engineering stack to build a scalable end-to-end pipeline for analyzing the global open-source Artificial Intelligence ecosystem.

### Cloud Platform

**Google Cloud Platform (GCP)**
The project is deployed on GCP, providing scalable infrastructure and managed services for data processing and storage.

---

### Infrastructure as Code

**Terraform**
Terraform is used to provision and manage cloud infrastructure resources such as storage buckets and data warehouse components in a reproducible and automated way.

---

### Workflow Orchestration

**Apache Airflow**
Airflow orchestrates the data pipeline through Directed Acyclic Graphs (DAGs). It schedules and manages the extraction, loading, and transformation processes of the pipeline.

---

### Data Lake

**Google Cloud Storage (GCS)**
GCS serves as the data lake layer where raw extracted data from the GitHub dataset is stored before being processed and loaded into the data warehouse.

---

### Data Warehouse

**BigQuery**
BigQuery acts as the analytical data warehouse for this project. It enables fast querying and processing of large-scale GitHub repository datasets.

---

### Data Transformation

**dbt (Data Build Tool)**
dbt is used to transform raw repository data into analytics-ready datasets by creating structured models and applying SQL-based transformations.

---

### Programming Language

**Python**
Python is used for data extraction scripts and pipeline development, particularly within Airflow tasks.

---

### Data Visualization

**Power BI**
Power BI is used to build interactive dashboards that visualize trends in global AI development, including repository growth, programming language usage, and geographic distribution of AI projects.

---

### Data Source

**GitHub Public Dataset (BigQuery)**
The project uses the publicly available GitHub repositories dataset hosted in BigQuery, which contains large-scale open-source development data including commits, files, and programming languages.

## Dataset

### GitHub Repositories Public Dataset

This project uses the **GitHub Repositories Public Dataset** available on Google BigQuery. The dataset contains large-scale information about open-source repositories hosted on GitHub, including repository metadata, commits, files, and programming languages.

The dataset is maintained as part of the BigQuery Public Datasets program and provides access to millions of open-source projects, enabling large-scale analysis of software development trends.

### Dataset Source

The dataset is available directly in BigQuery:

```
bigquery-public-data.github_repos
```

This public dataset allows querying repository information without the need to download or store the full dataset locally.

### Key Tables Used

The following tables are primarily used in this project:

| Table       | Description                                             |
| ----------- | ------------------------------------------------------- |
| `languages` | Contains programming languages used in repositories     |
| `commits`   | Provides commit history information for repositories    |
| `contents`  | Includes file content and metadata for repository files |
| `files`     | Contains file-level metadata                            |
| `licenses`  | Provides license information for repositories           |

For development and testing purposes, smaller sample tables are also used:

| Sample Tables     |
| ----------------- |
| `sample_repos`    |
| `sample_commits`  |
| `sample_contents` |
| `sample_files`    |

### Dataset Size

The GitHub repositories dataset is extremely large, containing data across millions of repositories and billions of files and commits. This makes it well suited for large-scale analytics and data engineering pipelines.

### Relevance to the Project

This dataset enables the identification and analysis of repositories related to:

* Machine Learning
* Deep Learning
* Large Language Models (LLMs)
* Artificial Intelligence

By filtering repository metadata and content for AI-related keywords, the dataset can be transformed into an analytical dataset that reveals global trends in AI development.

The resulting dataset supports the creation of insights such as:

* Growth of AI-related repositories over time
* Geographic distribution of AI development
* Programming languages most frequently used in AI projects
* Distribution of AI domains across different regions

## Power BI Dashboard

The final stage of this project is an interactive **Power BI dashboard** designed to visualize and explore the global evolution of Artificial Intelligence development within the open-source ecosystem.

The dashboard connects directly to the analytics tables generated in **BigQuery**, enabling efficient exploration of large-scale repository data and providing meaningful insights into AI-related open-source activity.

### Dashboard Objectives

The dashboard aims to answer the following key questions:

* Which AI domains are growing the fastest?
* Which countries and continents contribute the most to AI development?
* Which programming languages are most commonly used in AI-related repositories?
* How has the number of AI repositories evolved over time?

---

### Key Visualizations

#### 1. AI Repository Distribution by Category

This visualization shows the distribution of repositories across major AI domains, including:

* Machine Learning
* Deep Learning
* Large Language Models (LLMs)
* Artificial Intelligence

This chart helps identify which AI areas dominate open-source development.

---

#### 2. AI Repository Growth Over Time

A temporal line chart that illustrates how AI-related repositories have increased over time.

This visualization highlights the rapid expansion of AI development within the open-source ecosystem.

---

#### 3. Programming Languages Used in AI Projects

This chart displays the most commonly used programming languages across AI repositories.

Typical trends observed include strong dominance of languages such as:

* Python
* C++
* JavaScript
* Rust
* Go

---

#### 4. Global Distribution of AI Development

A geographic visualization that displays AI repository distribution by:

* Country
* Continent

This chart reveals which regions of the world contribute most actively to open-source AI innovation.

---

### Insights Generated

By combining repository metadata, programming language data, and geographic information, the dashboard provides insights into:

* The global growth of Artificial Intelligence development
* Technology stacks used in AI projects
* Regional patterns in open-source innovation
* Emerging AI domains gaining traction

This dashboard transforms large-scale GitHub repository data into an accessible and interactive platform for understanding the evolution of the global AI ecosystem.

## Project Structure

The project is organized into multiple layers representing the stages of a modern data engineering pipeline.

```
ai-open-source-intelligence-platform/
│
├── airflow/
│   ├── dags/
│   │   └── github_ai_pipeline.py
│   └── requirements.txt
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_github_repos.sql
│   │   ├── marts/
│   │   │   ├── ai_repo_growth.sql
│   │   │   ├── ai_repo_languages.sql
│   │   │   └── ai_repo_geography.sql
│   │   └── schema.yml
│   └── dbt_project.yml
│
├── ingestion/
│   └── extract_github_data.py
│
├── dashboards/
│   └── powerbi_dashboard.pbix
│
├── data/
│   └── sample_queries.sql
│
├── docs/
│   └── architecture_diagram.png
│
├── requirements.txt
└── README.md
```

### Folder Overview

**airflow/**
Contains the Airflow DAG responsible for orchestrating the pipeline tasks including extraction, loading, and triggering transformations.

**terraform/**
Includes Infrastructure as Code (IaC) configuration files used to provision cloud resources such as storage buckets and BigQuery datasets.

**dbt/**
Contains data transformation logic implemented using dbt.
Models are organized into staging and mart layers to prepare analytics-ready datasets.

**ingestion/**
Includes Python scripts used to extract and filter GitHub repository data from the BigQuery public dataset.

**dashboards/**
Contains the Power BI dashboard file used for data visualization and exploration.

**data/**
Contains example queries and intermediate SQL scripts used during development.

**docs/**
Includes architecture diagrams and documentation assets used in the project README.


## How to Run the Project

Follow the steps below to reproduce the full data engineering pipeline and generate the AI ecosystem analytics dashboard.

### 1. Prerequisites

Make sure the following tools are installed on your system:

* Python 3.9+
* Docker & Docker Compose
* Terraform
* Google Cloud SDK
* dbt
* Apache Airflow

You also need a **Google Cloud Platform (GCP)** account with access to:

* BigQuery
* Google Cloud Storage

---

### 2. Clone the Repository

```id="m0vhrj"
git clone https://github.com/<your-username>/ai-open-source-intelligence-platform.git
cd ai-open-source-intelligence-platform
```

---

### 3. Configure Google Cloud

Authenticate your Google Cloud account:

```id="bvr0gx"
gcloud auth application-default login
```

Set your project ID:

```id="1h70mc"
gcloud config set project <your-project-id>
```

---

### 4. Provision Infrastructure

Use Terraform to provision the required cloud resources:

```id="31qhii"
cd terraform
terraform init
terraform apply
```

This step creates:

* Google Cloud Storage bucket (Data Lake)
* BigQuery datasets (Data Warehouse)

---

### 5. Start Airflow

Run Airflow using Docker:

```id="dttxj4"
docker-compose up
```

Once started, open the Airflow UI:

```id="g74d0o"
http://localhost:8080
```

Activate the DAG:

```id="a8r3y6"
github_ai_pipeline
```

This pipeline will:

* Extract GitHub repository data
* Filter AI-related repositories
* Store raw data in GCS
* Load data into BigQuery

---

### 6. Run dbt Transformations

Navigate to the dbt directory:

```id="htw86a"
cd dbt
dbt run
```

This step transforms raw repository data into analytics-ready tables.

---

### 7. Launch the Dashboard

Open the Power BI dashboard file:

```id="q8h1ga"
dashboards/powerbi_dashboard.pbix
```

Connect Power BI to the BigQuery analytics tables to visualize the results.

---

### 8. Explore the Dashboard

The dashboard provides insights into:

* AI repository growth over time
* Distribution of AI domains
* Programming languages used in AI projects
* Geographic distribution of AI development

## Key Insights

The analysis of the global open-source AI ecosystem reveals several important patterns and trends in how artificial intelligence technologies are evolving across the world.

### Rapid Growth of AI Development

The number of repositories related to Artificial Intelligence, Machine Learning, and Deep Learning has increased significantly over time.
This trend reflects the rapid expansion of AI research and development within the open-source community.

Large Language Models (LLMs) have emerged as one of the fastest growing areas in recent years, indicating a strong shift toward generative AI technologies.

---

### Dominance of Python in AI Projects

The analysis shows that **Python is the dominant programming language** used in AI-related repositories.

Other languages such as **C++, JavaScript, Rust, and Go** also appear in AI projects, but Python remains the most widely used due to its rich ecosystem of AI frameworks and libraries.

---

### Geographic Concentration of AI Development

AI development activity is not evenly distributed across the globe.

A large portion of open-source AI repositories originates from countries with strong technology ecosystems such as:

* United States
* China
* India
* Germany
* United Kingdom

These regions contribute significantly to global AI innovation.

---

### Global Expansion of AI Innovation

Although historically concentrated in a few regions, AI development is increasingly becoming a **global phenomenon**.

Emerging tech communities in Asia, Europe, and South America are contributing more actively to open-source AI projects.

---

### Diversity of AI Domains

The analysis also highlights the diversity of AI domains within the open-source ecosystem, including:

* Machine Learning
* Deep Learning
* Natural Language Processing
* Large Language Models (LLMs)

These domains reflect the wide range of applications and research areas currently shaping the future of Artificial Intelligence.

---

Overall, the insights generated by this project demonstrate how open-source data can be used to understand the global evolution of Artificial Intelligence and identify the technologies and regions driving innovation.

## Future Improvements

While this project provides a complete end-to-end data engineering pipeline for analyzing the global AI open-source ecosystem, several enhancements could further improve the scalability, automation, and analytical capabilities of the platform.

### Real-Time Data Processing

Currently, the pipeline processes GitHub repository data in batch mode.
A potential improvement would be to implement **streaming data ingestion** using technologies such as Kafka or Pub/Sub to capture real-time repository activity and developer contributions.

---

### Automated Geographic Enrichment

The current analysis focuses on repository metadata available in the public dataset.
Future iterations could integrate additional data sources such as the GitHub API to enrich repository owners with location data, enabling more accurate country and continent-level analysis.

---

### Advanced AI Topic Classification

At the moment, AI repositories are identified using keyword-based filtering.
This approach could be enhanced by applying **Natural Language Processing (NLP)** techniques or machine learning models to classify repositories into AI categories more accurately.

---

### Expanded Dashboard Analytics

The Power BI dashboard could be extended with additional analytical views such as:

* Developer contribution networks
* AI framework usage trends
* Collaboration patterns between countries
* Organization-level AI innovation metrics

These insights would provide a deeper understanding of the global AI ecosystem.

---

### CI/CD and Automated Deployment

To further improve reproducibility and reliability, the project could include a **CI/CD pipeline** using tools such as GitHub Actions or GitLab CI.
This would allow automated testing, infrastructure deployment, and pipeline validation.

---

### Scalability Enhancements

Future improvements could also include optimizing BigQuery tables through **partitioning and clustering**, enabling faster analytical queries and reducing processing costs.

---

By implementing these improvements, the platform could evolve into a more advanced analytics system capable of monitoring the global AI ecosystem in near real-time and supporting deeper insights into the evolution of artificial intelligence technologies.

# Project Solution:

## STEP 1 — Create GCP Project and Enable Services

### Google Cloud Environment Setup

The first step of the project involved setting up the cloud environment on Google Cloud Platform (GCP).

A dedicated GCP project was created to host all infrastructure components required for the data pipeline. 

The following services were enabled:

* BigQuery for data warehousing and analytics
* Google Cloud Storage for the data lake layer
* IAM for access management

A service account with the necessary permissions was created to allow the pipeline components to securely interact with GCP services.

### STEP 2 — Infrastructure Provisioning with Terraform

To ensure reproducibility and infrastructure consistency, the cloud resources required for the project were provisioned using Terraform.

Terraform was used to automatically create the following resources:

 * A Google Cloud Storage bucket to serve as the data lake layer

 * BigQuery datasets to store raw and transformed analytical tables

Using Infrastructure as Code (IaC) allows the entire environment to be recreated easily and ensures that the pipeline can be deployed consistently across environments.

### STEP 3 — Data Exploration in BigQuery - Exploring the GitHub Public Dataset

The project uses the GitHub repositories public dataset available in BigQuery.

Before building the pipeline, exploratory queries were performed to better understand the structure of the dataset and identify relevant tables. The following tables were explored:

 * languages
 * commits
 * contents
 * files

These tables contain valuable information about repository metadata, programming languages, and development activity across millions of open-source projects.

This exploration step helped define the filtering strategy used to identify repositories related to Artificial Intelligence.

### STEP 4 — AI Repository Detection - Identifying AI-Related Repositories

To focus the analysis on Artificial Intelligence development, repositories related to AI domains were identified using keyword-based filtering.

Repository metadata and file contents were scanned for keywords related to:

 * Machine Learning
 * Deep Learning
 * Large Language Models (LLMs)
 * Artificial Intelligence

This filtering step allowed the creation of a subset of repositories specifically related to AI technologies.

### STEP 5 — Data Lake Layer (GCS) - Creating the Data Lake Layer 

Filtered repository data was exported from BigQuery and stored in Google Cloud Storage (GCS).

This step creates a data lake layer where raw data is preserved before transformation. The data is stored in columnar formats such as Parquet to improve storage efficiency and query performance.

The data lake layer ensures that raw extracted data remains available for future reprocessing and auditing.

### STEP 6 — Airflow Pipeline - Workflow Orchestration with Airflow

Apache Airflow was used to orchestrate the pipeline workflow.

A Directed Acyclic Graph (DAG) was created to automate the following tasks:

1 - Extract repository data from the BigQuery public dataset
2 - Filter AI-related repositories
3 - Export raw data to Google Cloud Storage
4 - Load data into BigQuery warehouse tables
5 - Trigger data transformation using dbt

This orchestration ensures the pipeline runs in a structured and repeatable manner.

### STEP 7 — Data Transformation with dbt 

Data transformations were implemented using dbt (Data Build Tool).

The raw repository data was transformed into analytics-ready tables designed specifically for visualization and analysis. These transformations included:

* Aggregating repository counts by AI category
* Calculating repository growth over time
* Identifying the most commonly used programming languages in AI projects
* Preparing geographic distribution datasets

The resulting tables serve as the foundation for the analytical dashboard.

### STEP 8 — Power BI Dashboard - Data Visualization with Power BI

The final stage of the project involved building an interactive dashboard using Power BI.

The dashboard connects directly to the analytical tables stored in BigQuery and provides visual insights into the global open-source AI ecosystem.

Key visualizations include:

  * Growth of AI repositories over time
  * Distribution of AI domains
  * Programming languages used in AI projects
  * Geographic distribution of AI development
