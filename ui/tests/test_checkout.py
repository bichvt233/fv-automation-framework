import pytest
@pytest.mark.smoke
@pytest.mark.ui
from ui.pages.login_page import LoginPage
from ui.pages.products_page import ProductsPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.ui
def test_checkout_flow(page):
    login = LoginPage(page)
    product = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Step 1: Login
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product
    product.add_first_product_to_cart()

    # Step 3: Go to cart
    product.go_to_cart()

    # Step 4: Checkout
    cart.checkout()

    # Step 5: Fill info
    checkout.fill_info("Bich", "Vu", "10000")

    # Step 6: Finish order
    checkout.finish_order()

    # Assert
    assert checkout.is_success()