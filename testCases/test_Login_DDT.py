import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities import xlUtilities
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    file = ".//TestData//LogData.xlsx"
    logger = LogGen.loggerGen()


    @pytest.mark.vinsd
    def test_DDT_Login(self,setup):

        self.logger.info("********** Verifying Test_002_DDT_Login *********")
        self.logger.info("********** verifying DDT Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lpddt = LoginPage(self.driver)
        self.rows = xlUtilities.getRowCount(self.file, "Sheet1")
        print("The max rows in the sheet are:", self.rows)
        lst = []

        for r in range(2, 6):
            self.username = xlUtilities.readData(self.file, "Sheet1", r, 1)
            self.password = xlUtilities.readData(self.file, "Sheet1", r, 2)
            self.exp = xlUtilities.readData(self.file, "Sheet1", r, 3)

            self.lpddt.setUserName(self.username)
            self.lpddt.setPassword(self.password)
            self.lpddt.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:  # First COMBINATION
                if self.exp == "Pass":
                    self.logger.info("******* DDT Test is Passed **********")
                    self.lpddt.clickLogout()
                    lst.append("Pass")
                elif self.exp == "Fail":  # UR COMPARING WITH UR XL
                    self.logger.error("******* DDT Test is Failed *****")
                    self.lpddt.clickLogout()
                    lst.append("Fail")

            elif act_title != exp_title:  # SECOND COMBINATION
                if self.exp == "Pass":
                    self.logger.error("****** DDT Test is Failed *******")
                    lst.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****** DDT test is passed *******")
                    lst.append("Pass")

        if "Fail" not in lst:
            self.logger.info("******** DDT TEST IS PASSED ********")
            self.driver.close()
            assert True
        else:
            self.logger.info("************* DDT TEST IS FAILED ************")
            self.driver.close()
            assert False

        self.lpddt.clickLogout()
        time.sleep(5)
        self.driver.close()
        self.logger.info("******* DDT TEST IS COMPLETED **********")
        self.logger.info("************ test_002_DDT_Login IS COMPLETED ***********")



