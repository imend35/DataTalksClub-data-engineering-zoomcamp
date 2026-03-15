output "gcs_bucket_name" {
  value = google_storage_bucket.data_lake.name
}

output "raw_dataset_id" {
  value = google_bigquery_dataset.raw_dataset.dataset_id
}

output "dw_dataset_id" {
  value = google_bigquery_dataset.dw_dataset.dataset_id
}