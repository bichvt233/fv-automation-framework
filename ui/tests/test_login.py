import pytest
from ui.pages.login_page import LoginPage
from ui.tests.data.test_data import VALID_USER, LOCKED_OUT_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER, ERROR_USER, VISUAL_USER

# TC1: Test login với user hợp lệ thì sẽ login thành công và vào được trang products
@pytest.mark.ui
def test_login_valid_user(page, base_url):
    login = LoginPage(page)
    page.goto(base_url)
    username = VALID_USER["username"]
    password = VALID_USER["password"]
    login.login(username, password)
    # Assert: Kiểm tra xem đã vào được trang products chưa bằng cách kiểm tra title của trang
    assert page.locator(".title").inner_text() == "Products"
    # Assert: Kiểm tra xem có hiển thị sản phẩm nào không (để chắc chắn đã vào được trang products)
    assert page.locator(".inventory_item").count() > 0


# TC2: Test login với user bị khóa thì sẽ không login được và hiển thị thông báo lỗi
@pytest.mark.ui
def test_login_locked_out_user(page, base_url):
    login = LoginPage(page)
    page.goto(base_url)
    username = LOCKED_OUT_USER["username"]
    password = LOCKED_OUT_USER["password"]
    login.login(username, password)
    # Assert: Kiểm tra xem có hiển thị thông báo lỗi không
    assert page.locator("[data-test='error']").is_visible()
    # Assert: Kiểm tra nội dung thông báo lỗi có đúng không
    assert page.locator("[data-test='error']").inner_text() == "Epic sadface: Sorry, this user has been locked out."    


# TC3: Test login với user problem_user thì vẫn login được nhưng sẽ gặp lỗi ở các chức năng khác (ảnh sản phẩm bị hỏng,...)
@pytest.mark.ui
def test_login_problem_user(page, base_url):
    login = LoginPage(page)
    page.goto(base_url)
    username = PROBLEM_USER["username"]
    password = PROBLEM_USER["password"]
    login.login(username, password)
    # Assert: Login thành công, vào được trang Products
    assert page.locator(".title").inner_text() == "Products"
    # Assert: Kiểm tra ảnh sản phẩm có hiển thị không
    assert page.locator(".inventory_item_img").first.is_visible()


# TC4: Test login với user performance_glitch_user thì vẫn login được nhưng response chậm hơn bình thường
@pytest.mark.ui
def test_login_performance_glitch_user(page, base_url):
    import time
    login = LoginPage(page)
    page.goto(base_url)
    username = PERFORMANCE_GLITCH_USER["username"]
    password = PERFORMANCE_GLITCH_USER["password"]
    start_time = time.time()
    login.login(username, password)
    page.locator(".title").wait_for(state="visible")
    end_time = time.time()
    response_time = end_time - start_time
    # Assert: Login thành công, vào được trang Products (dù chậm hơn)
    assert page.locator(".title").inner_text() == "Products"
    # Assert: response chậm hơn bình thường
    assert response_time > 1


# TC5: Test login với user error_user thì vẫn login được nhưng sẽ gặp lỗi khi thao tác một số chức năng
@pytest.mark.ui
def test_login_error_user(page, base_url):
    login = LoginPage(page)
    page.goto(base_url)
    username = ERROR_USER["username"]
    password = ERROR_USER["password"]
    login.login(username, password)
    # Assert: Login thành công, vào được trang Products
    assert page.locator(".title").inner_text() == "Products"
    # Assert: Kiểm tra ảnh sản phẩm và button Add to cart có hiển thị không
    assert page.locator(".inventory_item_img").first.is_visible()
    assert page.locator(".btn_inventory").first.is_visible()


# TC6: Test login với user visual_user thì vẫn login được nhưng UI sẽ bị lệch/hiển thị sai
@pytest.mark.ui
def test_login_visual_user(page, base_url):
    login = LoginPage(page)
    page.goto(base_url)
    username = VISUAL_USER["username"]
    password = VISUAL_USER["password"]
    login.login(username, password)
    # Assert: Login thành công, vào được trang Products
    assert page.locator(".title").inner_text() == "Products"
    # Assert: Kiểm tra ảnh sản phẩm và button Add to cart có hiển thị không
    assert page.locator(".inventory_item_img").first.is_visible()
    assert page.locator(".btn_inventory").first.is_visible()



