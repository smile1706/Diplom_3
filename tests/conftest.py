import allure
import pytest

from selenium import webdriver

import data
import helper
from curl import *

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
@allure.title("Регистрация пользователя, создание заголовка с accessToken в тест и последующее удаление пользователя")
def create_and_delete_user_after_tests():
    with allure.step("Получение email, password от генератора"):
        email, password, name = data.generate_registration_data()
    with allure.step("Создание тела запроса для регистрации"):
        register_body = data.register_body(email, password, name) #создали тело запроса для регистрации
    with (allure.step("Выполнение запроса регистрации")):
        register_response = helper.UserMethods.register_user(register_body) #запрос для регистрации
    with allure.step("Проверка статус-кода и сообщения при успешной регистрации"):
        assert register_response.status_code == 200 and register_response.json()['success'] == True #проверка успешности запроса
    with allure.step("Получение accessToken из ответа на запрос"):
        access_token = register_response.json()['accessToken']
    with allure.step("Создание заголовка запроса с accessToken"):
        auth_header = data.generate_auth_header(access_token) #создали заголовок с accessToken
    with allure.step("Передача email и password в тест"):
        yield email,password
    with allure.step("Выполнение запроса на удаления пользователя"):
        delete_response = helper.UserMethods.delete_user(auth_header) #запрос для удаления
    with allure.step("Проверка успешного удаления пользователя"):
        assert delete_response.status_code == 202 and delete_response.json()['success'] == True #проверка успешности запроса