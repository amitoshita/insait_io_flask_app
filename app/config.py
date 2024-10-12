import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:tima144@db:5432/flask_app')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# config.py

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = 'dummy-key'
