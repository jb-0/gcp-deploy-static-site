# GCS Static site continuous deployment
To achieve continuous deployment for static sites hosted in Google Cloud Storage Buckets, I developed this Cloud 
Function in Python. The Google Cloud Function is triggered via a GitHub webhook and is authorised against a secret 
stored in Google Secrets management.
 
This script can also be easily adapted to be run locally, using a Service Account. Refer early commit history for detail
on local configuration.


## Getting Started
The steps below outline how you can use this script in your GCP environment:
1. 