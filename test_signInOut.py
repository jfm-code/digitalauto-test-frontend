from util import *

class Test_SignIn(BaseTest, unittest.TestCase):

    # Test case 1: Sign in with invalid password, catch the message -> Invalid username or password
    def test_sign_in_invalid_password(self):
        self.base.beginOfTest_logFormat("test_sign_in_invalid_password")
        if (self.next is True):
            self.logger.info("Started Signing In")
            click_sign_in(self.driver, self.logger, self.configInfo)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "invalid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_message = "Failure. Cannot open the Sign In pop up"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
                email_content = self.configError["cannot_open_register_popup"]
                email_subject = "Error occured in the Home page"
                send_email(self.configInfo, email_content, email_subject)
                execute_next = False
                
            if (execute_next is True):
                try:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Incorrect email or password']")))
                    login_error = self.driver.find_element(By.XPATH, "//label[text()='Incorrect email or password']").text
                    assert (login_error == "Incorrect email or password")
                    self.logger.info("Success. Tested the invalid login attempt.")
                except Exception as e:
                    error_message = "Failure. Wrong password passed. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    #email_content = "<!DOCTYPE html><html lang='en'><body><p>Wrong password passed. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email but wrong password.</li><li>Click Sign In to see if the wrong password is accepted</li></ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EWrong%20password%20passed.%20Broken%20implementation.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%3C%2Fli%3E%3Cli%3EEnter%20the%20correct%20email%20but%20wrong%20password.%3C%2Fli%3E%3Cli%3EClick%20Sign%20In%20to%20see%20if%20the%20wrong%20password%20is%20accepted%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Home page"
                    send_email(self.configInfo, email_content, email_subject)

    # Test case 2: Sign in with valid password, verify the icon on the top right, then sign out
    def test_sign_in_valid_password_and_sign_out(self):
        self.base.beginOfTest_logFormat("test_sign_in_valid_password_and_sign_out")
        if (self.next is True):
            self.logger.info("Started Signing In")
            click_sign_in(self.driver, self.logger, self.configInfo)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_message = "Failure. Cannot open the Sign In pop up"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20open%20the%20Sign%20In%20pop%20up.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20the%20Sign%20In%20pop%20up%20can%20be%20loaded.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Home page"
                send_email(self.configInfo, email_content, email_subject)
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
                    error_message = "Failure. Cannot sign in and log out with valid password. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to sign in and log out with valid password. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email and correct password.</li><li>Click Sign In to see if the correct password is accepted</li><li>Then click log out button</li></ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20sign%20in%20and%20log%20out%20with%20valid%20password.%20Broken%20implementation.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%3C%2Fli%3E%3Cli%3EEnter%20the%20correct%20email%20and%20correct%20password.%3C%2Fli%3E%3Cli%3EClick%20Sign%20In%20to%20see%20if%20the%20correct%20password%20is%20accepted%3C%2Fli%3E%3Cli%3EThen%20click%20log%20out%20button%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Home page"
                    send_email(self.configInfo, email_content, email_subject)
