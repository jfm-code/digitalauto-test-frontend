# NOT DONE
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
            self.use_Code_dashboardConfig()
            self.check_widgetList_content()
            self.add_widget()
            self.use_Dashboard()
            time.sleep(7)
            self.edit_widget()
            time.sleep(3)
            self.delete_widget()
            
            self.modifyCode_checkUpdate("from_Code_to_Dashboard")
            self.run_code("no_error")
            self.modifyCode_checkUpdate("from_Dashboard_to_Code")
            # self.run_code("error")
            
            # Delete the testing model
            try:
                token = get_user_info(self.configInfo, "token", "signIn")
                current_url = self.driver.current_url
                pattern = r"model/([a-f0-9]{24})"
                model_id = re.findall(pattern, current_url)
                delete_model(token, model_id[0], self.configInfo)
                self.logger.info("Success. Deleted the testing model using Postman API.")
            except Exception as e:
                error_handler("warning", self.logger, "", "Failure. Cannot use Postman API to delete the testing model.", e, "", "")
            
            try:
                # Delete the testing prototype
                token = get_user_info(self.configInfo, "token", "signIn")
                current_url = self.driver.current_url
                pattern = r"/prototype/([a-f0-9]{24})/"
                prototype_id = re.findall(pattern, current_url)
                delete_prototype(token, prototype_id[0], self.configInfo)
                self.logger.info("Success. Deleted the testing prototype using Postman API.")
            except Exception as e:
                error_handler("warning", self.logger, "", "Failure. Cannot use Postman API to delete the testing prototype.", e, "", "")
                
    def run_code(self, mode):
        self.base.beginOfTest_logFormat(f"run_code_{mode}")
        try:
            static_dropdown = Select(self.driver.find_element(By.XPATH, "//select")) 
            static_dropdown.select_by_value("RunTime-VSS4.0-1970345")
            self.logger.info("Success. The RunTime-VSS4.0-1970345 is online.")
        except Exception as e:
            error_handler("warning", self.logger, "", "Failure. The RunTime-VSS4.0-1970345 is not online.", e, "", "")
        
        if (mode == "no_error"):
            try:
                self.driver.find_element(By.XPATH, "(//div[@class='flex px-1 false']/button)[1]").click()
                time.sleep(3)
                output = self.driver.find_element(By.XPATH, "//p[contains(text(),'code 0')]")
                assert (output.is_displayed())
                self.logger.info("Success. Run code successfully with exit code 0 in the Dashboard tab.")
            except Exception as e:
                error_handler("error", self.logger, "", "Failure. Failed to run code in the Dashboard tab.", e, "", "")
        elif (mode == "error"):
            try:
                self.driver.find_element(By.XPATH, "(//div[@class='flex px-1 false']/button)[1]").click()
                time.sleep(5) # wait for some output is printed
                self.driver.find_element(By.XPATH, "(//div[@class='flex px-1 false']/button)[2]").click()
                time.sleep(2) # wait for the error exit code to be appeared
                # NOT DONE
                # observe and grab the error exit code
            except Exception as e:
                error_handler("error", self.logger, "", "Failure. Failed to stop the executing code and return error exit code.", e, "", "")
                
    def modifyCode_checkUpdate(self, mode):
        self.base.beginOfTest_logFormat(f"modifyCode_checkUpdate_{mode}")
        if (mode == "from_Code_to_Dashboard"):
            try:
                code_block = self.driver.find_element(By.XPATH, "//div[@class='w-1/2 flex flex-col border-r']")
                line = code_block.find_element(By.XPATH, ".//div[@class='line-numbers' and text()='30']")
                line.click()
                action1 = ActionChains(self.driver)
                action1.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.BACK_SPACE).send_keys('print("Automation Test")').perform()
            
                time.sleep(2) # wait for the update in the Dashboard tab
                self.driver.find_element(By.XPATH, "//a/div[text()='Dashboard']").click()
                self.driver.find_element(By.XPATH, "//div[@class='flex']/button").click()
                self.driver.find_element(By.XPATH, "//div[@class='flex']/div[text()='Code']").click()
                time.sleep(3)
                
                result = self.driver.find_element(By.XPATH, "//div[@class='view-lines monaco-mouse-cursor-text']//span/span[text()='print']")
                assert (result.text == "print")
                self.logger.info("Success. Verified the code entered from Code tab in Dashboard tab.")
            except Exception as e:
                error_handler("error", self.logger, "", "Failure. The code entered in Code tab is not updated in Dashboard tab.", e, "", "")
        elif (mode == "from_Dashboard_to_Code"):
            try:
                self.driver.find_element(By.XPATH, "//div[@class='flex']/div[text()='Code']").click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, "//div[contains(@class, 'active-line-number')]").click()
                action = ActionChains(self.driver)
                action.key_down(Keys.BACK_SPACE).send_keys("for i in range(10):").key_down(Keys.ENTER).send_keys("print(i)").perform()
                
                time.sleep(3) # wait for the update in the Code tab
                # NOT DONE 
                # go to the Code tab to check
                # then go back to the Dashboard tab, click to open run code section
            except Exception as e:
                error_handler("error", self.logger, "", "Failure. The code entered in Dashboard tab is not updated in Code tab.", e, "", "")
                
    def create_and_verify_prototypeName(self):
        self.base.beginOfTest_logFormat("create_and_verify_prototypeName")
        
        # Choose the Combustion Car model to create testing prototype 
        time.sleep(3)
        click_select_model(self.driver, self.logger)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Model')]").click()
        expected_name = "Automation Test Model"
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Model Name']").send_keys(expected_name)
        self.driver.find_element(By. XPATH, "//button[text()='Create Model']").click()
        # self.driver.find_element(By.XPATH, "//label[text()='Combustion Car']").click()
        click_prototype_library(self.driver, self.logger)
        click_create_prototype(self.driver, self.logger)
        
        # Hit Create New Prototype without entering name 
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
            self.logger.debug("Clicked the Create Prototype button")
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']")))
            message = self.driver.find_element(By.XPATH, "//label[@class='da-label-small mt-4 text-da-accent-500']").text
            assert (message == '"name" is not allowed to be empty')
            self.logger.info("Success. Tested the case of empty input field when creating new prototype.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Empty input name passed when creating a new prototype", e, "", "")
        
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
            error_handler("warning", self.logger, "", "Failure. Incorrect name of the newly created prototype on the left", e, "", "")
            
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']")))
            prototype_name_right = self.driver.find_element(By.XPATH, f"//div[@class='p-5']/div/label[text()='{expected_name}']").text
            assert (prototype_name_right == expected_name)
            self.logger.info("Success. Verified the name of the newly created prototype on the right")
        except Exception as e:
            error_handler("warning", self.logger, "", "Failure. Incorrect name of the newly created prototype on the right", e, "", "")

    def use_Code_dashboardConfig(self):
        self.base.beginOfTest_logFormat("use_Code_dashboardConfig")

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
            error_handler("error", self.logger, "", "Failure. 'Add widget' button did not appear when valid boxes are selected", e, "", "")

    def use_Dashboard(self):
        self.base.beginOfTest_logFormat("use_Dashboard")
        try:
            self.driver.find_element(By.XPATH, "//div[text()='Dashboard']").click()
            wait = WebDriverWait(self.driver, 3)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='col-span-2 row-span-2']/iframe")))
            widget_preview = self.driver.find_element(By.XPATH, "//div[@class='col-span-2 row-span-2']/iframe")
            assert (widget_preview.is_displayed())
            following_boxes = self.driver.find_elements(By.XPATH, "//div[@class='col-span-2 row-span-2']/following-sibling::*")
            preceeding_boxes = self.driver.find_elements(By.XPATH, "//div[@class='col-span-2 row-span-2']/preceding-sibling::*")
            assert (len(preceeding_boxes) == 2 and len(following_boxes) == 4)
            self.logger.info("Success. Tested the Dashboard functionality to preview widget.")
            time.sleep(2)
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot see the preview of the widget in the Dashboard.", e, "", "")
        
    def check_widgetList_content(self):
        self.base.beginOfTest_logFormat("check_widgetList_content")
        try:
            time.sleep(2)
            widgets = self.driver.find_elements(By.XPATH, "//div[@class='grow']/div/div")
            assert (len(widgets) > 0)
            self.logger.info("Success. The list of widgets is not empty.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. List of widgets is empty.", e, "", "")

    def add_widget(self):
        self.base.beginOfTest_logFormat("add_widget")
        try:
            self.driver.find_element(By.XPATH, "(//div[contains(text(), 'Marketplace')])[2]").click()
            self.driver.find_element(By.XPATH, "//label[text()='Simple Wiper Widget']").click()
            self.driver.find_element(By.XPATH, "//button[text()='Add selected widget']").click()
            widget_text = self.driver.find_element(By.XPATH, "//div[text()='Simple Wiper Widget']").text
            assert (widget_text == "Simple Wiper Widget")
            self.logger.info("Success. Added a widget to the Dashboard Config.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot add a widget to the Dashboard Config.", e, "", "")
            
    def delete_widget(self):
        self.base.beginOfTest_logFormat("delete_widget")
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, "//div[text()='Simple Wiper Widget']")).perform()
            self.driver.find_element(By.XPATH, "//button[@class='da-btn da-btn-destructive da-btn-md !px-0']//*[name()='svg']").click()
            alert_popup = self.driver.switch_to.alert
            alert_popup.accept()
            self.logger.info("Success. Deleted a widget in the Dashboard Config.")
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot delete a widget in the Dashboard Config.", e, "", "")
            
    def edit_widget(self):
        self.base.beginOfTest_logFormat("edit_widget")
        self.driver.find_element(By.XPATH, "//div[text()='Code']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Dashboard Config']").click()
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
            
            action1 = ActionChains(self.driver)
            action1.send_keys(Keys.ARROW_LEFT).perform()
            action2 = ActionChains(self.driver)
            action2.send_keys(Keys.ARROW_LEFT).perform()
            time.sleep(1)  # Small delay to ensure key press is pressed
            action3 = ActionChains(self.driver)
            action3.send_keys(" Testing").perform()
            time.sleep(1)  

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
            if (found is False):
                self.logger.debug("Did not find the span with text 'Builtin Testing'")
            else:
                assert (span.text == '"Builtin Testing"')
                self.logger.info("Success. Tested the case of editing the widget config text.")
        
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot edit the widget config text.", e, "", "")