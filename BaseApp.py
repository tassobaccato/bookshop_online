from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.bookvoed.ru/"
        self.current_url = ''
        self.page_url = "https://www.bookvoed.ru/goods-from-spb"
        self.keys = ''

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def current_page(self):
        return self.current_url

    def go_to_page(self):
        return self.driver.get(self.page_url)

    def send_keys(self, keys):
        return self.send_keys(keys)

