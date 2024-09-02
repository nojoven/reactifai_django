from decouple import Config, RepositoryEnv
from functools import lru_cache
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent

ENV_PATH = BASE_DIR.parent / '.env'

@lru_cache
def get_config(use_gcloud=True):
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))

    return Config

config = get_config()