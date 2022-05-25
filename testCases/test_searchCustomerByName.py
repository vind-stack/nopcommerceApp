import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.add_New_Customer import AddNewCustomer
from pageObjects.searchCustomer import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_SearchCustomerByName():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggerGen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********* Test_005_SearchCustomerByName ***********")
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

        self.logger.info("******** Search Customer by Name **********")
        self.srchcust = SearchCustomer(self.driver)
        self.srchcust.setSearchFirstname("James")
        self.srchcust.setSearchLastname("Pan")
        self.srchcust.clickSearch()
        time.sleep(5)
        self.logger.info("******** table validation **********")
        namestatus = self.srchcust.searchCustomerName("James Pan")
        assert True == namestatus
        self.logger.info("******** Customer search by Name is completed **********")
        self.lop.clickLogout()
        time.sleep(5)
        self.driver.close()













