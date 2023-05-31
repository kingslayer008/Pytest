from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Base import BaseClass


class Actions(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def wait_and_click(self, By, path):
        element = self.WebDriverWaitUntilClickable(By, path)
        try:
            element.click()
        except StaleElementReferenceException:
            element = self.WebDriverWaitUntilClickable(By, path)
            element.click()

    def get_list_of_elements(self, By, path):
        elements = self.driver.find_elements(By, path)
        return elements

    def get_text(self, ele):
        return ele.text

    def WebDriverWaitUntilClickable(self, By, path):

        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By, path)))
