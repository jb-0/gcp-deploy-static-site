from google.cloud import storage
from config import bucket_name, credentials, project
import os
import git
import shutil
import tempfile


def main():
    storage_client = storage.Client(credentials=credentials, project=project)
    bucket = storage_client.bucket(bucket_name)

    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from('https://github.com/jb-0/site.git', temp_dir, branch='master', depth=1)

    upload_repo_to_bucket(temp_dir, bucket)

    shutil.rmtree(temp_dir)


def upload_repo_to_bucket(dir, bucket):
    exclude_subdirs = set(['.git'])
    exclude_files = set(['README.md', 'LICENSE', '.gitignore'])

    for path, subdirs, files in os.walk(dir):
        subdirs[:] = [sd for sd in subdirs if sd not in exclude_subdirs]
        files[:] = [f for f in files if f not in exclude_files]
        for name in files:
            local_path = os.path.join(path, name)
            blob_path = local_path.replace(dir + '/', '')

            blob = bucket.blob(blob_path)
            blob.upload_from_filename(local_path)


main()
