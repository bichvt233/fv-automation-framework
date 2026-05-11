# Thư viện os được sử dụng để làm việc với hệ thống tệp và đường dẫn
import os 
# Thư viện dotenv được sử dụng để tải biến môi trường từ tệp .env
from dotenv import load_dotenv 


class Config:
    def __init__(self, env="staging"):
        # Xây dựng đường dẫn đến tệp .env dựa trên tham số env
        env_path = os.path.join(os.path.dirname(__file__), "..", "config", f"{env}.env")
        # Tải biến môi trường từ tệp .env 
        load_dotenv(dotenv_path=env_path) 
        # Lấy giá trị của biến môi trường BASE_URL và gán cho thuộc tính base_url của lớp Config
        self.base_url = os.getenv("BASE_URL") 
        