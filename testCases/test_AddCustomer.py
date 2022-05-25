import random
import string
import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.add_New_Customer import AddNewCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer():
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggerGen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("********** Test_003_AddCustomer ***********")

        self.logger.info("********** test_Login ***********")
        self.lop = LoginPage(self.driver)
        self.lop.setUserName(self.username)
        self.lop.setPassword(self.password)
        self.lop.clickLogin()
        self.logger.info("********** test_Login is Successfull ***********")

        self.logger.info("********** test_addCustomer ***********")
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNewCustomer()

        self.logger.info("********** providing customer details ***********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Vinayaka")
        self.addcust.setLastName("Dixit")
        self.addcust.setGender("Male")
        self.addcust.setDOB("8/14/1992")
        self.addcust.setCompanyName("MKBS")
        self.addcust.setTaxExempt()
        self.addcust.setNewsLetter("Test store 2")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminContent("This is addCustomer testing")
        self.addcust.clickOnSave()

        self.logger.info("*********** saved the customer details ***********")
        self.logger.info("*********** add customer validation started ***********")

        message = self.driver.find_element(By.TAG_NAME, "body").text
        print(message)

        if "The new customer has been added successfully." in message:
            assert True == True
            self.logger.info("*********** Add customer test is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("*********** Add customer Test is Failed ************")
            assert True == False

        self.lop.clickLogout()
        time.sleep(5)
        self.driver.close()
        self.logger.info("******** Ending of Add customer Test ************")


def random_generator(size= 8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))



