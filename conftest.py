# Thêm import pytest để sử dụng các tính năng của pytest trong file này
import pytest 
# Thêm import Config để sử dụng lớp Config trong file này
from core.config import Config 

# Thêm tùy chọn --env để chỉ định môi trường chạy test (mặc định là staging)
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against") 

# Thiết lập fixture có phạm vi session để chỉ tạo một lần cho toàn bộ suite test
@pytest.fixture(scope="session") 
# Sử dụng fixture env để lấy giá trị của tùy chọn --env từ dòng lệnh và trả về nó cho các test sử dụng
def env(request):  
    return request.config.getoption("--env") 


@pytest.fixture(scope="session")
# Sử dụng fixture env để tạo một instance của Config với môi trường được chỉ định và trả về nó cho các test sử dụng
def config(env): 
    return Config(env=env)


@pytest.fixture(scope="session")
# Sử dụng fixture config để lấy base_url từ file config và trả về nó cho các test sử dụng
def base_url(config): 
    return config.base_url

@pytest.fixture(scope="session")
# Cấu hình cho trình duyệt, ví dụ: kích thước cửa sổ, chế độ headless, v.v.
def browser_context_args(): 
    return {
        "viewport": {"width": 1280, "height": 720},
    }

@pytest.fixture(scope="session")
# Cấu hình cho trình duyệt, ví dụ: chế độ headless, v.v.
def browser_type_launch_args(): 
    return {
        # Chạy trình duyệt ở chế độ headless (không hiển thị giao diện người dùng) để tăng tốc độ và giảm tài nguyên sử dụng
        "headless": True  
    }

# Thêm import pytest để sử dụng các tính năng của pytest trong file này
import pytest 
# Thêm import allure để sử dụng tính năng đính kèm ảnh chụp màn hình khi test thất bại
import allure 

# Sử dụng hook pytest_runtest_makereport để kiểm tra kết quả của mỗi test sau khi nó chạy xong  
@pytest.hookimpl(hookwrapper=True) 
# Khi một test chạy xong, pytest sẽ gọi hàm này để tạo báo cáo kết quả của test đó
def pytest_runtest_makereport(item): 
    outcome = yield
    rep = outcome.get_result()

    # Nếu test đã chạy xong và kết quả là thất bại, thì thực hiện các bước sau
    if rep.when == "call" and rep.failed: 
        # Lấy đối tượng page từ các tham số của test (nếu có)
        page = item.funcargs.get("page") 
        # Nếu có đối tượng page, thì chụp ảnh màn hình và đính kèm nó vào báo cáo Allure
        if page: 
            allure.attach(
                page.screenshot(),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )
