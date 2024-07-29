from util import *

class Test_Model(BaseTest, unittest.TestCase):
    def test_wishlistAPI_functionalities(self):
        if (self.next is True):
            sign_in(self.driver, self.configInfo)
            time.sleep(2)
            create_new_model(self.driver, "Automation Test Model")
            self.create_delete_wishlist_API()
            self.use_API_filter()
            while ("api" in self.driver.current_url):
                self.driver.back()
            delete_testing_object("model", self.driver, self.logger, self.configInfo)

            
    def create_delete_wishlist_API(self):
        self.base.beginOfTest_logFormat("create_delete_wishlist_API")
        self.driver.find_element(By.XPATH, "//div[text()='Vehicle APIs']").click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//button[contains(., 'Add Wishlist API')]").click()
            self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Vehicle")
            object = self.driver.find_element(By.XPATH, "//label[contains(text(),'API name must start with')]")
            assert (object.text == 'API name must start with "Vehicle."')   
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(".AutomationTest")
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
            time.sleep(2)
            self.driver.find_element(By.TAG_NAME, "input").send_keys("Vehicle.Automation")
            self.driver.find_element(By.XPATH, "//label[text()='Vehicle.AutomationTest']").click()
            self.logger.info("Success. Created successfully a wishlist API.")
        except Exception as e:
            error_handler("error", self.logger, self.configInfo, "Failure. Cannot create a wishlist API.", e, "", "")
        
        self.create_delete_discussion()
        
        try:
            self.driver.find_element(By.XPATH, "//div[text()='Delete Wishlist API']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
            self.logger.info("Success. Deleted successfully a wishlist API.")
        except Exception as e:
            error_handler("warning", self.logger, self.configInfo, "Failure. Cannot delete a wishlist API.", e, "", "")
        
    def create_delete_discussion(self):
        self.base.beginOfTest_logFormat("create_delete_discussion")
        try:
            self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Automation Test Discussion")
            self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
            time.sleep(2)
            object = self.driver.find_element(By.XPATH, "//div[@class='whitespace-pre-wrap da-label-small max-h-[200px] overflow-y-auto']")
            assert (object.text == "Automation Test Discussion")
            self.logger.info("Success. Created successfully a discussion.")
        except Exception as e:
            error_handler("warning", self.logger, self.configInfo, "Failure. Cannot create a discussion.", e, "", "")
            
        try:
            self.driver.find_element(By.XPATH, "//div[@class='inline-flex']/span/button[@class='da-btn da-btn-plain da-btn-sm']").click()
            self.driver.find_element(By.XPATH, "//button[text()=' Delete']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
            time.sleep(2)
            self.logger.info("Success. Deleted successfully a discussion.")
        except Exception as e:
            error_handler("warning", self.logger, self.configInfo, "Failure. Cannot delete a discussion.", e, "", "")
            
    def use_API_filter(self):
        self.base.beginOfTest_logFormat("use_API_filter")
        try:
            for _ in range(20):
                self.driver.find_element(By.TAG_NAME, "input").send_keys(Keys.BACK_SPACE)
            self.driver.find_element(By.TAG_NAME, "input").send_keys("Vehicle.Body")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']").click()
            self.driver.find_element(By.XPATH, "//span[text()='Branch']").click()
            self.driver.find_element(By.XPATH, "//span[text()='Actuator']").click()
            self.driver.find_element(By.XPATH, "//span[text()='Attribute']").click()
            numOf_sensors = self.driver.find_elements(By.XPATH, "//label[text()='sensor']")
            assert (len(numOf_sensors) > 0)
            self.logger.info("Success. The API filter is working properly.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. The API filter is not working properly.", e, "", "")
        time.sleep(3)
        
        try:
            self.driver.find_element(By.XPATH, "//label[text()='COVESA VSS 4.1']").click()
            self.driver.find_element(By.XPATH, "//span[text()='Branch']")
            error_handler("warning", self.logger, "", "Failure. Cannot close the API popup filter when clicking outside the popup.", e, "", "")
        except Exception as e:
            self.logger.info("Success. Closed successfully the API popup filter when clicking outside the popup.")