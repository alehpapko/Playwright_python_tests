from playwright.sync_api import Page, expect

from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage


def test_e2e_order(page: Page,
                   login_page: LoginPage,
                   products_page: ProductsPage,
                   cart_page: CartPage):
    # login
    login_page.load_page()
    login_page.login("standard_user", "secret_sauce")

    # create order
    products_page.add_item_to_cart()
    products_page.open_cart()
    cart_page.checkout()
    cart_page.enter_user_info("Name", "Lastname", "230023")
    cart_page.finish_order()

    # check successes message
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
