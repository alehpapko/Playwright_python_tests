from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_item = page.locator('.inventory_item_name').nth(0)
        self.add_to_cart_button = page.locator("button").get_by_text("Add to cart")
        self.cart_button = page.locator('.shopping_cart_link')

    def add_item_to_cart(self):
        self.first_item.click()
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_button.click()
