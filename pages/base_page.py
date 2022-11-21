from Bio.Phylo._cdao_owl import element
from fontTools.subset.svg import xpath
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver) -> object:
        self.driver = driver

    def field_send_keys(self, selector: object, value: object, locator_type: object = By.XPATH) -> object:
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector: object, selector_type: object = By.XPATH) -> object:
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

        element - driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clicable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((locator_type, locator)))
