from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_cart_button(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        login_link.click()
    def find_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        return book_title
    def add_to_cart_name(self, book_title):
        book_add_title = self.browser.find_element(*ProductPageLocators.BOOK_ADD_TITLE)
        assert (book_title.text == book_add_title.text), "Названия разные"
    def find_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price
    def add_to_cart_price(self, book_price):
        book_add_price = self.browser.find_element(*ProductPageLocators.BOOK_ADD_PRICE)
        assert book_price.text == book_add_price.text, "Цены разные"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def success_message_should_disappeare(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeare"
