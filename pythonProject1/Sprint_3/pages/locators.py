from conftest import *


class AuthorizationForm:
    # форма для ввода логина
    login = (By.XPATH, './/input[@name="name"]')

    # Форма для ввода email
    email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле для ввода пароля
    password = (By.XPATH, './/input[@name="Пароль"]')  # форма для ввода пароля

    # Уведомление о вводе неправильного пароля
    password_fail = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Кнопка входа на страницах register и login
    button_login = (By.XPATH, './/button[contains(text(),"Войти")]')

    # Кнопка регистрации на странице register
    register_button = (By.XPATH, './/button[text()="Зарегистрироваться"]')

    # Кнопка востановить пароль на странице /login
    button_password_setting = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Кнопака Войти на странице register
    button_login_reg_form = (By.XPATH, "//a[contains(text(),'Войти')]")

    # Заголовок Вход на странице /login
    title_login_page = (By.XPATH, "//h2[contains(text(),'Вход')]")


class AppHeader:
    # Cсылка для входа в личный кабинет
    link_acc = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # Ссылка для входа в раздел конструктор
    link_constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Ссылка на логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')


class MainPage:
    # Кнопка войти в аккаунт на главной странице
    button_login_acc = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Заголовок на главной стрице Соберите бургер
    title_main_page = (By.XPATH, "//h1[text() = 'Соберите бургер']")

    # Кнопка оформить заказ на главной странице
    button_checkout = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Активная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Секция соусов
    sauce_element = (By.XPATH, "//span[text() = 'Соусы']")

    # Секция Булки
    bread_element = (By.XPATH, "//span[text() = 'Булки']")

    # Секция Начинки
    filling_element = (By.XPATH, "//span[text() = 'Начинки']")


class ProfilePage:
    # Кнопка выхода из Личного кабинета
    button_exit = (By.XPATH, "//button[contains(text(),'Выход')]")


def wait_el(driver_to_use, locator):
    WebDriverWait(driver_to_use, 3).until(
        expected_conditions.visibility_of_element_located(locator))


def wait_url(driver_to_use, locator):
    WebDriverWait(driver_to_use, 3).until \
        (expected_conditions.url_to_be(locator))
