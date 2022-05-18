from BaseApp import BasePage
from selenium.webdriver.common.by import By
from settings import invalid_cell_number, invalid_password


class Locators:
    LOCATOR_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, ".gu")
    LOCATOR_SEARCHING_RESULTS = (By.XPATH, "//div[contains(text(), 'Мандзони А. ')]")
    LOCATOR_BUTTON_CATALOG = (By.XPATH, "//*[@id='ml2_header']/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]")
    LOCATOR_SIDEBAR = (By.ID, "c_sidebar")
    LOCATOR_HELLO_SPB = (By.XPATH, "//a[@href='/goods-from-spb']")
    LOCATOR_CABINET = (By.XPATH, "//*[@id='h_cab']")
    LOCATOR_AUTH_FORM = (By.XPATH, "//*[@href='#auth_tab']")
    LOCATOR_AUTH_LOG_FIELD = (By.XPATH, "//*[@id='auth_form-login-input']")
    LOCATOR_AUTH_PASS_FIELD = (By.XPATH, "//*[@id='auth_form-password-input']")
    LOCATOR_AUTH_BUTTON_ENTER = (By.XPATH, "//*[@class='Uf Tt qz GJ']")
    LOCATOR_BUTTON_HOMEPAGE = (By.CSS_SELECTOR, ".Bjb")
    LOCATOR_INVALID_LOG_OR_PASS = (By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(Locators.LOCATOR_SEARCH_BUTTON, time=2).click()

    def check_results(self):
        results = self.find_elements(Locators.LOCATOR_SEARCHING_RESULTS, time=2)
        return results

    def click_homepage(self):
        return self.find_element(Locators.LOCATOR_BUTTON_HOMEPAGE, time=2).click()

    def click_on_the_catalog_button(self):
        return self.find_element(Locators.LOCATOR_BUTTON_CATALOG, time=2).click()

    def check_sidebar(self):
        return self.find_element(Locators.LOCATOR_SIDEBAR, time=2)

    def click_hello_spb(self):
        return self.find_element(Locators.LOCATOR_HELLO_SPB, time=2).click()

    def click_cabinet(self):
        return self.find_element(Locators.LOCATOR_CABINET, time=2).click()

    def check_auth(self):
        return self.find_element(Locators.LOCATOR_AUTH_FORM, time=2)

    def check_auth_log_field(self):
        return self.find_element(Locators.LOCATOR_AUTH_LOG_FIELD, time=2)

    def check_auth_pass_field(self):
        return self.find_element(Locators.LOCATOR_AUTH_PASS_FIELD, time=2)

    def check_auth_button_enter(self):
        return self.find_element(Locators.LOCATOR_AUTH_BUTTON_ENTER, time=2)

    def enter_log(self):
        log_field = self.check_auth_log_field().click()
        log_field.send_keys(keys=invalid_cell_number)
        return log_field

    def enter_pass(self):
        pass_field = self.check_auth_pass_field().click()
        pass_field.send_keys(keys=invalid_password)
        return pass_field

    def click_auth_button_enter(self):
        return self.find_element(Locators.LOCATOR_AUTH_BUTTON_ENTER, time=2).click()

    def check_response_invalid_auth(self):
        return self.find_element(Locators.LOCATOR_INVALID_LOG_OR_PASS, time=2)
