from setup_methods.util import *

class Test_Model(BaseTest, unittest.TestCase):
    def test_Model_functionalities(self):
        if (self.next is True):
            self.noSignIn_createModel()
            self.SignIn_createModel() # Also check the dropdown content inside this function
            self.check_modelVisibility() 
            self.add_member_contributor()
            self.create_maximumModels()
            self.delete_testing_models()

    def noSignIn_createModel(self):
        self.base.beginOfTest_logFormat("noSignIn_createModel")
        self.logger.info("Started checking the visibility of 'Create New Model' button when not signing in")
        signIn_button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")
        if (signIn_button.is_displayed()):
            self.logger.debug("User is not signing in")
            click_getting_started(self.driver)

            try:
                createModel_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Model')]")
                if (createModel_button.is_displayed()):
                    error_handler("critical", self.logger, self.configInfo, "Failure. User did not sign in but can still see the 'Create New Model' button",
                        "", self.configError["not_signIn_see_CreateModel"], "Model")
            except:
                self.logger.info("Success. Tested the case of not seeing the 'Create New Model' button when not signing in")
    
    def SignIn_createModel(self):
        self.base.beginOfTest_logFormat("SignIn_createModel")
        sign_in(self.driver, self.configInfo)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Create New Model']").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@src='/imgs/profile.png']")))
        self.check_dropdownContent()
        
        # Hit Create New Model button without entering name
        try:
            self.driver.find_element(By. XPATH, "//button[text()='Create Model']").click()
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']")))
            message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']").text
            assert (message == '"name" is not allowed to be empty')
            self.logger.info("Success. Tested the case of empty input field when creating new model.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Empty input name passed when creating a new model", e, "", "")
            
        # Hit Create New Model button and entering name
        try:
            expected_name = "Automation Test Model 1"
            self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Model Name']").send_keys(expected_name)
            self.driver.find_element(By. XPATH, "//button[text()='Create Model']").click()
            wait = WebDriverWait(self.driver, 4)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_name}']")))
            self.logger.debug("Created a new model")
            model_name = self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").text
            assert (model_name == expected_name or model_name == 'Model "Automation Test Model 1" created successfully')
            self.logger.info("Success. Verified the name of the new model")
        except Exception as e:
            error_handler("warning", self.logger, self.configInfo, "Failure. Entered new model name is different from resulting new model name", e, "", "")
                    
    def check_dropdownContent(self):
        self.base.beginOfTest_logFormat("check_dropdownContent")
        self.logger.info("Checking if the Create New Model dropdown is empty or not")
        try: 
            options = self.driver.find_elements(By.XPATH, "//select/option")
            assert (len(options) > 0)
            self.logger.info("Success. Tested the dropdown content when creating a new model.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Empty option in the dropdown then creating a new model", e, "", "")
    
    def check_modelVisibility(self):
        self.base.beginOfTest_logFormat("check_modelVisibility")
        self.logger.info("Test the visibility when click Change to public/private")
        wait = WebDriverWait(self.driver, 2)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Visibility:']/label")))
        current_mode = self.driver.find_element(By.XPATH, "//label[text()='Visibility:']/label").text
        visibility_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Change to')]")
        button_mode = visibility_button.text
        try:
            self.logger.info("Started to switch from private to public mode")
            assert (button_mode == "Change to public")
            visibility_button.click()
            self.logger.debug("Clicked the 'Change to public' button")
            current_mode = self.driver.find_element(By.XPATH, "//label[text()='Visibility:']/label").text
            assert (current_mode == "Public")
            self.logger.info("Success. Switched successfully from private to public mode")
            time.sleep(3)
            try:
                self.logger.info("Started to switch from public to private mode")
                visibility_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Change to')]")
                button_mode = visibility_button.text
                assert (button_mode == "Change to private")
                visibility_button.click()
                self.logger.debug("Clicked the 'Change to private' button")
                current_mode = self.driver.find_element(By.XPATH, "//label[text()='Visibility:']/label").text
                assert (current_mode == "Private")
                self.logger.info("Success. Switched successfully from public to private mode")
                time.sleep(3)
            except Exception as e:
                error_handler("error", self.logger, "", "Failure. Failed to switch from public mode to private mode", e, "", "")
        except Exception as e:
           error_handler("error", self.logger, "", "Failure. Failed to switch from private mode to public mode", e, "", "")
    
    def add_member_contributor(self):
        self.base.beginOfTest_logFormat("add_member_contributor")
        self.logger.info("Test the add user functionality in model detail page")
        
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add user']").click()
        try:
            users = self.driver.find_elements(By.XPATH, "//div[@class='border-b border-slate-200 flex']")
            assert (len(users) > 0)
            self.logger.info("Success. The list of user in the 'add user' pop up is not empty.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. The list of user in the 'add user' pop up is empty.", e, "", "")
        try:
            search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            self.search_user("my", "My")
            time.sleep(2)
            search_box.send_keys(Keys.CONTROL,'A')
            search_box.send_keys(Keys.BACK_SPACE)
            self.search_user("hc", "My")
            time.sleep(2)
            self.logger.info("Success. Found the correct user after typing characters in the search box.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. The filter list in the add user pop up doesn't work properly.", e, "", "")
            
        # Close the add user pop up to click other buttons
        self.driver.find_element(By.XPATH, "//button[text()='Close']").click()
        time.sleep(2)
    
    def search_user(self, input, expected_result):
        try:
            self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(input)
            result_text = self.driver.find_element(By.XPATH, "//div[@class='py-1 grow']/label").text
            assert (result_text == expected_result)
        except:
            self.logger.debug("Search function doesn't work properly.")
            raise Exception

    def create_maximumModels(self):
        self.base.beginOfTest_logFormat("create_maximumModels")
        try:
            self.driver.find_element(By.XPATH, "//a[text()='Vehicle Models']").click()
            create_new_model(self.driver, "Automation Test Model 2")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//a[text()='Vehicle Models']").click()
            create_new_model(self.driver, "Automation Test Model 3")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//a[text()='Vehicle Models']").click()
            create_new_model(self.driver, "Automation Test Model 4")
            
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']")))
            message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-2 text-da-accent-500']").text
            assert (message == "Users are limited to 3 models")
            self.logger.info("Success. Tested the case of creating maximum number of models.")
        except Exception as e:
            error_handler("warning", self.logger, "", "Failure. User can create more than 3 models.", e, "", "")
        
    def delete_testing_models(self):
        try:
            self.base.beginOfTest_logFormat("delete_testing_models")
            action = ActionChains(self.driver)
            action.move_by_offset(100, 100).click().perform() # Click outside the pop up
            self.driver.refresh()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//label[text()='Automation Test Model 1']").click()
            delete_testing_object("model", self.driver, self.logger, self.configInfo)
            self.logger.debug("URL: ", self.driver.current_url)
            self.driver.back()
            self.driver.refresh()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//label[text()='Automation Test Model 2']").click()
            delete_testing_object("model", self.driver, self.logger, self.configInfo)
            self.logger.debug("URL: ", self.driver.current_url)
            self.driver.back()
            self.driver.refresh()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//label[text()='Automation Test Model 3']").click()
            delete_testing_object("model", self.driver, self.logger, self.configInfo)
            self.logger.debug("URL: ", self.driver.current_url)
            self.driver.back()
        except Exception as e:
            self.logger.debug("Unable to delete all three testing models.")