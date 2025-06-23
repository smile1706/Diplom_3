from selenium.webdriver.common.by import By


class AuthPageLocators: #Локаторы для входа
    EMAIL = (By.NAME, "name") # поле Емейл
    PASSWORD = (By.NAME, "Пароль") # поле Пароль
    LOGIN_BUTTON_AT_AUTH_PAGE = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа на Странице входа
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, "//a[contains(@class,'AppHeader_header__link__3D_hX')]/p[text()='Конструктор']") # кнопка Конструктор в шапке
