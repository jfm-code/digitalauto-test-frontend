from util import *

class Test_Prototype(BaseTest, unittest.TestCase):
    def test_Prototype_functionalities(self):
        self.base.beginOfTest_logFormat("test_Prototype_functionalities")
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
            enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
            submit_sign_in(self.driver, self.logger)
            self.logger.info("Started testing prototype functionalities after signing in")
            time.sleep(5)
            
            # Test case 1: Create new prototype and verify the name
            self.create_and_verify_prototypeName()
            
    def create_and_verify_prototypeName(self):
        # Choose the Combustion Car model to create testing prototype
        click_select_model(self.driver, self.logger)
        self.driver.find_element(By.XPATH, "//label[text()='Combustion Car']").click()
        click_prototype_library(self.driver, self.logger)
        click_create_prototype(self.driver, self.logger)
        
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
            error_message = "Failure. Empty name field passed"
            self.logger.error(f"{error_message}: {e}")
            email_content = self.configError["empty_nameInput_passed_CreatePrototype"]
            email_subject = get_emailSubject("Model")
            send_email(self.configInfo, email_content, email_subject)
        
        # Hit Create New Prototype and entering name
        try:
            expected_name = "Automation Test Prototype"
            self.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(expected_name)
            self.logger.debug("Entered the prototype name")
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
                delete_prototype(token,prototype_id)
                
            except Exception as e:
                error_message = "Failure. Incorrect name of the newly created prototype on the right"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["wrong_newPrototype_name"]
                email_subject = get_emailSubject("Model")
                send_email(self.configInfo, email_content, email_subject)
            
        except Exception as e:
            error_message = "Failure. Incorrect name of the newly created prototype on the left"
            self.logger.error(f"{error_message}: {e}")
            email_content = self.configError["wrong_newPrototype_name"]
            email_subject = get_emailSubject("Model")
            send_email(self.configInfo, email_content, email_subject)
