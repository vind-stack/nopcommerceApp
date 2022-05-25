from selenium.webdriver.common.by import By

class SearchCustomer():
    txtSearchEmail_xpath = "//input[@id='SearchEmail']"
    txtSearchfirstname_xpath = "//input[@id='SearchFirstName']"
    txtSearchlastname_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"
    tableSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSearchEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtSearchEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchEmail_xpath).send_keys(email)

    def setSearchFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtSearchfirstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchfirstname_xpath).send_keys(fname)

    def setSearchLastname(self, lname):
        self.driver.find_element(By.XPATH, self.txtSearchlastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchlastname_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def getNoRows(self):
        rows = self.driver.find_element(By.XPATH, self.tableRows_xpath)
        return rows

    def getNoColumns(self):
        columns = self.driver.find_element(By.XPATH, self.tableColumns_xpath)
        return columns
    
    def searchCustomerEmail(self, email):
        vins = False
        for r in range(1, 7):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                vins = True
                break
        return vins

    def searchCustomerName(self, name):
        flag = False
        for r in range(1, 7):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
