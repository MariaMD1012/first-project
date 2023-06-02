from conftest import *

from utils import *


class TestRegistration:
    def test_register_new_user_true(self, driver):
        driver.get(link + 'register')
        driver.find_element(*AuthorizationForm.login).send_keys(fake_login)
        driver.find_element(*AuthorizationForm.email).send_keys(fake_email)
        driver.find_element(*AuthorizationForm.password).send_keys(fake_password)
        driver.find_element(*AuthorizationForm.register_button).click()
        wait_url(driver, link + 'login')
        current_url = driver.current_url
        assert current_url == link + 'login'

    def test_register_new_user_incorrect_password(self, driver):
        driver.get(link + 'register')
        driver.find_element(*AuthorizationForm.login).send_keys(fake_login)
        driver.find_element(*AuthorizationForm.email).send_keys(fake_email)
        driver.find_element(*AuthorizationForm.password).send_keys(incorrect_password)
        driver.find_element(*AuthorizationForm.register_button).click()
        error_tex = driver.find_element(*AuthorizationForm.password_fail).text
        assert error_tex == 'Некорректный пароль'
