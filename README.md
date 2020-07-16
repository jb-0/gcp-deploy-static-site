# GCS Static site continuous deployment

This simple script clones a git repo into a local temp folder. The script walks through this temp folder and writes the files to a storage bucket.

To use this script run the main.py file, you will need to include appropriate configuration for your enviornment, an example of how a config.py file could look can be seen below.