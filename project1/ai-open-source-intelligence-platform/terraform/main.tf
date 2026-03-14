terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project = "braided-keel-490209-q8"
  region  = "us-central1"
}

# GCS Data Lake Bucket
resource "google_storage_bucket" "data_lake" {
  name     = "ai-open-source-lake"
  location = "US"

  uniform_bucket_level_access = true
}

# BigQuery Dataset
resource "google_bigquery_dataset" "data_warehouse" {
  dataset_id = "ai_open_source_dw"
  location   = "US"
}
