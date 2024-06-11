from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTER_IN_ACCOUNT = ('xpath', '//button[text()="Войти в аккаунт"]')  # кнопка Войти в аккаунт
    BASKET_AREA = ('xpath', '//ul[contains(@class, "BurgerConstructor_basket")]')  # область сборки бургера
    CREATE_ORDER = ('xpath', '//button[text()="Оформить заказ"]')  # кнопка Оформить заказ
    INGREDIENT = ('xpath', '//a[contains(@class,"BurgerIngredient")]')  # ингредиент бургера
    INGREDIENT_COUNTER = ('xpath', '//p[contains(@class, "counter__num")]')  # счетчик ингредиента
    ORDER_NUMBER = ('xpath', '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа
    PROFILE_BTN = ('xpath', '//p[text()="Личный Кабинет"]')  # кнопка перехода в личный кабинет
    MODAL_WINDOW = ('xpath', '//section[contains (@class, "modal_opened")]')  # модальное окно
    CLOSE_MODAL_WINDOW = ('xpath', '//button[contains(@class, "modal__close")]')  # кнопка закрытия модального окна
    ORDERS_FEED_BTN = ('xpath', '//p[text()="Лента Заказов"]')  # кнопка "Лента Заказов"