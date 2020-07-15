from google.cloud import storage
from config import bucketName, localFolder, bucketFolder, credentials
from os import listdir, path
import git
import shutil
import tempfile

storage_client = storage.Client(credentials=credentials, project="personal-site-283305")
bucket = storage_client.bucket(bucketName)


def get_repo():
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from('https://github.com/jb-0/site.git', temp_dir, branch='master', depth=1)
    #shutil.move(path.join(t, 'setup.py'), '.')
    shutil.rmtree(temp_dir)


def upload_files(bucketName):
    """Upload files to GCP bucket."""
    files = [f for f in listdir(localFolder) if path.isfile(path.join(localFolder, f))]
    for file in files:
        localFile = localFolder + file
        blob = bucket.blob(bucketFolder + file)
        blob.upload_from_filename(localFile)
    return f'Uploaded {files} to "{bucketName}" bucket.'


upload_files(bucket)
