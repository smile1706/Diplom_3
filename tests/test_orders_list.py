import allure
import pytest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage


@allure.epic("Проверка счетчиков заказов и номера заказа")
class TestOrdersList:
    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест увеличения счётчика «Выполнено за всё время» при создании нового заказа")
    def test_new_order_increases_all_time_orders_counter(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_order_list_page_button()
        orders_page = OrdersPage(driver)
        orders_page.wait_for_orders_page_data_visibility()
        all_time_orders = orders_page.get_value_of_all_time_counter()
        orders_page.click_on_constructor_page_button()
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_login_page_button()
        auth_page = AuthPage(driver)
        auth_page.wait_for_login_button_at_auth_page_clickable()
        auth_page.auth(email, password)
        main_page_authorised = MainPage(driver)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_create_order_button_clickable()
        main_page_authorised.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.click_on_create_order_button()
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_order_number_from_api()
        main_page_authorised.click_on_close_popup()
        main_page_authorised.wait_for_orders_page_button_clickable()
        main_page_authorised.click_on_order_list_page_button()
        orders_page_check = OrdersPage(driver)
        orders_page_check.wait_for_orders_page_data_visibility()
        all_time_orders_upd = orders_page_check.get_value_of_all_time_counter()
        assert all_time_orders < all_time_orders_upd

    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест увеличения счётчика «Выполнено за сегодня» при создании нового заказа")
    def test_new_order_increases_today_orders_counter(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests  # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_order_list_page_button()
        orders_page = OrdersPage(driver)
        orders_page.wait_for_orders_page_data_visibility()
        today_orders = orders_page.get_value_of_today_counter()
        orders_page.click_on_constructor_page_button()
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_login_page_button()
        auth_page = AuthPage(driver)
        auth_page.wait_for_login_button_at_auth_page_clickable()
        auth_page.auth(email, password)
        main_page_authorised = MainPage(driver)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_create_order_button_clickable()
        main_page_authorised.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.click_on_create_order_button()
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_order_number_from_api()
        main_page_authorised.click_on_close_popup()
        main_page_authorised.wait_for_orders_page_button_clickable()
        main_page_authorised.click_on_order_list_page_button()
        orders_page_check = OrdersPage(driver)
        orders_page_check.wait_for_orders_page_data_visibility()
        today_orders_upd = orders_page_check.get_value_of_today_counter()
        assert today_orders < today_orders_upd

    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест появления номера заказа в разделе «В работе» после оформления заказа")
    def test_new_order_number_shows_in_progress_section(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_login_page_button()
        auth_page = AuthPage(driver)
        auth_page.wait_for_login_button_at_auth_page_clickable()
        auth_page.auth(email, password)
        main_page_authorised = MainPage(driver)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_create_order_button_clickable()
        main_page_authorised.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.click_on_create_order_button()
        main_page_authorised.main_page_loading_wait()
        main_page_authorised.wait_for_order_number_from_api()
        order_number = main_page_authorised.get_order_number_popup()
        main_page_authorised.click_on_close_popup()
        main_page_authorised.wait_for_orders_page_button_clickable()
        main_page_authorised.click_on_order_list_page_button()
        orders_page = OrdersPage(driver)
        orders_page.wait_for_orders_page_data_visibility()
        orders_page.wait_for_order_number_in_current_list(order_number)
        orders_in_progress = orders_page.get_order_number_from_current_list()
        assert order_number in orders_in_progress
