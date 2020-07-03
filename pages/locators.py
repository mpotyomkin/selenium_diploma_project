from selenium.webdriver.common.by import By

LANG_PREFIX = "/ru"

class MainPageLocators():
    PAGE_URL = "http://selenium1py.pythonanywhere.com/"

# promo link to crash tests
#MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():

    PAGE_URL        = "/accounts/login/"
    LOGIN_FORM      = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM   = (By.CSS_SELECTOR, "#register_form")

    