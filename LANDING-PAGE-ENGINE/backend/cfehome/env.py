import io
import os
import pathlib
from decouple import Config, RepositoryEnv
from functools import lru_cache

BASE_DIR = pathlib.Path(__file__).parent.parent

ENV_PATH = BASE_DIR.parent / '.env'

@lru_cache
def get_config(use_gcloud=True):
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config
    return config
