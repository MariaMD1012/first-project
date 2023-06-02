from conftest import *
from utils import *


class TestNavigateToPersonalAccount:
    def test_navigate_to_pesronal_account_true(self, driver):
        driver.get(link)
        driver.find_element(*AppHeader.link_acc).click()
        wait_el(driver, AuthorizationForm.title_login_page)
        driver.find_element(*AuthorizationForm.email).send_keys(email)
        driver.find_element(*AuthorizationForm.password).send_keys(password)
        driver.find_element(*AuthorizationForm.button_login).click()
        wait_el(driver, MainPage.title_main_page)
        driver.find_element(*AppHeader.link_acc).click()
        current_url = driver.current_url
        assert current_url == link + 'account'
