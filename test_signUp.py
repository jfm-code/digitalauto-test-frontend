from util import *

class Test_SignUp(BaseTest, unittest.TestCase):
    
    def test_SignUp(self):
        if ((self.next is True) and (self.open_SignUp_popup() is True)):
            self.signUp_fail_lackOneField()
            time.sleep(2)
            self.signUp_fail_existingEmail()
            time.sleep(2)
            self.signUp_fail_confirmPassword()
            time.sleep(2)
            self.signUp_success()
            
            delete_testing_object("account", self.driver, self.logger, self.configInfo)

    def open_SignUp_popup(self):
        self.base.beginOfTest_logFormat("open_SignUp_popup")
        try:
            click_sign_in(self.driver, self.logger, self.configInfo)
            click_register(self.driver, self.logger)
            popup = self.driver.find_element(By.XPATH, "//form/label[text()='Register']")
            assert (popup.is_displayed())
            canOpen_popUp = True
            self.logger.info("Success. Can open the register popup.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot open the Register pop up", e, "", "")
        return canOpen_popUp
    
    def signUp_fail_lackOneField(self):
        self.base.beginOfTest_logFormat("signUp_fail_lackOneField")
        try:
            enter_name(self.driver, self.logger, self.configInfo)
            enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
            enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            click_register(self.driver, self.logger)
            expected_message = '"email" is required'
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
            message = self.driver.find_element(By.XPATH,f"//label[text()='{expected_message}']").text
            assert (message == expected_message)
            self.logger.info("Success. Tested the case of not entered the email field.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Empty email field but can still registered. Broken implementation", e, "", "")
            
    def signUp_fail_existingEmail(self):
        self.base.beginOfTest_logFormat("signUp_fail_existingEmail")
        try:
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
            click_register(self.driver, self.logger)
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email already taken']")))
            message = self.driver.find_element(By.XPATH, "//label[text()='Email already taken']").text
            assert (message == "Email already taken")
            self.logger.info("Success. Tested the case of using existing email.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Existing email was used to sign up the account. Broken implementation", e, "", "")

    def signUp_fail_confirmPassword(self):
        self.base.beginOfTest_logFormat("signUp_fail_confirmPassword")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").clear()
            enter_password(self.driver, self.logger, self.configInfo, "invalid", "re_enter")
            click_register(self.driver, self.logger)
            expected_message = '"password" and "confirm password" must be the same'
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
            message = self.driver.find_element(By.XPATH, f"//label[text()='{expected_message}']").text
            assert (message == expected_message)
            self.logger.info("Success. Tested the case of different entered password and confirmed password.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Confirm password was different from entered password. Broken implementation", e, "", "")

    def signUp_success(self):
        self.base.beginOfTest_logFormat("signUp_success")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='email']").clear()
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signUp_email"])
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").clear()
            enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            click_register(self.driver, self.logger)
            wait = WebDriverWait(self.driver, 4)
            wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "picture")))
            user_icon = self.driver.find_element(By.TAG_NAME, "picture")
            assert (user_icon.is_displayed())
            self.logger.debug("Saw the user icon")
            self.logger.info("Success. Tested registering a new account.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot register a new account.", e, "", "")
            self.driver.get_screenshot_as_file("screenshot-failed-register.png")
                    
    # Test case 5: Enter all info but invalid email address, catch the message -> this is failing
    
    # Test case 6: Password has at least 8 characters -> is there any other conditions for password?
