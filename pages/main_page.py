import allure

from locators.main_page_locators import MainPageLocators
from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.orders_page import OrdersPage


class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Подождать пока кнопка «Оформить заказ» станет кликабельной")
    def wait_for_create_order_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Подождать пока кнопка «Лента Заказов» станет кликабельной")
    def wait_for_orders_page_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.ORDER_LIST_BUTTON_HEADER)

    @allure.step("Подождать получения номера заказа от API")
    def wait_for_order_number_from_api(self):
        self.wait_for_text_in_element_changes(MainPageLocators.ORDER_ID_POPUP, '9999')

    @allure.step("Подождать появления всплывающего окна с деталями ингредиента")
    def wait_for_ingredient_details_popup(self):
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step("Подождать закрытия всплывающего окна с деталями ингредиента")
    def wait_for_ingredient_details_popup_closes(self):
        return self.wait_for_element_hide(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step("Получение названия ингредиента во всплывающем окне")
    def get_ingredient_name_popup(self):
        ingredient_name_element = self.get_text_on_element(MainPageLocators.INGREDIENT_NAME_POPUP)
        return ingredient_name_element

    @allure.step("Получение номера заказа во всплывающем окне")
    def get_order_number_popup(self):
        return self.get_text_on_element(MainPageLocators.ORDER_ID_POPUP)

    @allure.step("Клик на кнопку «Оформить заказ»")
    def click_on_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Клик на раздел «Лента заказов»")
    def click_on_order_list_page_button(self):
        self.click_on_element(MainPageLocators.ORDER_LIST_BUTTON_HEADER)
        return OrdersPage(self.driver)

    @allure.step("Клик на кнопку Войти в аккаунт")
    def click_on_login_page_button(self):
        self.click_on_element(MainPageLocators.LOGIN_PAGE_BUTTON)
        return AuthPage(self.driver)

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self,path_index,ingredient_index):
        ingredient_locator = MainPageLocators.ingredient_number(path_index,ingredient_index)
        self.scroll_to_element(ingredient_locator)
        self.click_on_element(ingredient_locator)

    @allure.step("Клик на крестик во всплывающем окне")
    def click_on_close_popup(self):
        self.click_on_element(MainPageLocators.INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON)

    @allure.step("Добавить ингредиент")
    def adding_ingredient_by_drag_and_drop(self, path_index, ingredient_index):
        source = MainPageLocators.ingredient_number(path_index, ingredient_index)
        target = MainPageLocators.CONSTRUCTOR_BASKET_AREA
        self.scroll_to_element(source)
        self.drag_and_drop_element(source, target)

    @allure.step("Получить количество ингредиента")
    def get_ingredient_count(self, path_index, ingredient_index):
        counter = MainPageLocators.ingredient_count(path_index, ingredient_index)
        counter_text = self.get_text_on_element(counter)
        return counter_text
