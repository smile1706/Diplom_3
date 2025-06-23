import allure

from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step("Подождать пока кнопка «Войти» станет кликабельной")
    def wait_for_login_button_at_auth_page_clickable(self):
        self.wait_for_element_clickable(AuthPageLocators.LOGIN_BUTTON_AT_AUTH_PAGE)

    @allure.step("Клик на раздел «Конструктор»")
    def click_on_constructor_page_button(self):
        self.click_on_element(AuthPageLocators.CONSTRUCTOR_BUTTON_HEADER)

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.send_keys_to_input(AuthPageLocators.EMAIL, email)
        self.send_keys_to_input(AuthPageLocators.PASSWORD, password)
        self.click_on_element(AuthPageLocators.LOGIN_BUTTON_AT_AUTH_PAGE)
