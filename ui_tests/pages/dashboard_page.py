from seleniumbase import BaseCase


class DashboardPage:

    SEARCH_INPUT = "input#searchBox"
    BOOK_LINK = "//a[contains(., '%s')]"

    def __init__(self, sb: BaseCase):
        self.sb = sb

    def open_book_link(self, book):
        self.sb.type(selector=self.SEARCH_INPUT, text=book)
        self.sb.click(selector=self.BOOK_LINK % book)
