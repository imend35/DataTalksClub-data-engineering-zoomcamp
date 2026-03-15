variable "project_id" {
  description = "braided-keel-490209-q8"
  type        = string
}

variable "region" {
  description = "GCP region"
  default     = "US"
}

variable "gcs_bucket_name" {
  description = "ai-open-source-lake"
  type        = string
}

variable "raw_dataset" {
  description = "BigQuery raw dataset"
  default     = "ai_open_source_raw"
}

variable "dw_dataset" {
  description = "BigQuery analytics dataset"
  default     = "ai_open_source_dw"
}