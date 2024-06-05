import allure
from locators.profile_page_locators import ProfilePageLocators
from locators.headers_locators  import HeaderLocators
from pages.base_page import BasePage
from data import Url


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Перейти к истории заказов')
    def go_to_orders_history(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BTN)

    @allure.step('Перейти на страницу Лента заказов')
    def go_to_orders_feed_page(self):
        self.click_on_element(HeaderLocators.ORDERS_FEED_BTN)
        self.wait_load_url(Url.FEED)

    @allure.step('Выйти из профиля')
    def logout(self):
        self.click_on_element(ProfilePageLocators.EXIT_BTN)

    @allure.step('Получить список заказов пользователя')
    def get_history_orders(self):
        self.go_to_orders_history()
        self.wait_element(ProfilePageLocators.ORDERS_HISTORY_LIST)
        orders = [element.text.lstrip('#0') for element in self.get_elements(ProfilePageLocators.ORDERS_HISTORY_LIST)]
        return orders

    @allure.step('Проверить видимость информации о профиле пользователя')
    def check_visible_profile_info(self):
        return self.check_is_visible_element(ProfilePageLocators.PROFILE_INFO)

    @allure.step('Проверить видимость истории заказов пользователя')
    def check_visible_order_history(self):
        return self.check_is_visible_element(ProfilePageLocators.ORDERS_HISTORY_LIST)