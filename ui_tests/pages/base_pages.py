from seleniumbase import BaseCase

from ui_tests.pages.book_page import BookPage
from ui_tests.pages.dashboard_page import DashboardPage


class BasePages:

    def __init__(self, sb: BaseCase):
        self.sb = sb
        self.DashboardPage = DashboardPage(sb)
        self.BookPage = BookPage(sb)

