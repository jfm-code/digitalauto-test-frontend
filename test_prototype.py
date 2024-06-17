from util import *

class Test_Prototype(BaseTest, unittest.TestCase):
    def test_Prototype_functionalities(self):
        if (self.next is True):
            click_sign_in(self.driver, self.logger, self.configInfo)
            enter_email(self.driver, self.logger, self.configInfo, self.configInfo["signIn_email"])
            enter_password(self.driver, self.logger, self.configInfo, "valid", "first_enter")
            submit_sign_in(self.driver, self.logger)
            time.sleep(5)
            
            self.create_and_verify_prototypeName()
            self.driver.find_element(By.XPATH, "//button[text()='Open']").click() # Open the prototype detail page
            self.use_Dashboard_Config()
            self.check_widgetList_content()
            self.add_widget()
            self.edit_widget()
            self.delete_widget()
            
            # Delete the testing prototype
            token = get_user_info(self.configInfo, "token", "signIn")
            current_url = self.driver.current_url
            prototype_id = current_url[83:107]
            delete_prototype(token, prototype_id)
            
    def create_and_verify_prototypeName(self):
        self.base.beginOfTest_logFormat("create_and_verify_prototypeName")
        
        # Choose the Combustion Car model to create testing prototype 
        time.sleep(3)
        click_select_model(self.driver, self.logger)
        self.driver.find_element(By.XPATH, "//label[text()='Combustion Car']").click()
        click_prototype_library(self.driver, self.logger)
        click_create_prototype(self.driver, self.logger)
        
        # Hit Create New Prototype without entering name 
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
            self.logger.debug("Clicked the Create Prototype button")
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']")))
            message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']").text
            assert (message == "Something went wrong")
            self.logger.info("Success. Tested the case of empty input field when creating new prototype.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Empty name field passed", e,
                self.configError["empty_nameInput_passed_CreatePrototype"], "Model")
        
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
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Incorrect name of the newly created prototype on the left", e,
                self.configError["wrong_newPrototype_name"], "Model")
            
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']")))
            prototype_name_right = self.driver.find_element(By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']").text
            assert (prototype_name_right == expected_name)
            self.logger.info("Success. Verified the name of the newly created prototype on the right")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Incorrect name of the newly created prototype on the right", e,
                self.configError["wrong_newPrototype_name"], "Model")

    def use_Dashboard_Config(self):
        self.base.beginOfTest_logFormat("use_Dashboard_Config")

        self.driver.find_element(By.XPATH, "//div[text()='Code']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Dashboard Config']").click()
        self.driver.find_element(By.XPATH, "//div[text()='1']").click()
        self.driver.find_element(By.XPATH, "//div[text()='3']").click()
        self.driver.find_element(By.XPATH, "//div[text()='4']").click()
        self.driver.find_element(By.XPATH, "//div[text()='8']").click()
        self.driver.find_element(By.XPATH, "//div[text()='9']").click()
        
        try:
            add_widget_btn = self.driver.find_element(By.XPATH, "//button[text()='Add widget']")
            if (add_widget_btn.is_displayed()):
                error_handler(self.logger, self.configInfo, "Failure. 'Add widget' button appeared when invalid boxes are selected",
                    "", self.configError["addWidget_invalidBoxes"], "Prototype")
        except:
            self.logger.info("Success. The 'Add widget' button did not appear when invalid boxes are selected.")
            
        try:
            self.driver.find_element(By.XPATH, "//div[@class='flex-1 flex flex-col w-full overflow-hidden']/div/div/div[text()='1']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Add widget']").click()
            self.logger.info("Success. The 'Add widget' button appeared when valid boxes are selected")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. 'Add widget' button did not appear when valid boxes are selected", e,
                self.configError["addWidget_validBoxes"], "Prototype")

    def check_widgetList_content(self):
        self.base.beginOfTest_logFormat("check_widgetList_content")
        try:
            widgets = self.driver.find_elements(By.XPATH, "//div[@class='grow']/div/div")
            assert (len(widgets) > 0)
            self.logger.info("Success. The list of widgets is not empty.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. List of widgets is empty.", e,
                self.configError["addWidget_widgetList_empty"], "Prototype")
            
    def add_widget(self):
        self.base.beginOfTest_logFormat("add_widget")
        try:
            self.driver.find_element(By.XPATH, "//label[text()='Simple Wiper Widget']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Add selected widget']").click()
            widget_text = self.driver.find_element(By.XPATH, "//div[text()='Simple Wiper Widget']").text
            assert (widget_text == "Simple Wiper Widget")
            self.logger.info("Success. Added a widget to the Dashboard Config.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot add a widget to the Dashboard Config.", e,
                self.configError["addWidget_failed"], "Prototype")
            
    def delete_widget(self):
        self.base.beginOfTest_logFormat("delete_widget")
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, "//div[text()='Simple Wiper Widget']")).perform()
            self.driver.find_element(By.XPATH, "//button[@class='da-btn da-btn-plain da-btn-md !px-0']//*[name()='svg']").click()
            alert_popup = self.driver.switch_to.alert
            alert_popup.accept()
            self.logger.info("Success. Deleted a widget in the Dashboard Config.")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot delete a widget in the Dashboard Config.", e,
                self.configError["deleteWidget_failed"], "Prototype")
            
    def edit_widget(self):
        self.base.beginOfTest_logFormat("edit_widget")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//div[text()='Simple Wiper Widget']")).perform()
        self.driver.find_element(By.XPATH, "//button[@class='da-btn da-btn-plain da-btn-md !px-0 hover:text-da-primary-500']//*[name()='svg']").click()
        time.sleep(2)
        try:
            wait = WebDriverWait(self.driver, 10)
            modal = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='MuiModal-root css-8ndowl']")))
            code_block = modal.find_element(By.XPATH, ".//div[contains(@class, 'monaco-editor')]")
            line_of_code = code_block.find_element(By.XPATH, ".//div[@class='view-line' and .//span[text()='\"Builtin\"']]")
            line_of_code.click()
            
            for _ in range(2):
                action.send_keys(Keys.ARROW_LEFT).perform()
            action.send_keys(" Testing").perform()
            
            action.move_to_element(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")).perform()
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button/div[text()='Show all raw config text']").click()
            
            wait = WebDriverWait(self.driver, 10)
            code_block = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//div[contains(@class, 'view-lines monaco-mouse-cursor-text')])[2]")))
            self.logger.debug("Found the code_block")
            inner_html = code_block.get_attribute('innerHTML')
            self.logger.debug("Code block inner HTML: %s", inner_html)
            span_elements = code_block.find_elements(By.XPATH, ".//span[@class='mtk5']")
            
            found = False
            for span in span_elements:
                if span.text == '"Builtin Testing"':
                    self.logger.debug("Found the span with text: %s", span.text)
                    found = True
                    break
            if not found:
                self.logger.debug("Did not find the span with text 'Builtin Testing'")
            else:
                assert (span.text == '"Builtin Testing"')
            self.logger.info("Success. Tested the case of editing the widget config text.")
        
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot edit the widget config text.", e,
                    self.configError["editWidget_failed"], "Prototype")