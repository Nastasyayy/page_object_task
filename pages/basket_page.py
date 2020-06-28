from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_cart(self): #проверка на то, что в корзине нет товаров
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_CART), \
            "В корзине есть товары!"
    def should_be_message_of_empty_cart(self): #Ожидаем, что есть текст о том что корзина пуста
        assert self.is_not_element_present(*BasePageLocators.EMPTY_CART_MESSAGE), \
            "Корзина не пуста, сообщения о пустой корзине нет!"
