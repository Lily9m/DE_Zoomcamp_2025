provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_storage_bucket" "data_lake_bucket" {
  name     = "my-data-lake-bucket"
  location = "US"
}

resource "google_bigquery_dataset" "taxi_dataset" {
  dataset_id = "ny_taxi_data"
  location   = "US"
}