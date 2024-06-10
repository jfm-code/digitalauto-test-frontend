from util import *

class Test_NoData(BaseTest, unittest.TestCase):

    # Test Case 1: Count and make sure the number of models in model page is greater than 0
    def test_numOf_models(self):
        if (self.next is True):
            try:
                self.logger.info("Started counting the model components in model page")
                self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click()
                self.logger.debug("Clicked the Select Model button")
                models = self.driver.find_elements(By.CSS_SELECTOR, "a[class='mr-2 w-full']")
                assert (len(models) > 0)
                self.logger.info("Success. Tested the number of model components in model page")
            except Exception as e:
                error_message = "Failure. Cannot load the model components in model page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["cannotLoad_model"]
                email_subject = "Error occured in the Select Vehicle Models page"
                send_email(self.configInfo, email_content, email_subject)
    
    # Test Case 2: Count and make sure the number of prototypes in home page is greater than 0
    def test_numOf_prototypes(self):
        if (self.next is True):
            try:
                self.logger.info("Started counting the prototype components in home page")
                prototypes = self.driver.find_elements(By.XPATH, "//a/div")
                assert (len(prototypes) > 0)
                self.logger.info("Success. Tested the number of prototype components in home page")
            except Exception as e:
                error_message = "Failure. Cannot load the prototype components in home page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["cannotLoad_prototype"]
                email_subject = "Error occured in the Home page"
                send_email(self.configInfo, email_content, email_subject)

    
    # Test Case 3: Count and make sure the number of red pins in model page is greater than 0
    def test_redPin_exist(self):
        if (self.next is True):
            try:
                self.logger.info("Started counting the number of pins")
                self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click()
                self.logger.debug("Clicked the Select Model button")
                self.driver.find_element(By.CSS_SELECTOR, "img[src='https://firebasestorage.googleapis.com/v0/b/digital-auto.appspot.com/o/media%2FE-Car_Full_Vehicle.png?alt=media&token=9c9d4cb4-fee0-42e3-bbb1-7feaa407cc8e']").click()
                self.logger.debug("Clicked the ACME Car (EV) v0.1 Model")
                self.driver.find_element(By.XPATH, "//div/div[text()='Vehicle APIs']").click()
                self.logger.debug("Clicked the Vehicle APIs button")
                hidden_element = self.driver.find_element(By.XPATH, "//span[text()='7']")
                hidden_text = self.driver.execute_script("return arguments[0].textContent;", hidden_element)
                assert (hidden_text == "7")
                self.logger.info("Success tested the number of pins")
            except:
                error_message = "Failure. Cannot load the red pins on the canvas"
                self.logger.error(error_message)
                email_content = self.configError["cannotLoad_redPins"]
                email_subject = "Error occured in the Vehicle APIs page"
                send_email(self.configInfo, email_content, email_subject)
                