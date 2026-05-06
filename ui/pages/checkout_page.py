class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_info(self, first, last, zip_code):
        self.page.locator("#first-name").wait_for()
        self.page.fill("#first-name", first)
        self.page.locator("#last-name").wait_for()
        self.page.fill("#last-name", last)
        self.page.locator("#postal-code").wait_for()
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def finish_order(self):
        self.page.click("#finish")

    def is_success(self):
        return self.page.locator(".complete-header").inner_text() == "Thank you for your order!"