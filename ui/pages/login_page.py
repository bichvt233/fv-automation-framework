class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        # muốn chuyên URL này vào một biến là base_url để dễ maintain hơn
        base_url = "https://www.saucedemo.com/"
        self.page.goto(base_url)
        self.page.locator("#user-name").wait_for()
        self.page.fill("#user-name", username)

        self.page.locator("#password").wait_for()
        self.page.fill("#password", password)
        self.page.click("#login-button")
        