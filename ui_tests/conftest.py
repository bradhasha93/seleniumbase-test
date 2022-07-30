import pytest

from ui_tests.pages.base_pages import BasePages


@pytest.fixture(scope="function", autouse=True)
def load_base_url(sb):
    sb.open("https://demoqa.com/books")


@pytest.fixture(scope="function")
def bp(sb):
    yield BasePages(sb)
