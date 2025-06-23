from selenium.webdriver.common.by import By


class OrdersPageLocators:
    ORDERS_ALL_TIME_COUNTER = (By.XPATH,"//p[@class='text text_type_main-medium'][text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_TODAY_COUNTER = (By.XPATH,"//p[@class='text text_type_main-medium'][text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_LIST_CURRENT = (By.XPATH,"//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']") #список заказов "В работе"
    ORDERS_LIST_TITLE = (By.XPATH,"//h1[@class='text text_type_main-large mt-10 mb-5']")
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, "//a[contains(@class,'AppHeader_header__link__3D_hX')]/p[text()='Конструктор']")
