class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).wait_for()
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).wait_for()
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
