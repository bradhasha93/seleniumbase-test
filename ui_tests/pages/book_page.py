from seleniumbase import BaseCase


class BookPage:

    BACK_TO_BOOKSTORE_BUTTON = "//button[@id='addNewRecordButton']"
    BOOK_TITLE_TEXT = "//*[@id='title-wrapper']//*[@id='userName-value']"

    def __init__(self, sb: BaseCase):
        self.sb = sb

    def verify_book_data(self, book):
        self.sb.assert_text(selector=self.BOOK_TITLE_TEXT, text=book)

    def click_back_to_bookstore_button(self):
        self.sb.click(selector=self.BACK_TO_BOOKSTORE_BUTTON)
        self.sb.assert_element_not_present(self.BACK_TO_BOOKSTORE_BUTTON)

