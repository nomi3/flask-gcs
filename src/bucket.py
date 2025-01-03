from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
from google.cloud.storage.bucket import Bucket

from src.config import Config


def get_storage_client():
    emulator_host = Config.STORAGE_EMULATOR_HOST

    if emulator_host:
        client = storage.Client(
            credentials=AnonymousCredentials(),
            project="test",
        )
    else:
        client = storage.Client()

    return client


def get_bucket() -> Bucket:
    client = get_storage_client()
    return client.bucket(Config.BUCKET_NAME)
