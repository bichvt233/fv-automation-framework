import requests
from api.tests.data.api_data import VALID_API_USER, API_KEY

def test_login_api():
    base_api_url = "https://reqres.in/api"
    headers = {"x-api-key": API_KEY}
    res = requests.post(f"{base_api_url}/login", headers=headers, json={
        "email": VALID_API_USER["email"],
        "password": VALID_API_USER["password"]
    })
    # Kiểm tra mã trạng thái trả về là 200 (thành công)
    assert res.status_code == 200
    # Kiểm tra token trả về không rỗng và có độ dài hợp lệ
    token = res.json().get("token")
    assert token is not None
    assert len(token) > 0
