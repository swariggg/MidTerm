import os

from dotenv import load_dotenv

# Lee las variables del archivo .env (si existe)
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
TABLE_NAME = os.getenv("TABLE_NAME", "short_links")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
# Orígenes permitidos para CORS, separados por comas
CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",")]
