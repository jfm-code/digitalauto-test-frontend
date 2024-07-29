from util import *

class Test_NoData(BaseTest, unittest.TestCase):
    def test_no_data(self):
        if (self.next is True):
            # self.count_numOf_prototypes()
            self.count_numOf_models()

    def count_numOf_models(self):
        self.base.beginOfTest_logFormat("count_numOf_models")
        try:
            self.driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
            models = self.driver.find_elements(By.XPATH, "//div/a/div")
            assert (len(models) > 0)
            self.logger.info("Success. Tested the number of model components in model page")
        except Exception as e:
            error_handler("critical", self.logger, self.configInfo, "Failure. Cannot load the model components in model page", e,
                self.configError["cannotLoad_model"], "Model")
    
    def count_numOf_prototypes(self):
        self.base.beginOfTest_logFormat("count_numOf_prototypes")
        try:
            prototypes = self.driver.find_elements(By.XPATH, "//div/a/div")
            assert (len(prototypes) > 0)
            self.logger.info("Success. Tested the number of prototype components in home page")
        except Exception as e:
            error_handler("critical", self.logger, self.configInfo, "Failure. Cannot load the prototype components in home page", e,
                self.configError["cannotLoad_prototype"], "Home")
                