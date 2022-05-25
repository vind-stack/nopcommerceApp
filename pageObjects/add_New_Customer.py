import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddNewCustomer():
    lnkCustomers_Menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_MenuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAdd_New_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdGenderMale_id = "Gender_Male"
    rdGenderFemale_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkbox_taxExempt_id = "IsTaxExempt"
    lstItemNewsLetter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    lstItemYourstore_xpath = "//li[normalize-space()='Your store name']"
    lstItemTeststore2_xpath = "//li[normalize-space()='Test store 2']"
    txtCustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstAdministrators_xpath = "//span[normalize-space()='Administrators']"
    lstForumModerators_xpath = "//span[normalize-space()='Forum Moderators']"
    lstGuests_xpath = "//li[contains(text(),'Guests')]"
    lstRegistered_xpath = "//span[contains(text(),'Administrators')]"
    lstVendors_xpath = "//span[normalize-space()='Vendors']"
    drpManagerofVendor_id = "VendorId"
    txtAdmionContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_Menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_MenuItem_xpath).click()

    def clickOnAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.btnAdd_New_xpath).click()
        time.sleep(5)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdGenderMale_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdGenderFemale_id).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, cmpname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cmpname)

    def setTaxExempt(self):
        self.driver.find_element(By.ID, self.chkbox_taxExempt_id).click()

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.lstItemNewsLetter_xpath).click()
        if newsletter == "Your store name":
            newslet = self.driver.find_element(By.XPATH, self.lstItemYourstore_xpath)
        elif newsletter == "Test store 2":
            newslet = self.driver.find_element(By.XPATH, self.lstItemTeststore2_xpath)
        else:
            newslet = self.driver.find_element(By.XPATH, self.lstItemYourstore_xpath)

        self.driver.execute_script("arguments[0].click();", newslet)
        time.sleep(5)


    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstAdministrators_xpath)
        elif role == "Guests":
            time.sleep(5)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstGuests_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstVendors_xpath)
            time.sleep(5)

        self.driver.execute_script("arguments[0].click();", self.listitem)


    def setManagerOfVendor(self, value):
        drp =Select(self.driver.find_element(By.ID, self.drpManagerofVendor_id))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdmionContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()




