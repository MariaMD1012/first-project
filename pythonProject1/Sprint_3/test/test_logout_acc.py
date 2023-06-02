from conftest import *
from utils import *


class TestLogout:
    def test_click_link_constructor_true(self, driver):
        driver.get(link)
        driver.find_element(*AppHeader.link_acc).click()
        wait_el(driver, AuthorizationForm.title_login_page)
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        driver.find_element(*AppHeader.link_acc).click()
        wait_el(driver, ProfilePage.button_exit)
        driver.find_element(*ProfilePage.button_exit).click()
        wait_el(driver, AuthorizationForm.title_login_page)
        current_url = driver.current_url

        assert current_url == link + 'login'
