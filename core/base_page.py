class BasePage:
    # Nhận đối tượng page từ Playwright
    def __init__(self, page): 
        self.page = page

    # locator là một chuỗi định danh cho phần tử trên trang (ví dụ: CSS selector, XPath, v.v.)
    def click(self, locator: str): 
        self.page.locator(locator).wait_for()
        self.page.locator(locator).click()

    # Điền văn bản vào một trường nhập liệu trên trang
    def fill(self, locator: str, text: str): 
        self.page.locator(locator).wait_for()
        self.page.locator(locator).fill(text)

    # Lấy văn bản từ một phần tử trên trang
    def get_text(self, locator: str) -> str:
        # Trả về văn bản bên trong phần tử được xác định bởi locator 
        return self.page.locator(locator).inner_text() 
