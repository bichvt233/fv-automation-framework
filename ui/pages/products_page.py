from core.base_page import BasePage


class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON = ".inventory_item button"
    CART_LINK = ".shopping_cart_link"

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_LINK)