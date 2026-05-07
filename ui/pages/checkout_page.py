from core.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    SUCCESS_HEADER = ".complete-header"

    def fill_info(self, first, last, zip_code):
        self.fill(self.FIRST_NAME_INPUT, first)
        self.fill(self.LAST_NAME_INPUT, last)
        self.fill(self.POSTAL_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def is_success(self):
        return self.get_text(self.SUCCESS_HEADER) == "Thank you for your order!"