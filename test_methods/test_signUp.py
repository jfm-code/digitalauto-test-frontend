from setup_methods.util import *

class Test_SignUp(BaseTest, unittest.TestCase):
    
    def test_SignUp(self):
        if ((self.next is True) and (self.open_SignUp_popup() is True)):
            self.signUp_fail_lackOneField()
            time.sleep(2)
            self.signUp_fail_existingEmail()
            time.sleep(2)
            self.signUp_fail_confirmPassword()
            time.sleep(2)
            self.signUp_fail_password_notLongEnough()
            time.sleep(2)
            self.signUp_success()
            
            delete_testing_object("user", self.driver, self.logger, self.configInfo)

    def open_SignUp_popup(self):
        self.base.beginOfTest_logFormat("open_SignUp_popup")
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
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
            self.driver.find_element(By.XPATH, "//input[@name='fullName']").send_keys(self.configInfo["signUp_name"])
            enter_password(self.driver, self.configInfo, "valid", "first_enter")
            enter_password(self.driver, self.configInfo, "valid", "re_enter")
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
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
            self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.configInfo["signIn_email"])
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
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
            enter_password(self.driver, self.configInfo, "invalid", "re_enter")
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
            expected_message = '"password" and "confirm password" must be the same'
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
            message = self.driver.find_element(By.XPATH, f"//label[text()='{expected_message}']").text
            assert (message == expected_message)
            self.logger.info("Success. Tested the case of different entered password and confirmed password.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Confirm password was different from entered password. Broken implementation", e, "", "")

    def signUp_fail_password_notLongEnough(self):
        self.base.beginOfTest_logFormat("signUp_fail_password_notLongEnough")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='password']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("pass")
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("pass")
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
            expected_message = 'password must be at least 8 characters'
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
            message = self.driver.find_element(By.XPATH, f"//label[text()='{expected_message}']").text
            assert (message == expected_message)
            self.logger.info("Success. Tested the case of too short password entered.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Too short password passed. Broken implementation.", e, "", "")

    def signUp_success(self):
        self.base.beginOfTest_logFormat("signUp_success")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='email']").clear()
            self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.configInfo["signUp_email"])
            self.driver.find_element(By.XPATH, "//input[@name='password']").clear()
            enter_password(self.driver, self.configInfo, "valid", "first_enter")
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").clear()
            enter_password(self.driver, self.configInfo, "valid", "re_enter")
            self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
            time.sleep(5)
            user_icon = self.driver.find_element(By.TAG_NAME, "picture")
            assert (user_icon.is_displayed())
            self.logger.debug("Saw the user icon")
            self.logger.info("Success. Tested registering a new account.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot register a new account.", e, "", "")
            self.driver.get_screenshot_as_file("images\\screenshot-failed-register.png")
