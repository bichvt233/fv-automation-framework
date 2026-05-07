from core.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = "#checkout"

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)