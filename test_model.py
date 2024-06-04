from util import *

class Test_Model(BaseTest, unittest.TestCase):
    
    # Test case 1: Not sign in, if "Create New Model" button is visible then fail the test
    def test_noSignIn_newModelButton(self):
        self.base.beginOfTest_logFormat("test_noSignIn_newModelButton")
        if (self.next is True):
            self.logger.info("Started checking the visibility of 'Create New Model' button when not signing in")
            signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
            if (signIn_button.is_displayed()):
                self.logger.debug("User is not signing in")
                self.driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
                self.logger.debug("Clicked the Select Model button")
                try:
                    createModel_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Model')]")
                    assert (not createModel_button.is_displayed())
                    self.logger.info("Successfully tested the case of not seeing the 'Create New Model' button when not signing in")
                except Exception as e:
                    error_message = "Failed to sign in and log out with valid password. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")