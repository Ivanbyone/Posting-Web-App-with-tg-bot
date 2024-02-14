import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

PORT = int(os.getenv("port"))
HOST = str(os.getenv("host"))

DB_URL = os.getenv("db_url")
DB_NAME = os.getenv("db_name")

PROJECT_NAME = os.getenv("project_name")
