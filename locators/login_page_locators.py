class LoginPageLocators:
    LOGIN_FORM = ('xpath', '//h2[text()="Вход"]')  # форма авторизации
    EMAIL_INPUT = ('xpath', '//label[text()="Email"]/../input')  # поле ввода электронной почты
    PASSWORD_INPUT = ('xpath', '//label[text()="Пароль"]/../input')  # поле ввода пароля
    SUBMIT_BUTTON = ('xpath', '//form//button')  # кнопка Войти
    RECOVERY_PASSWORD = ('xpath', '//a[text()="Восстановить пароль"]')  # кнопка Восстановить пароль
    SHOW_PASSWORD = ('xpath', '//div[contains(@class, "input__icon-action")]')  # кнопка Показать/скрыть пароль
    PASSWORD_CONTAIN = ('xpath', '//label[text()="Пароль"]/..')  # отображение активности поля
