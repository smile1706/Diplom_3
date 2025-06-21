import allure
import pytest

from pages.main_page import MainPage


@allure.epic("Проверка счетчиков заказов и номера заказа")
class TestOrdersList:
    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест увеличения счётчика «Выполнено за всё время» при создании нового заказа")
    def test_new_order_increases_all_time_orders_counter(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        orders_page = main_page.click_on_order_list_page_button()
        orders_page.wait_for_orders_page_data_visibility()
        all_time_orders = orders_page.get_value_of_all_time_counter()
        main_page = orders_page.click_on_constructor_page_button()
        main_page.main_page_loading_wait()
        auth_page = main_page.click_on_login_page_button()
        auth_page.wait_for_login_button_at_auth_page_clickable()
        main_page = auth_page.auth(email, password)
        main_page.main_page_loading_wait()
        main_page.wait_for_create_order_button_clickable()
        main_page.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page.main_page_loading_wait()
        main_page.click_on_create_order_button()
        main_page.main_page_loading_wait()
        main_page.wait_for_order_number_from_api()
        main_page.click_on_close_popup()
        main_page.wait_for_orders_page_button_clickable()
        orders_page = main_page.click_on_order_list_page_button()
        orders_page.wait_for_orders_page_data_visibility()
        all_time_orders_upd = orders_page.get_value_of_all_time_counter()
        assert all_time_orders < all_time_orders_upd

    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест увеличения счётчика «Выполнено за сегодня» при создании нового заказа")
    def test_new_order_increases_today_orders_counter(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests  # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        orders_page = main_page.click_on_order_list_page_button()
        orders_page.wait_for_orders_page_data_visibility()
        today_orders = orders_page.get_value_of_today_counter()
        main_page = orders_page.click_on_constructor_page_button()
        main_page.main_page_loading_wait()
        auth_page = main_page.click_on_login_page_button()
        auth_page.wait_for_login_button_at_auth_page_clickable()
        main_page = auth_page.auth(email, password)
        main_page.main_page_loading_wait()
        main_page.wait_for_create_order_button_clickable()
        main_page.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page.main_page_loading_wait()
        main_page.click_on_create_order_button()
        main_page.main_page_loading_wait()
        main_page.wait_for_order_number_from_api()
        main_page.click_on_close_popup()
        main_page.wait_for_orders_page_button_clickable()
        orders_page = main_page.click_on_order_list_page_button()
        orders_page.wait_for_orders_page_data_visibility()
        today_orders_upd = orders_page.get_value_of_today_counter()
        assert today_orders < today_orders_upd

    @pytest.mark.parametrize('path_index, ingredient_index', [(1, 2)])  # Краторная булка N-200i
    @allure.title("Тест появления номера заказа в разделе «В работе» после оформления заказа")
    def test_new_order_number_shows_in_progress_section(self,driver,create_and_delete_user_after_tests,path_index, ingredient_index):
        email, password = create_and_delete_user_after_tests # получаем данные из фикстуры
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        auth_page = main_page.click_on_login_page_button()
        auth_page.wait_for_login_button_at_auth_page_clickable()
        main_page = auth_page.auth(email, password)
        main_page.main_page_loading_wait()
        main_page.wait_for_create_order_button_clickable()
        main_page.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        main_page.main_page_loading_wait()
        main_page.click_on_create_order_button()
        main_page.main_page_loading_wait()
        main_page.wait_for_order_number_from_api()
        order_number = main_page.get_order_number_popup()
        main_page.click_on_close_popup()
        main_page.wait_for_orders_page_button_clickable()
        orders_page = main_page.click_on_order_list_page_button()
        orders_page.wait_for_orders_page_data_visibility()
        orders_page.wait_for_order_number_in_current_list(order_number)
        orders_in_progress = orders_page.get_order_number_from_current_list()
        assert order_number in orders_in_progress
