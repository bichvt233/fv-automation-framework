import pytest
from ui.pages.login_page import LoginPage
from ui.pages.products_page import ProductsPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.ui
def test_checkout_flow(page):
    login = LoginPage(page)
    product = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Step 1: Login
    username = "standard_user"
    password = "secret_sauce"
    login.login(username, password)
    expect(page.locator(".title")).to_have_text("Products") 

    # Step 2: Add product
    product.add_first_product_to_cart()

    # Step 3: Go to cart
    product.go_to_cart()

    # Step 4: Checkout
    cart.checkout()

    # Step 5: Fill info
    first_name = "Bich"
    last_name = "Vu"
    postal_code = "10000"
    checkout.fill_info(first_name, last_name, postal_code)

    # Step 6: Finish order
    checkout.finish_order()

    # Assert
    assert checkout.is_success()