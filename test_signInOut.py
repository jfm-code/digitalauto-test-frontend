from util import *

class Test_SignIn_SignOut(BaseTest, unittest.TestCase):
    def test_SignIn_and_SignOut(self):
        if ((self.next is True) and (self.open_SignIn_popup() is True)):
            self.signIn_invalid_password()
            time.sleep(2)
            self.signIn_valid_password()
            time.sleep(2)
            self.logOut()
            
    def open_SignIn_popup(self):
        self.base.beginOfTest_logFormat("open_SignIn_popup")
        click_sign_in(self.driver, self.logger, self.configInfo)
        canOpen_popUp = False
        try:
            popup = self.driver.find_element(By.TAG_NAME, "form")
            assert (popup.is_displayed())
            canOpen_popUp = True
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot open the Sign In pop up", e,
                self.configError["cannot_open_signIn_popup"], "Home")
        return canOpen_popUp

    def signIn_invalid_password(self):
        self.base.beginOfTest_logFormat("signIn_invalid_password")
        try:
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
            enter_password(self.driver, self.logger, self.configInfo, "invalid", "first_enter")
            submit_sign_in(self.driver, self.logger)
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Incorrect email or password']")))
            login_error = self.driver.find_element(By.XPATH, "//label[text()='Incorrect email or password']").text
            assert (login_error == "Incorrect email or password")
            self.logger.info("Success. Tested the invalid login attempt.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Wrong password passed. Broken implementation", e,
                self.configError["wrong_password_passed"], "Home")

    def signIn_valid_password(self):
        self.base.beginOfTest_logFormat("signIn_valid_password")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='password']").clear()
            enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
            submit_sign_in(self.driver, self.logger)
            user_icon = self.driver.find_element(By.TAG_NAME, "picture")
            assert (user_icon.is_displayed())
            self.logger.info("Success. Tested the valid login attempt.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot sign in with correct password. Broken implementation", e,
                self.configError["cannot_signIn"], "Home")
    
    def logOut(self):
        self.base.beginOfTest_logFormat("logOut")
        try:
            self.driver.find_element(By.TAG_NAME, "picture").click()
            self.logger.debug("Clicked the user icon")
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Logout')]")))
            logout_icon = self.driver.find_element(By.XPATH, "//label[contains(text(),'Logout')]")
            time.sleep(2)
            logout_icon.click()
            self.logger.debug("Clicked the logout icon")
            signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
            assert (signIn_button.is_displayed())
            self.logger.info("Success. Tested logging out.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot log out after signing in.", e,
                self.configError["cannot_logOut"], "Home")