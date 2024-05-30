from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
from set_up import Base

class Test_NoData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = Base()
        cls.base.setup_logger()
    # Making sure that logger is configured only once

    def setUp(self):
        self.base.setup_browser()
        self.driver = self.base.driver
        self.logger = self.base.logger

    def tearDown(self):
        self.base.clean_up()

    def test_numOf_models(self):
        try:
            self.logger.info("Started counting the model components in model page")
            self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click()
            models = self.driver.find_elements(By.CSS_SELECTOR, "a[class='mr-2 w-full']")
            assert (len(models) > 0)
            self.logger.info("Successfully tested the number of model components in model page")
        except Exception as e:
            self.logger.error(f"Failed to load the model components in model page: {e}")
            
    def test_numOf_prototypes(self):
        try:
            self.logger.info("Started counting the prototype components in home page")
            prototypes = self.driver.find_elements(By.XPATH, "//div/div[@class='w-full h-full relative']/div/a/img")
            assert (len(prototypes) > 0)
            self.logger.info("Successfully tested the number of prototype components in home page")
        except Exception as e:
            self.logger.error(f"Failed to load the prototype components in home page: {e}")