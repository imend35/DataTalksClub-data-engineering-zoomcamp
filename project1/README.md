
### Step 1 — Google Cloud Environment Setup

In the first step of the project, I set up the cloud environment on **Google Cloud Platform (GCP)** to support the data engineering pipeline.

I created a dedicated GCP project to host all infrastructure components required for the pipeline. Within this project, I enabled the core services needed for data storage, processing, and access management.

The following services were activated:

* **BigQuery**, which serves as the data warehouse for analytical queries and large-scale data processing
* **Google Cloud Storage (GCS)**, which acts as the data lake layer for storing raw and intermediate data
* **Identity and Access Management (IAM)**, which is used to securely manage permissions and access control across the project

To allow the pipeline components to securely interact with Google Cloud services, I created a **service account** and assigned the necessary roles, including BigQuery and Cloud Storage administrative permissions.

This initial setup established the cloud foundation required for building and running the end-to-end data pipeline.

           
