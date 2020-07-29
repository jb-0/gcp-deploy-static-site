from google.cloud import storage, secretmanager
import os
import git
import shutil
import tempfile
import hashlib
import hmac


def authorisation(request):
    secrets = secretmanager.SecretManagerServiceClient()
    secret = secrets.access_secret_version(os.environ.get('SECRET_PATH')).payload.data

    signature = hmac.new(secret, request.data, hashlib.sha1).hexdigest()
    if hmac.compare_digest(signature, request.headers['X-Hub-Signature'].split('=')[1]):
        main()
    else:
        raise RuntimeError('Terminated as HMAC compare is false')


def main():
    storage_client = storage.Client()
    bucket = storage_client.bucket(os.environ.get('BUCKET_NAME'))

    temp_dir = tempfile.mkdtemp()

    git.Repo.clone_from(os.environ.get('GIT_REPO'), temp_dir, branch='master', depth=1)

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
            blob.cache_control = os.environ.get('CACHE_CONTROL')
            blob.upload_from_filename(local_path)
