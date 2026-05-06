import pytest
from ui.pages.login_page import LoginPage
from ui.pages.products_page import ProductsPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage
from playwright.sync_api import expect
from ui.tests.data.checkout_data import VALID_USER, CHECKOUT_INFO, EXPECTED_PRODUCT_COUNT

@pytest.mark.smoke
@pytest.mark.ui
def test_checkout_flow(page, base_url):
    login = LoginPage(page)
    product = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Step 1: Login
    page.goto(base_url)
    username = VALID_USER["username"]
    password = VALID_USER["password"]
    login.login(username, password)
    # Verify login successful by checking the title of the page
    expect(page.locator(".title")).to_have_text("Products") 

    # Step 2: Kiểm tra xem trong màn hình có sản phẩm nào không, nếu có thì add vào cart
    # kiểm tra xem có sản phẩm nào không, nếu có thì thực hiện add 1 sản phẩm vào, nếu không thì báo không có sản phẩm nào để add vào cart
    expect(page.locator(".inventory_item")).to_have_count(EXPECTED_PRODUCT_COUNT)
    product.add_first_product_to_cart()



    # Step 3: Go to cart
    product.go_to_cart()

    # Step 4: Checkout
    cart.checkout()

    # Step 5: Fill info
    first_name = CHECKOUT_INFO["first_name"]
    last_name = CHECKOUT_INFO["last_name"]
    postal_code = CHECKOUT_INFO["postal_code"]
    checkout.fill_info(first_name, last_name, postal_code)

    # Step 6: Finish order
    checkout.finish_order()

    # Assert
    assert checkout.is_success()