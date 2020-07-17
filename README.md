# GCS Static site continuous deployment
To achieve continuous deployment for static sites hosted in Google Cloud Storage Buckets, I developed this Cloud 
Function in Python. The Google Cloud Function is triggered via a GitHub webhook and is authorised against a secret 
stored in Google Secrets management.
 
This script can also be easily adapted to be run locally, using a Service Account. Refer early commit history for detail
on local configuration.


## Getting Started
The steps below outline how you can use this script in your GCP environment, with execution being triggered

**GCP GUI (https://console.cloud.google.com/):**
1. Generate your secret and store it in Google Secrets Management, take note of the secret's path.
2. Create a new cloud function in the same project as your static site bucket
3. There are a number of configuration settings that you will customise as necessary, however the following configuration
steps are required to ensure this code operates as intended:
    * Select trigger as "HTTP"
    * Tick "Allow unauthenticated invocations" 
    * Select "Inline Editor" with runtime "Python 3.7+"
    * Copy the code from "main.py" and "requirements.txt" into the corresponding textboxes
    * Select a service account with permissions to write to storage and read the relevant secret
    * Set the required Environment Variables -
        i. SECRET_PATH: The path noted in step 1
        ii. BUCKET_NAME: The name of your storage bucket
        ii. GIT_REPO: The clone path of the repo you want to copy to your storage bucket
        
4. Deploy the cloud function and take note of the URL

**GitHub GUI (https://github.com/)**
1. While in the repo you assigned to GIT_REPO earlier click "Setting" > "Webhooks"
2. Copy the URL you noted in step 5 above into "Payload URL"
3. Select "application/json" as "Content type"
4. Copy your secret into "Secret"
5. Select "Just the push event" for "Which events would you like to trigger this webhook?"
6. Click "Add webhook"
  
This concludes the setup, when you push to this repo your site will be automatically deployed.

  
## Improvements
Potential improvements that could be made to this code can be seen below:
- Any push event to the repository (regardless of whether it is the master branch) will trigger the cloud function, the function should check which branch triggered the webhook and only deploy if the branch is the master 
- Currently all files (other than those explicitly excluded) are copied from GitHub, regardless of whether they are
- The getting started section above should include a gcloud CLI deployment approach
