import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sys.path.append("C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Orange_HRM")
from utilities.Baseclass import Base


class Login(Base):

    def __init__(self, driver):
        self.driver = driver
        self.Logo = "//img[@src='/web/images/ohrm_branding.png?v=1689053487449']"
        self.Title = ".orangehrm-login-title"
        self.Default_username = "(//p[@class='oxd-text oxd-text--p'])[1]"
        self.Default_password = "(//p[@class='oxd-text oxd-text--p'])[2]"
        self.username_text = "(//label[@class='oxd-label'])[1]"
        self.password_text = "(//label[@class='oxd-label'])[2]"
        self.username_input = "username"
        self.password_input = "password"
        self.Login_button = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
        self.Forget_pwd = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
        self.Dashboard = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"

    def Enter_username(self, Testdata):
        self.driver.find_element(By.NAME, self.username_input).send_keys(Testdata)

    def Enter_password(self, Testdata):
        # self.wait_untill(Locator=self.password_input)
        self.driver.find_element(By.NAME, self.password_input).send_keys(Testdata)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.Login_button).click()
        self.wait_untill(Locator=self.Dashboard)
