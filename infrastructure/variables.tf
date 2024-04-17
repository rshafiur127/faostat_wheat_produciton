variable "project" {
  description = "Project ID"
  default = "dtc-de-411905"
}

variable "region" {
  description = "Region ID"
  default = "us-central1"
}

variable "location" {
  description = "Location Name"
  default = "US"
}

variable "storage_bucket_name" {
  description = "GCP Bucket Name"
  default = "dtc-de-411905-project"
}

variable "bigquery_id" {
  description = "Bigquery dataset ID"
  default = "project"
}
