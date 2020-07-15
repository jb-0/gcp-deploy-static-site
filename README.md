# Git Repo to GCP storage bucket

This simple script clones a git repo into a local temp folder. The script walks through this temp folder and writes the files to a storage bucket.

To use this script run the main.py file, you will need to include appropriate configuration for your enviornment, an example of how a config.py file could look can be seen below.

```python
from google.oauth2 import service_account

bucket_name = '__NAME OF STORAGE BUCKET__'
project = '__FULL GCP PROJECT NAME__'
local_folder = '__/Users/jamie/Documents/dev/site/css/__'

credentials = service_account.Credentials.from_service_account_file(
    '__PATH TO SA KEY__',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
```
