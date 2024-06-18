from util import *

class Test_SignIn(BaseTest, unittest.TestCase):

    # Test case 1: Sign in with invalid password, catch the message -> Invalid username or password
    def test_sign_in_invalid_password(self):
        if (self.next is True):
            self.base.beginOfTest_logFormat("test_sign_in_invalid_password")
            self.logger.info("Started Signing In")
            click_sign_in(self.driver, self.logger, self.configInfo)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "invalid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_handler(self.logger, self.configInfo, "Failure. Cannot open the Sign In pop up", e,
                    self.configError["cannot_open_signIn_popup"], "Home")
                execute_next = False
                
            if (execute_next is True):
                try:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Incorrect email or password']")))
                    login_error = self.driver.find_element(By.XPATH, "//label[text()='Incorrect email or password']").text
                    assert (login_error == "Incorrect email or password")
                    self.logger.info("Success. Tested the invalid login attempt.")
                except Exception as e:
                    error_handler(self.logger, self.configInfo, "Failure. Wrong password passed. Broken implementation", e,
                        self.configError["wrong_password_passed"], "Home")

    # Test case 2: Sign in with valid password, verify the icon on the top right, then sign out
    def test_sign_in_valid_password_and_sign_out(self):
        if (self.next is True):
            self.base.beginOfTest_logFormat("test_sign_in_valid_password_and_sign_out")
            self.logger.info("Started Signing In")
            click_sign_in(self.driver, self.logger, self.configInfo)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_handler(self.logger, self.configInfo, "Failure. Cannot open the Sign In pop up", e,
                    self.configError["cannot_open_signIn_popup"], "Home")
                execute_next = False

            if (execute_next is True):
                try:
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@src='/imgs/profile.png']")))
                    self.driver.find_element(By.XPATH, "//img[@src='/imgs/profile.png']").click()
                    self.logger.debug("Clicked the user icon")
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Logout')]")))
                    logout_icon = self.driver.find_element(By.XPATH, "//label[contains(text(),'Logout')]")
                    assert (logout_icon.text == "Logout")
                    self.logger.info("Success. Tested signing in with the valid password.")
                    logout_icon.click()
                    self.logger.debug("Clicked the logout icon")
                    signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
                    assert (signIn_button.is_displayed())
                    self.logger.info("Success. Tested logging out.")
                except Exception as e:
                    error_handler(self.logger, self.configInfo, "Failure. Cannot sign in and log out with valid password. Broken implementation", e,
                        self.configError["cannot_signIn_logOut"], "Home")
