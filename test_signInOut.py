from util import *

class Test_SignIn(BaseTest, unittest.TestCase):

    # Test case 1: Sign in with invalid password, catch the message -> Invalid username or password
    def test_sign_in_invalid_password(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.config, self.config["signIn_email"])
                enter_password(self.driver, self.logger, self.config, "invalid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_message = "Failed to open the Sign In pop up"
                self.logger.error(f"{error_message}: {e}")
                email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
                email_subject = "Error occured in the Home page"
                send_email(self.config, email_content, email_subject)
                execute_next = False
                
            if (execute_next is True):
                try:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Incorrect email or password']")))
                    login_error = self.driver.find_element(By.XPATH, "//label[text()='Incorrect email or password']").text
                    assert (login_error == "Incorrect email or password")
                    self.logger.info("Successfully tested the invalid login attempt.")
                except Exception as e:
                    error_message = "Wrong password passed. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = "<!DOCTYPE html><html lang='en'><body><p>Wrong password passed. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email but wrong password.</li><li>Click Sign In to see if the wrong password is accepted</li></ol></p></body></html>"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)

    # Test case 2: Sign in with valid password, verify the icon on the top right, then sign out
    def test_sign_in_valid_password_and_sign_out(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            execute_next = True
            try:
                enter_email(self.driver, self.logger, self.config, self.config["signIn_email"])
                enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
                submit_sign_in(self.driver, self.logger)
            except Exception as e:
                error_message = "Failed to open the Sign In pop up"
                self.logger.error(f"{error_message}: {e}")
                email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
                email_subject = "Error occured in the Home page"
                send_email(self.config, email_content, email_subject)
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
                    self.logger.info("Successfully signed in with the valid password.")
                    logout_icon.click()
                    self.logger.debug("Clicked the logout icon")
                    signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
                    assert (signIn_button.is_displayed())
                    self.logger.info("Successfully logged out.")
                except Exception as e:
                    error_message = "Failed to sign in and log out with valid password. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to sign in and log out with valid password. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email and correct password.</li><li>Click Sign In to see if the correct password is accepted</li><li>Then click log out button</li></ol></p></body></html>"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)