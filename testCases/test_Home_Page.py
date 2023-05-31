

import pytest

from pageObject.Home_Page import HomePage
from utilities.Actions import Actions
from utilities.Base import BaseClass

@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    def test_01_Redirection(self):
        log = self.getLogger()
        log.info("Checking the log")
        actions = Actions(self.driver)
        title = actions.get_title()
        assert "ProtoCommerce" in title

    def test_02_Add_to_Cart(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        prod_list = home_page.get_list_of_products()
        log.info(prod_list)

