import os
from dotenv import load_dotenv


class Config:
    def __init__(self, env="staging"):
        env_path = os.path.join(os.path.dirname(__file__), "..", "config", f"{env}.env")
        load_dotenv(dotenv_path=env_path)
        self.base_url = os.getenv("BASE_URL")