from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.chrome.options import ChromiumOptions


def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browsername")
    print(browser_name)
    global driver
    if browser_name == "chrome":
        option = ChromiumOptions()
        option.add_argument("--headless")
        service_obj = Service(
            "C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Orange_HRM\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=option)
    elif browser_name == "edge":
        service_obj = Service(
            "C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Orange_HRM\\Drivers\\msedgedriver.exe.exe")
        driver = webdriver.Edge(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()
