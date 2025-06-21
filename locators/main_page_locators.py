from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_LIST_BUTTON_HEADER = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX'][@href='/feed']") #//a[contains(@class,'AppHeader_header__link__3D_hX')]/p[text()='Лента Заказов']
    INGREDIENT_NAME_POPUP = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']") #/text()
    INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON = (By.XPATH, "//section[1]/div/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    CONSTRUCTOR_BASKET_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket') and contains(@class, 'mt-25')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']")  # оверлей
    LOGIN_PAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # кнопка Войти в аккаунт
    CREATE_ORDER_BUTTON = (By.XPATH,"//button[contains(text(),'Оформить заказ')]")
    ORDER_ID_POPUP = (By.XPATH,"//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    INGREDIENT_DETAILS_POPUP = (By.XPATH,"//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div[@class='Modal_modal__container__Wo2l_']")

    @staticmethod
    def ingredient_number(path_index,ingredient_index):
        return By.XPATH, f"//h2[@class='text text_type_main-medium mb-6 mt-10'][1]/following-sibling::ul[{path_index}]/a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][{ingredient_index}]",

    @staticmethod
    def ingredient_count(path_index,ingredient_index):
        return By.XPATH, f"//ul[@class='BurgerIngredients_ingredients__list__2A-mT'][{path_index}]/a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][{ingredient_index}]/div/p[@class='counter_counter__num__3nue1']"
