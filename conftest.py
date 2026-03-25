import pytest
from playwright.sync_api import Page

from tests.ui.pages.buttons import ButtonsPage
from tests.ui.pages.checkbox import CheckboxPage
from tests.ui.pages.links import LinksPage
from tests.ui.pages.radio_button import RadioButtonPage
from tests.ui.pages.textbox import TextboxPage
from tests.ui.pages.web_table import WebTablePage


@pytest.fixture
def buttons(page: Page) -> ButtonsPage:
    return ButtonsPage(page)

@pytest.fixture
def checkbox(page: Page):
    return CheckboxPage(page)

@pytest.fixture
def links(page: Page):
    return LinksPage(page)

@pytest.fixture
def radio_button(page: Page):
    return RadioButtonPage(page)

@pytest.fixture
def textbox(page: Page):
    return TextboxPage(page)

@pytest.fixture
def web_table(page: Page):
    return WebTablePage(page)
