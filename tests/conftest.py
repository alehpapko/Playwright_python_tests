import pytest

from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    return ProductsPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)
