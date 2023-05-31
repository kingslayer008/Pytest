from selenium.webdriver.common.by import By

from utilities.Base import BaseClass
from utilities.Actions import Actions


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver


    product_titles = "//h4[@class='card-title']"

    def get_list_of_products(self):
        newl = []
        prod_list = Actions.get_list_of_elements(self, By.XPATH, HomePage.product_titles)
        for ele in prod_list:
            newl.append(Actions.get_text(self, ele))
        return newl



