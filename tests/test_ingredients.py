import allure
import pytest

from data import Data
from pages.main_page import MainPage


@allure.epic("Проверки счетчиков и всплывающих окон ингредиентов")
class TestIngredients:
    @pytest.mark.parametrize(
        'path_index, ingredient_index, ingredient_name',
        [(1,2, 'Краторная булка N-200i'),
         (2,4, 'Соус с шипами Антарианского плоскоходца'),
         (3,8, 'Мини-салат Экзо-Плантаго')
         ])
    @allure.title("Тест появления всплывающего окна с деталями, если кликнуть на ингредиент")
    def test_click_on_ingredient_opens_popup_with_details(self, driver,path_index,ingredient_index, ingredient_name):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_ingredient(path_index,ingredient_index)
        main_page.wait_for_ingredient_details_popup()
        ingredient_name_in_popup = main_page.get_ingredient_name_popup()
        assert ingredient_name_in_popup == ingredient_name

    @allure.title("Тест закрытия всплывающего окна кликом по крестику")
    def test_click_on_close_button_popup_closes(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_on_ingredient(Data.path_index,Data.ingredient_index)
        main_page.wait_for_ingredient_details_popup()
        main_page.click_on_close_popup()
        popup_closed = main_page.wait_for_ingredient_details_popup_closes()
        assert popup_closed is True

    @pytest.mark.parametrize(
        'path_index, ingredient_index',
        [(1, 2), #Краторная булка N-200i
         (2, 4), #Соус с шипами Антарианского плоскоходца
         (3, 8) #Мини-салат Экзо-Плантаго
         ])
    @allure.title("Тест увеличения счетчика ингредиента при добавлении его в заказ")
    def test_increase_counter_adding_ingredient_to_order(self, driver, path_index, ingredient_index):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        start_count = int(main_page.get_ingredient_count(path_index, ingredient_index))
        main_page.adding_ingredient_by_drag_and_drop(path_index, ingredient_index)
        after_add_count = int(main_page.get_ingredient_count(path_index, ingredient_index))
        assert after_add_count>start_count