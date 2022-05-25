import pytest

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggerGen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********* Test_001_Login *********")
        self.logger.info("******* verifying home page title ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** HomepageTitle test is Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage.PNG")
            self.driver.close()
            self.logger.info("*********** HomepageTitle test is Failed *********")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("********** verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lip = LoginPage(self.driver)
        self.lip.setUserName(self.username)
        self.lip.setPassword(self.password)
        self.lip.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********* Login Test is Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.PNG")
            self.driver.close()
            self.logger.error("********** Login Test is Failed *******")
            assert False
