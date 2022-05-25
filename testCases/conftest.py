import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(): # setup(browser)  ==> Need to pass it inside
    serv_obj = Service("C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    # if browser == "chrome":
    #     serv_obj = Service("C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
    #     driver = webdriver.Chrome(service=serv_obj)
    #     print("Launching Chrome Browser")
    # elif browser == "firefox":
    #     serv_obj = Service("C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
    #     driver = webdriver.Firefox(service=serv_obj)  # FIREFOX DRIVER IS NEEDED
    return driver

# # THIS WILL GET THE VALUES FROM CLI/HOOKS (WILL RECOGNIZE WHICH BROWESER HAS GIVEN CMDPRMT)
# def pytest_adoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):            # THIUS WILL RETURN THE BROWSER VALUE TO SETUP METHOD
#     return request.config.getoption("--browser")

########## Pytest HTML Report #############
# its a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Vinayaka"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)




