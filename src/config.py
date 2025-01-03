import os


class Config:
    BUCKET_NAME = os.environ.get("BUCKET_NAME", "local-bucket")
    STORAGE_EMULATOR_HOST = os.environ.get("STORAGE_EMULATOR_HOST", None)
