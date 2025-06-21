import allure

from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step("Клик на раздел «Конструктор»")
    def click_on_constructor_page_button(self):
        self.click_on_element(OrdersPageLocators.CONSTRUCTOR_BUTTON_HEADER)
        from .main_page import MainPage
        return MainPage(self.driver)

    @allure.step("Подождать видимости данных на странице заказов")
    def wait_for_orders_page_data_visibility(self):
        return self.wait_for_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step("Подождать появления номера заказа в списке «В работе»")
    def wait_for_order_number_in_current_list(self,order_number):
        self.wait_for_text_in_element(OrdersPageLocators.ORDER_LIST_CURRENT,order_number)

    @allure.step("Получить номер заказа из списка «В работе»")
    def get_order_number_from_current_list(self):
        return self.get_text_on_element(OrdersPageLocators.ORDER_LIST_CURRENT)

    @allure.step("Получить значение счетчика «Выполнено за все время»")
    def get_value_of_all_time_counter(self):
        return self.get_text_on_element(OrdersPageLocators.ORDERS_ALL_TIME_COUNTER)

    @allure.step("Получить значение счетчика «Выполнено за сегодня»")
    def get_value_of_today_counter(self):
        return self.get_text_on_element(OrdersPageLocators.ORDERS_TODAY_COUNTER)