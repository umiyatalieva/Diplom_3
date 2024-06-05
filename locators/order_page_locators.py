from selenium.webdriver.common.by import By

class OrdersPageLocators:
    ORDER_ITEM = ('xpath', '//li[contains(@class, "OrderHistory_listItem")]')  # заказ
    ALL_ORDERS_COUNT = ('xpath', '//p[text()="Выполнено за все время:"]/../p[contains(@class, "OrderFeed_number")]')  # счетчик всех заказов
    TODAY_ORDERS_COUNT = ('xpath', '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "OrderFeed_number")]')  # счетчик заказов за сегодня
    ALL_ORDERS_LIST = ('xpath', '//p[contains(text(), "#")]')  # лента выполненных заказов
    ORDER_IN_WORK = ('xpath', '//ul[contains(@class, "orderListReady")]/li')  # заказ в работе
    MODAL_WINDOW = ('xpath', '//section[contains (@class, "modal_opened")]')  # модальное окно