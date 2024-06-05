class ProfilePageLocators:
    PROFILE_INFO = ('xpath', '//div[contains(@class, "Profile")]')  # информация о профиле пользователя
    ORDER_HISTORY_BTN = ('xpath', '//a[text()="История заказов"]')  # кнопка перехода в историю заказов
    EXIT_BTN = ('xpath', '//button[text()="Выход"]')  # кнопка Выйти из профиля
    ORDERS_HISTORY_LIST = ('xpath', '//p[contains(text(), "#")]')  # история заказов пользователя