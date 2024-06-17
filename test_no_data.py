from util import *

class Test_NoData(BaseTest, unittest.TestCase):
    def test_no_data(self):
        if (self.next is True):
            self.count_numOf_prototypes()
            self.count_numOf_models()

    def count_numOf_models(self):
        self.base.beginOfTest_logFormat("count_numOf_models")
        try:
            click_select_model(self.driver, self.logger)
            models = self.driver.find_elements(By.XPATH, "//div/a/div")
            assert (len(models) > 0)
            self.logger.info("Success. Tested the number of model components in model page")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot load the model components in model page", e,
                self.configError["cannotLoad_model"], "Model")
    
    def count_numOf_prototypes(self):
        self.base.beginOfTest_logFormat("count_numOf_prototypes")
        try:
            prototypes = self.driver.find_elements(By.XPATH, "//div/a/div")
            assert (len(prototypes) > 0)
            self.logger.info("Success. Tested the number of prototype components in home page")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot load the prototype components in home page", e,
                self.configError["cannotLoad_prototype"], "Home")
    
    # def count_numOf_redPins(self):
    #     try:
    #         self.logger.info("Started counting the number of pins")
    #         self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click()
    #         self.logger.debug("Clicked the Select Model button")
    #         self.driver.find_element(By.CSS_SELECTOR, "img[src='https://firebasestorage.googleapis.com/v0/b/digital-auto.appspot.com/o/media%2FE-Car_Full_Vehicle.png?alt=media&token=9c9d4cb4-fee0-42e3-bbb1-7feaa407cc8e']").click()
    #         self.logger.debug("Clicked the ACME Car (EV) v0.1 Model")
    #         self.driver.find_element(By.XPATH, "//div/div[text()='Vehicle APIs']").click()
    #         self.logger.debug("Clicked the Vehicle APIs button")
    #         hidden_element = self.driver.find_element(By.XPATH, "//span[text()='7']")
    #         hidden_text = self.driver.execute_script("return arguments[0].textContent;", hidden_element)
    #         assert (hidden_text == "7")
    #         self.logger.info("Success tested the number of pins")
    #     except Exception as e:
    #         error_handler(self.logger, self.configInfo, "Failure. Cannot load the red pins on the canvas", e,
    #             self.configError["cannotLoad_redPins"], "Vehicle APIs")
                