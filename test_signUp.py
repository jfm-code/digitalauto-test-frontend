from util import *

class Test_SignUp(BaseTest, unittest.TestCase):

    # # Test case 1: Enter all info and sign up successfully
    # def test_SignUp_successfully(self):
    #     if (self.next is True):
    #         click_sign_in(self.driver, self.logger, self.config)
    #         click_register(self.driver, self.logger)
    #         execute_next = True
    #         try:
    #             enter_name(self.driver, self.logger, self.config)
    #             enter_email(self.driver, self.logger, self.config, self.config["signUp_email"])
    #             enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
    #             enter_password(self.driver, self.logger, self.config, "valid", "re_enter")
    #         except Exception as e:
    #             error_message = "Failed to open the Register pop up"
    #             self.logger.error(f"{error_message}: {e}")
    #             email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
    #             email_subject = "Error occured in the Home page"
    #             send_email(self.config, email_content, email_subject)
    #             execute_next = False
            
    #         if (execute_next is True):
    #             try:
    #                 click_register(self.driver, self.logger)
    #                 user_icon = self.driver.find_element(By.XPATH, "//img[@src='/imgs/profile.png']")
    #                 assert (user_icon.is_displayed())
    #                 self.logger.info("Successfully signed up an account.")
    #             except Exception as e:
    #                 error_message = "Failed to register an account"
    #                 self.logger.critical(f"{error_message}: {e}")
    #                 email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to register an account.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields</li><li>Click Register button to create an account</li><</ol></p></body></html>"
    #                 email_subject = "Error occured in the Home page"
    #                 send_email(self.config, email_content, email_subject)
                    
    # # Test case 2: Enter all info but using existing email, sign up failed and catch the message -> Email taken
    # def test_signUp_existingEmail(self):
    #     if (self.next is True):
    #         click_sign_in(self.driver, self.logger, self.config)
    #         click_register(self.driver, self.logger)
    #         execute_next = True
    #         try:
    #             enter_name(self.driver, self.logger, self.config)
    #             enter_email(self.driver, self.logger, self.config, self.config["signIn_email"])
    #             enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
    #             enter_password(self.driver, self.logger, self.config, "valid", "re_enter")
    #         except Exception as e:
    #             error_message = "Failed to open the Register pop up"
    #             self.logger.error(f"{error_message}: {e}")
    #             email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
    #             email_subject = "Error occured in the Home page"
    #             send_email(self.config, email_content, email_subject)
    #             execute_next = False
            
    #         if (execute_next is True):
    #             try:
    #                 click_register(self.driver, self.logger)
    #                 wait = WebDriverWait(self.driver, 3)
    #                 wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email already taken']")))
    #                 message = self.driver.find_element(By.XPATH, "//label[text()='Email already taken']").text
    #                 assert (message == "Email already taken")
    #                 self.logger.info("Successfully tested the case of using existing email.")
    #             except Exception as e:
    #                 error_message = "Failed the test - existing email was used to sign up the account. Broken implementation"
    #                 self.logger.critical(f"{error_message}: {e}")
    #                 email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test - existing email was used to sign up the account. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields but use an existing email</li><li>Click Register button to create an account</li><</ol></p></body></html>"
    #                 email_subject = "Error occured in the Home page"
    #                 send_email(self.config, email_content, email_subject)

    # Test case 3: Confirm password and password is different, catch the message -> "password" and "confirm password" must be the same
    def test_signUp_confirmPassword(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.config)
                enter_email(self.driver, self.logger, self.config, self.config["signIn_email"])
                enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.config, "invalid", "re_enter")
            except Exception as e:
                error_message = "Failed to open the Register pop up"
                self.logger.error(f"{error_message}: {e}")
                email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
                email_subject = "Error occured in the Home page"
                send_email(self.config, email_content, email_subject)
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-3 block text-da-accent-500']")))
                    message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-3 block text-da-accent-500']").text
                    assert (message == '"password" and "confirm password" must be the same')
                    self.logger.info("Successfully tested the case of different entered password and confirmed password.")
                except Exception as e:
                    error_message = "Failed the test - confirm password was different from entered password. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test - confirm password was different from entered password. Broken implementation. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields but enter a different password in the confirm password field</li><li>Click Register button to create an account</li><</ol></p></body></html>"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)

# Test case 4: Lack 1 field of input, catch the message -> "name" is required
# Test case 5: Enter all info but invalid email address, catch the message -> this is failing