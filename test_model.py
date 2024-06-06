from util import *

class Test_Model(BaseTest, unittest.TestCase):
    
    # Test case 1: Not sign in, if "Create New Model" button is visible then fail the test
    def test_noSignIn_createNewModel(self):
        self.base.beginOfTest_logFormat("test_noSignIn_createNewModel")
        if (self.next is True):
            self.logger.info("Started checking the visibility of 'Create New Model' button when not signing in")
            signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
            if (signIn_button.is_displayed()):
                self.logger.debug("User is not signing in")
                self.driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
                self.logger.debug("Clicked the Select Model button")
                try:
                    createModel_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Model')]")
                    if (createModel_button.is_displayed()):
                        error_message = "Failure. User did not sign in but can still see the 'Create New Model' button"
                        self.logger.critical(f"{error_message}")
                        #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. User did not sign in but can still see the 'Create New Model' button.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Do not sign in and click the Select Model button</li><li>Wait to see if there is the Create New Model button</li></ol></p></body></html>"
                        email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20User%20did%20not%20sign%20in%20but%20can%20still%20see%20the%20'Create%20New%20Model'%20button.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3EDo%20not%20sign%20in%20and%20click%20the%20Select%20Model%20button%3C%2Fli%3E%3Cli%3EWait%20to%20see%20if%20there%20is%20the%20Create%20New%20Model%20button%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                        email_subject = "Error occured in the Model page"
                        send_email(self.configInfo, email_content, email_subject)
                except Exception as e:
                    self.logger.info("Success. Tested the case of not seeing the 'Create New Model' button when not signing in")
                    
                    
    # Test case 2: Sign in, test create new model and create new prototype
    def test_SignIn_createNewModel(self):
        self.base.beginOfTest_logFormat("test_SignIn_createNewModel")
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
            enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
            submit_sign_in(self.driver, self.logger)
            
            time.sleep(5) # Explicit wait doesn't work here
            self.driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
            self.logger.debug("Clicked the Select Model button")
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Model')]").click()
            self.logger.debug("Clicked the Create New Model button")
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@src='/imgs/profile.png']")))
            
            # Check if the dropdown is empty or not
            try: 
                options = self.driver.find_elements(By.XPATH, "//select/option")
                assert (len(options) > 0)
                self.logger.info("Success. Tested the dropdown when creating a new model.")
            except Exception as e:
                error_message = "Failure. Empty option in the dropdown then creating a new model"
                self.logger.error(f"{error_message}: {e}")
                # email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Empty option in the dropdown then creating a new model.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model</li><li>Click the Create New Model, check the options in the pop up's dropdown.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Empty%20option%20in%20the%20dropdown%20then%20creating%20a%20new%20model.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Model%2C%20check%20the%20options%20in%20the%20pop%20up's%20dropdown.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Model page"
                send_email(self.configInfo, email_content, email_subject)
            
            # Hit Create New Model button without entering name
            try:
                self.driver.find_element(By. XPATH, "//button[text()='Create Model']").click()
                self.logger.debug("Submitted the Create Model button")
                wait = WebDriverWait(self.driver, 2)
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']")))
                message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']").text
                assert (message == '"name" is not allowed to be empty')
                self.logger.info("Success. Tested the case of empty input field when creating new model.")
            except Exception as e:
                error_message = "Failure. Empty input field passed"
                self.logger.error(f"{error_message}: {e}")
                # email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Empty input field passed.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model</li><li>Click the Create New Model, leave the name field empty and click Create Model.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Empty%20input%20field%20passed.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Model%2C%20leave%20the%20name%20field%20empty%20and%20click%20Create%20Model.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Model page"
                send_email(self.configInfo, email_content, email_subject)
            
            # Hit Create New Model button and entering name
            try:
                expected_name = "Automation Test Model"
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Model Name']").send_keys(expected_name)
                self.logger.debug("Entered the name for the new model")
                self.driver.find_element(By. XPATH, "//button[text()='Create Model']").click()
                self.logger.debug("Submitted the Create Model button")
                wait = WebDriverWait(self.driver, 4)
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_name}']")))
                self.logger.debug("Created a new model")
                model_name = self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").text
                assert (model_name == expected_name)
                self.logger.info("Success. Verified the name of the new model")
            except Exception as e:
                error_message = "Failure. Entered new model name is different from resulting new model name"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Entered new model name is different from resulting new model name.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model</li><li>Click the Create New Model, enter the name and click Create Model.</li><li>Verify the entered model name with the actual model name on the screen</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Entered%20new%20model%20name%20is%20different%20from%20resulting%20new%20model%20name.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Model%2C%20enter%20the%20name%20and%20click%20Create%20Model.%3C%2Fli%3E%3Cli%3EVerify%20the%20entered%20model%20name%20with%20the%20actual%20model%20name%20on%20the%20screen%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Model page"
                send_email(self.configInfo, email_content, email_subject)
                
            # Test the visibility when click Change to public/private
            old_mode = self.driver.find_element(By.XPATH, "//label[text()='Visibility:']/label").text
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Change to')]")
            
            # Navigate to other pages to test the prototype creation functions
            self.driver.find_element(By.XPATH, "//label[text()='Prototype Library']").click()
            self.logger.debug("Clicked the Prototype Library button")
            self.driver.find_element(By.XPATH, "//button[text()='Create New Prototype']").click()
            self.logger.debug("Clicked the Create New Prototype button")

            # Hit Create New Prototype without entering name
            try:
                self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
                self.logger.debug("Clicked the Create Prototype button")
                self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']")
                wait = WebDriverWait(self.driver, 5)
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']")))
                message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']").text
                assert (message == "Something went wrong")
                self.logger.info("Success. Tested the case of empty input field when creating new prototype.")
            except Exception as e:
                error_message = "Failure. Empty input field passed"
                self.logger.error(f"{error_message}: {e}")
                #email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Empty input field passed.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model, choose a model and click Prototype Library</li><li>Click the Create New Prototype, leave the name field empty and click Create.</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Empty%20input%20field%20passed.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%2C%20choose%20a%20model%20and%20click%20Prototype%20Library%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Prototype%2C%20leave%20the%20name%20field%20empty%20and%20click%20Create.%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Model page"
                send_email(self.configInfo, email_content, email_subject)
            
            # Hit Create New Prototype and entering name
            try:
                expected_name = "Automation Test Prototype"
                self.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(expected_name)
                self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
                self.logger.debug("Clicked the Create Prototype button")
                wait = WebDriverWait(self.driver, 5)
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_name}']")))
                prototype_name_left = self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").text
                assert (prototype_name_left == expected_name)
                self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").click()
                self.logger.debug("Clicked the prototype box")
                self.logger.info("Success. Verified the name of the newly created prototype on the left")
                
                try:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']")))
                    prototype_name_right = self.driver.find_element(By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']").text
                    assert (prototype_name_right == expected_name)
                    self.logger.info("Success. Verified the name of the newly created prototype on the right")
                    self.driver.find_element(By.XPATH, "//a/button[text()='Open']").click()
                    
                    # Delete the testing prototype
                    token = get_user_info(self.configInfo, "token", "signIn")
                    current_url = self.driver.current_url
                    prototype_id = current_url[83:107]
                    print(f"\nPrototype ID is: {prototype_id}")
                    print(delete_prototype(token,prototype_id))
                    
                except Exception as e:
                    error_message = "Failure. Incorrect name of the newly created prototype on the right"
                    self.logger.error(f"{error_message}: {e}")
                    # email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Incorrect name of the newly created prototype on the right.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model, choose a model and click Prototype Library</li><li>Click the Create New Prototype, enter the name and click Create.</li><li>Wait and see the prototype name on the prototype page</li></ol></p></body></html>"
                    email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Incorrect%20name%20of%20the%20newly%20created%20prototype%20on%20the%20right.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%2C%20choose%20a%20model%20and%20click%20Prototype%20Library%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Prototype%2C%20enter%20the%20name%20and%20click%20Create.%3C%2Fli%3E%3Cli%3EWait%20and%20see%20the%20prototype%20name%20on%20the%20prototype%20page%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                    email_subject = "Error occured in the Model page"
                    send_email(self.configInfo, email_content, email_subject)
                
            except Exception as e:
                error_message = "Failure. Incorrect name of the newly created prototype on the left"
                self.logger.error(f"{error_message}: {e}")
                # email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed the test. Incorrect name of the newly created prototype on the left.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Sign in and click Select Model, choose a model and click Prototype Library</li><li>Click the Create New Prototype, enter the name and click Create.</li><li>Wait and see the prototype name on the prototype page</li></ol></p></body></html>"
                email_content = "%3C!DOCTYPE%20html%3E%3Chtml%20lang%3D'en'%3E%3Cbody%3E%3Cp%3EFailed%20the%20test.%20Incorrect%20name%20of%20the%20newly%20created%20prototype%20on%20the%20right.%3C%2Fp%3E%3Cp%3ESteps%20to%20Reproduce%3A%3C%2Fp%3E%3Col%3E%3Cli%3ENavigate%20to%20the%20home%20page.%3C%2Fli%3E%3Cli%3ESign%20in%20and%20click%20Select%20Model%2C%20choose%20a%20model%20and%20click%20Prototype%20Library%3C%2Fli%3E%3Cli%3EClick%20the%20Create%20New%20Prototype%2C%20enter%20the%20name%20and%20click%20Create.%3C%2Fli%3E%3Cli%3EWait%20and%20see%20the%20prototype%20name%20on%20the%20prototype%20page%3C%2Fli%3E%3C%2Fol%3E%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
                email_subject = "Error occured in the Model page"
                send_email(self.configInfo, email_content, email_subject)
                
            # Delete the testing model
            token = get_user_info(self.configInfo, "token", "signIn")
            current_url = self.driver.current_url
            model_id = current_url[40:64]
            delete_model(token, model_id)