from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.locator('#checkout')
        self.firstname_input = page.locator('#first-name')
        self.lastname_input = page.locator('#last-name')
        self.postal_code_input = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.finish_button = page.locator('#finish')

    def checkout(self):
        self.checkout_button.click()

    def enter_user_info(self, firstname: str, lastname: str, postal_code: str):
        self.firstname_input.fill(firstname)
        self.lastname_input.fill(lastname)
        self.postal_code_input.fill(postal_code)

    def finish_order(self):
        self.continue_button.click()
        self.finish_button.click()
