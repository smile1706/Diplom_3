## Дипломный проект. Задание 3: UI-тесты
<hr>

## Студент: Муталлапов Динар

## <h>Когорта: #21</h>
<hr>

## <h>Project: Stellar Burgers UI</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла          | Содержание файла                                         |
|-------------------------|----------------------------------------------------------|
| tests dir               | Директория с тестами                                     |
| test_ingredients.py     | Тесты проверки счетчиков и всплывающих окон ингредиентов |
| test_orders_list.py     | Тесты проверки счетчиков заказов и номера заказа         |
| test_redirects.py       | Тесты проверки переходов                                 |
| conftest.py             | Фикстуры                                                 |
| locators dir            | Директория с локаторами                                  |
| auth_page_locators.py   | Локаторы страницы авторизации                            |
| main_page_locators.py   | Локаторы главной страницы                                |
| orders_page_locators.py | Локаторы страницы ленты заказов                          |
| pages dir               | Директория с Page Object                                 |
| auth_page.py            | Page Object страницы авторизации                         |
| base_page.py            | Методы для POM                                           |
| main_page.py            | Page Object главной страницы                             |
| orders_page.py          | Page Object страницы ленты заказов                       |
| curl.py                 | Файл с URL и эндпоинтами API                             |
| data.py                 | Генератор данных, header и body запросов API             |
| helpers.py              | http клиент для создания/удаления пользователя           |
| requirements.txt        | Файл с зависимостями                                     |
| allure_results dir      | Папка с отчетами Allure                                  |

