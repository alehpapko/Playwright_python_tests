from playwright.sync_api import Page, expect

from pages.login import LoginPage


def test_login(page: Page,
               login_page: LoginPage):
    login_page.load_page()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_user_login(page: Page,
                           login_page: LoginPage):
    login_page.load_page()
    login_page.login("locked_out_user", "secret_sauce")

    expect(page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()
