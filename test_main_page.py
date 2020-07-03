from .pages.main_page import MainPage
from .pages.locators import MainPageLocators #MAIN_PAGE_URL
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPageLocators.PAGE_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    
    login_page = page.go_to_login_page() 
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.PAGE_URL)
    page.open()
    page.should_be_login_link()


'''
def test_add_to_cart(browser):
    page = ProductPage(browser, url="")   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
'''