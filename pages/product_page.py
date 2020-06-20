from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_cart_button(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        login_link.click()

