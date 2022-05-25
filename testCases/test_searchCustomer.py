import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.add_New_Customer import AddNewCustomer
from pageObjects.searchCustomer import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggerGen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********* Test_004_SearchCustomerByEmail ***********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger.info("******** Log in **********")
        self.lop = LoginPage(self.driver)
        self.lop.setUserName(self.username)
        self.lop.setPassword(self.password)
        self.lop.clickLogin()
        self.logger.info("******** Login Is Successfull **********")

        self.logger.info("******** Customer Menu and Item **********")
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("******** Search Customer by Email **********")
        self.srchcust = SearchCustomer(self.driver)
        self.srchcust.setSearchEmail("victoria_victoria@nopCommerce.com")
        self.srchcust.clickSearch()
        time.sleep(5)
        self.srchcust.getNoRows()
        self.logger.info("******** table validation **********")
        status = self.srchcust.searchCustomerEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******** Customer search by Email is completed **********")
        self.lop.clickLogout()
        time.sleep(5)
        self.driver.close()













