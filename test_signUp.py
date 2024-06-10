from util import *

class Test_SignUp(BaseTest, unittest.TestCase):

    # Test case 1: Enter all info and sign up successfully
    def test_SignUp_successfully(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.configInfo)
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signUp_email"])
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            except Exception as e:
                cannotOpenPopUp_errorHandler(e, self.logger, self.configError, self.configInfo, "register")
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    user_icon = self.driver.find_element(By.XPATH, "//img[@src='/imgs/profile.png']")
                    assert (user_icon.is_displayed())
                    self.logger.info("Success. Tested signing up an account.")
                    
                    # Delete the testing account
                    testUser_id = get_user_info(self.configInfo, "id", "signUp")
                    admin_token = get_user_info(self.configInfo, "token", "admin")
                    delete_user(admin_token, testUser_id)
                    
                except Exception as e:
                    cannotOpenPopUp_errorHandler(e, self.logger, self.configError, self.configInfo, "register")

                
    # Test case 2: Enter all info but using existing email, sign up failed and catch the message -> Email taken
    def test_signUp_existingEmail(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.configInfo)
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            except Exception as e:
                cannotOpenPopUp_errorHandler(e, self.logger, self.configError, self.configInfo, "register")
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email already taken']")))
                    message = self.driver.find_element(By.XPATH, "//label[text()='Email already taken']").text
                    assert (message == "Email already taken")
                    self.logger.info("Success. Tested the case of using existing email.")
                except Exception as e:
                    error_message = "Failure. Existing email was used to sign up the account. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = self.configError["existing_email_passed"]
                    email_subject = get_emailSubject("Home")
                    send_email(self.configInfo, email_content, email_subject)

    # Test case 3: Confirm password and password is different, catch the message -> "password" and "confirm password" must be the same
    def test_signUp_confirmPassword(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.configInfo)
                enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.configInfo, "invalid", "re_enter")
            except Exception as e:
                cannotOpenPopUp_errorHandler(e, self.logger, self.configError, self.configInfo, "register")
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    expected_message = '"password" and "confirm password" must be the same'
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
                    message = self.driver.find_element(By.XPATH, f"//label[text()='{expected_message}']").text
                    assert (message == expected_message)
                    self.logger.info("Success. Tested the case of different entered password and confirmed password.")
                except Exception as e:
                    error_message = "Failure. Confirm password was different from entered password. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = self.configError["incorrect_confirm_password"]
                    email_subject = get_emailSubject("Home")
                    send_email(self.configInfo, email_content, email_subject)

    # Test case 4: Lack 1 field of input, catch the message -> "email" is required
    def test_signUp_lackOneField(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.configInfo)
                enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            except Exception as e:
                cannotOpenPopUp_errorHandler(e, self.logger, self.configError, self.configInfo, "register")
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    expected_message = '"email" is required'
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_message}']")))
                    message = self.driver.find_element(By.XPATH,f"//label[text()='{expected_message}']").text
                    assert (message == expected_message)
                    self.logger.info("Success. Tested the case of not entered the email field.")
                except Exception as e:
                    error_message = "Failure. Empty email field but can still registered. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    email_content = self.configError["empty_email_passed"]
                    email_subject = get_emailSubject("Home")
                    send_email(self.configInfo, email_content, email_subject)
                    
    # Test case 5: Enter all info but invalid email address, catch the message -> this is failing
