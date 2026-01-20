terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
# Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  credentials = file("awesome-icon-484918-n5-6e0f8d98aacb.json")
  project = "awesome-icon-484918-n5"
  region  = "us-central1"
}



resource "google_storage_bucket" "data-lake-bucket" {
  name          = "esila-de-zoomcamp-bucket-2026"
  location      = "US"

  # Optional, but recommended settings:
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  // days
    }
  }

  force_destroy = true
}


resource "google_bigquery_dataset" "dataset" {
  dataset_id = "trips_data_all"
  project    = "awesome-icon-484918-n5"
  location   = "US"
}