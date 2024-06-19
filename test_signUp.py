from util import *

class Test_SignUp(BaseTest, unittest.TestCase):

    # # Test case 1: Enter all info and sign up successfully
    # def test_SignUp_successfully(self):
    #     if (self.next is True):
    #         click_sign_in(self.driver, self.logger, self.config)
    #         self.logger.info("Started Signing Up")
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
    #             #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
    #             email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20open%20the%20Register%20pop%20up.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20then%20the%20Register%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20the%20Register%20pop%20up%20can%20be%20loaded.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
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
    #                 #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to register an account.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields</li><li>Click Register button to create an account</li><</ol></p></body></html>"
    #                 email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20register%20an%20account.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20and%20click%20the%20Register%20button%3C%2Fli%3E%3Cli%3EFill%20in%20all%20required%20fields%3C%2Fli%3E%3Cli%3EClick%20Register%20button%20to%20create%20an%20account%3C%2Fli%3E%3C%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
    #                 email_subject = "Error occured in the Home page"
    #                 send_email(self.config, email_content, email_subject)
                    
    # Test case 2: Enter all info but using existing email, sign up failed and catch the message -> Email taken
    def test_signUp_existingEmail(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.config)
                enter_email(self.driver, self.logger, self.config, self.config["signIn_email"])
                enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.config, "valid", "re_enter")
            except Exception as e:
                error_message = "Failed to open the Register pop up"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20open%20the%20Register%20pop%20up.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20then%20the%20Register%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20the%20Register%20pop%20up%20can%20be%20loaded.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Home page"
                send_email(self.config, email_content, email_subject)
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email already taken']")))
                    message = self.driver.find_element(By.XPATH, "//label[text()='Email already taken']").text
                    assert (message == "Email already taken")
                    self.logger.info("Successfully tested the case of using existing email.")
                except Exception as e:
                    error_message = "Failed the test - existing email was used to sign up the account. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test - existing email was used to sign up the account. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields but use an existing email</li><li>Click Register button to create an account</li><</ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test%20-%20existing%20email%20was%20used%20to%20sign%20up%20the%20account.%20Broken%20implementation.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20and%20click%20the%20Register%20button%3C%2Fli%3E%3Cli%3EFill%20in%20all%20required%20fields%20but%20use%20an%20existing%20email%3C%2Fli%3E%3Cli%3EClick%20Register%20button%20to%20create%20an%20account%3C%2Fli%3E%3C%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)

    # Test case 3: Confirm password and password is different, catch the message -> "password" and "confirm password" must be the same
    def test_signUp_confirmPassword(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            self.logger.info("Started Signing Up")
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
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
                email_contentt = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20open%20the%20Register%20pop%20up.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20then%20the%20Register%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20the%20Register%20pop%20up%20can%20be%20loaded.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
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
                    #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test - confirm password was different from entered password. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields but enter a different password in the confirm password field</li><li>Click Register button to create an account</li><</ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test%20-%20confirm%20password%20was%20different%20from%20entered%20password.%20Broken%20implementation.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20and%20click%20the%20Register%20button%3C%2Fli%3E%3Cli%3EFill%20in%20all%20required%20fields%20but%20enter%20a%20different%20password%20in%20the%20confirm%20password%20field%3C%2Fli%3E%3Cli%3EClick%20Register%20button%20to%20create%20an%20account%3C%2Fli%3E%3C%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)

    # Test case 4: Lack 1 field of input, catch the message -> "email" is required
    def test_signUp_lackOneField(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.config)
            self.logger.info("Started Signing Up")
            click_register(self.driver, self.logger)
            execute_next = True
            try:
                enter_name(self.driver, self.logger, self.config)
                enter_password(self.driver, self.logger, self.config, "valid", "first_enter")
                enter_password(self.driver, self.logger, self.config, "valid", "re_enter")
            except Exception as e:
                error_message = "Failed to open the Register pop up"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Register pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button then the Register button</li><li>Wait to see if the Register pop up can be loaded.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20to%20open%20the%20Register%20pop%20up.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20then%20the%20Register%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20the%20Register%20pop%20up%20can%20be%20loaded.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Home page"
                send_email(self.config, email_content, email_subject)
                execute_next = False
            
            if (execute_next is True):
                try:
                    click_register(self.driver, self.logger)
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-3 block text-da-accent-500']")))
                    message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-3 block text-da-accent-500']").text
                    assert (message == '"email" is required')
                    self.logger.info("Successfully tested the case of not entered the email field.")
                except Exception as e:
                    error_message = "Failed the test - empty email field but can still registered. Broken implementation"
                    self.logger.critical(f"{error_message}: {e}")
                    #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test - empty email field but can still registered. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button and click the Register button</li><li>Fill in all required fields except the email field</li><li>Click Register button to create an account</li><</ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test%20-%20empty%20email%20field%20but%20can%20still%20registered.%20Broken%20implementation.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EClick%20the%20Sign%20In%20button%20and%20click%20the%20Register%20button%3C%2Fli%3E%3Cli%3EFill%20in%20all%20required%20fields%20except%20the%20email%20field%3C%2Fli%3E%3Cli%3EClick%20Register%20button%20to%20create%20an%20account%3C%2Fli%3E%3C%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Home page"
                    send_email(self.config, email_content, email_subject)
                    
                    
# Test case 5: Enter all info but invalid email address, catch the message -> this is failing

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
            error_handler(self.logger, self.configInfo, "Failure. Cannot open the Register pop up", e,
                self.configError["cannot_open_register_popup"], "Home")
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
            error_handler(self.logger, self.configInfo, "Failure. Empty email field but can still registered. Broken implementation", e,
                self.configError["empty_email_passed"], "Home")
            
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
            error_handler(self.logger, self.configInfo, "Failure. Existing email was used to sign up the account. Broken implementation", e,
                self.configError["existing_email_passed"], "Home")

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
            error_handler(self.logger, self.configInfo, "Failure. Confirm password was different from entered password. Broken implementation", e,
                self.configError["incorrect_confirm_password"], "Home") 

    def signUp_success(self):
        self.base.beginOfTest_logFormat("signUp_success")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='email']").clear()
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signUp_email"])
            self.driver.find_element(By.XPATH, "//input[@name='confirmPassword']").clear()
            enter_password(self.driver, self.logger, self.configInfo, "valid", "re_enter")
            click_register(self.driver, self.logger)
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "picture")))
            user_icon = self.driver.find_element(By.TAG_NAME, "picture")
            assert (user_icon.is_displayed())
            self.logger.debug("Saw the user icon")
            self.logger.info("Success. Tested registering a new account.")
            
            # Delete the testing account
            testUser_id = get_user_info(self.configInfo, "id", "signUp")
            admin_token = get_user_info(self.configInfo, "token", "admin")
            delete_user(admin_token, testUser_id)
            self.logger.debug("Deleting the testing user.")
    
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot register a new account.", e,
                self.configError["cannot_register_account"], "Home")
                
                    
    # Test case 5: Enter all info but invalid email address, catch the message -> this is failing
    
    # Test case 6: Password has at least 8 characters -> is there any other conditions for password?
