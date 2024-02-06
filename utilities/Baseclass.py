import sys
sys.path.append("C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Orange_HRM")
import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging


@pytest.mark.usefixtures('setup')
class Base:

    def get_logs(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filehandler = logging.FileHandler(
            "Report/Logs.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(filehandler)
        return logger

    def wait_untill(self, Locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, Locator)))
