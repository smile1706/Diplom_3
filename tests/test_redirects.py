import allure
import curl
from pages.auth_page import AuthPage

from pages.main_page import MainPage


@allure.epic("Проверки переходов")
class TestRedirects:
    @allure.title("Тест перехода по клику на раздел «Лента заказов»")
    def test_click_on_order_list_button_redirects_order_list_page(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_order_list_page_button()
        assert main_page.get_current_url() == curl.order_page_url

    @allure.title("Тест перехода по клику на раздел «Конструктор»")
    def test_click_on_constructor_button_redirects_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_login_page_button()
        auth_page = AuthPage(driver)
        auth_page.wait_for_login_button_at_auth_page_clickable()
        auth_page.click_on_constructor_page_button()
        assert auth_page.get_current_url() == f'{curl.main_site}/'
