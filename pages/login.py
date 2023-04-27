from playwright.sync_api import Page


class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('#user-name')
        self.pass_input = page.locator('#password')
        self.login_button = page.locator('#login-button')

    def load_page(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.pass_input.fill(password)
        self.login_button.click()
