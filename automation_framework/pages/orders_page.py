class OrdersPage:

    def __init__(self,page):
        self.page=page

    def open(self):
        self.page.goto("http://localhost:5173")

    def enter_item(self,item):
        self.page.get_by_test_id("item-input").fill(item)

    def click_create(self):
        self.page.get_by_test_id("create-btn").click()

    def first_order_text(self):
        return self.page.locator("li").first.text_content()
