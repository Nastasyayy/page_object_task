from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTER_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class ProductPageLocators():
    BUTTON_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.TAG_NAME, "h1")
    BOOK_ADD_TITLE = (By.CSS_SELECTOR, ".alertinner  strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_ADD_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    ITEMS_IN_CART = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")