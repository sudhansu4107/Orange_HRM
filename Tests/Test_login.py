import sys
import time

sys.path.append("C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Orange_HRM")
from utilities.Baseclass import Base
from Pages.Orange_HRM_Loginpage import Login


class Test_login(Base):
    def test_Checklogin(self):
        logs=self.get_logs()
        logs.debug("Test started")
        login_obj = Login(self.driver)
        login_obj.Enter_username("Admin")
        logs.info("User name has enterd.")
        login_obj.Enter_password("admin123")
        logs.info("password has enterd.")
        time.sleep(10)
        logs.debug("sleep for 10 sec")
        login_obj.click_login()
        logs.debug("test completed successfully")

