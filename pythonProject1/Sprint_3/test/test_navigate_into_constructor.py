from conftest import *


class TestConstructor:
    def test_click_link_constructor_true(self, driver):
        driver.get(link + 'login')
        driver.find_element(*AppHeader.link_constructor).click()
        current_url = driver.current_url
        assert current_url == link
    def test_click_link_logo_true(self, driver):
        driver.get(link + 'login')
        driver.find_element(*AppHeader.logo).click()
        current_url = driver.current_url
        assert current_url == link
    def test_section_check_bread_true(self, driver):
        driver.get(link)
        bread_element = driver.find_element(*MainPage.bread_element)
        current_element = driver.find_element(*MainPage.active_section)
        assert bread_element.text == current_element.text
    def test_section_check_sauces_true(self, driver):
        driver.get(link)
        sauce_element = driver.find_element(*MainPage.sauce_element)
        sauce_element.click()
        current_element = driver.find_element(*MainPage.active_section)
        assert sauce_element.text == current_element.text
    def test_section_check_fillings_true(self, driver):
        driver.get(link)
        filling_element = driver.find_element(*MainPage.filling_element)
        filling_element.click()
        current_element = driver.find_element(*MainPage.active_section)
        assert filling_element.text == current_element.text
