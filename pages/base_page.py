import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Подождать пока элемент станет кликабельным')
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        source_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(source))
        target_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(target))
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Получение значения url текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать пока указанный текст элемента изменится")
    def wait_for_text_in_element_changes(self,locator,text_to_change):
        return WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, text_to_change))

    @allure.step("Подождать пока текст появится в элементе")
    def wait_for_text_in_element(self,locator, text):
        return WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(locator, text))
