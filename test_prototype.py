from util import *

class Test_Prototype(BaseTest, unittest.TestCase):
    def test_Prototype_functionalities(self):
        if (self.next is True):
            sign_in(self.driver, self.configInfo)
            time.sleep(5)
            
            self.create_and_verify_prototypeName()
            action = ActionChains(self.driver)
            action.move_by_offset(100, 100).click().perform() # Click outside the pop up
            self.driver.find_element(By.XPATH, "//button[text()='Open']").click() # Open the prototype detail page
            
            self.edit_prototype()
            time.sleep(5)
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
        
            delete_testing_object("prototype", self.driver, self.logger, self.configInfo)
            delete_testing_object("model", self.driver, self.logger, self.configInfo)
            
    def edit_prototype(self):
        self.base.beginOfTest_logFormat("edit_prototype")
        try:
            # edit the information
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Edit Prototype']").click()
            self.driver.find_element(By.XPATH, "//div/label[text()='Problem']/following-sibling::div/div/input").send_keys("Testing Problem")
            self.driver.find_element(By.XPATH, "//div/label[text()='Says who?']/following-sibling::div/div/input").send_keys("Testing People")
            self.driver.find_element(By.XPATH, "//div/label[text()='Solution']/following-sibling::div/div/input").send_keys("Testing Solution")
            complexity = self.driver.find_element(By.XPATH, "//label[text()='Complexity']/following-sibling::div/label/button[@role='combobox']")
            complexity.click()
            action = ActionChains(self.driver)
            action.move_to_element(complexity).move_by_offset(0,100).click().perform()
            status = self.driver.find_element(By.XPATH, "//label[text()='Status']/following-sibling::div/label/button[@role='combobox']")
            status.click()
            action1 = ActionChains(self.driver)
            action1.move_to_element(status).move_by_offset(0,100).click().perform()
            self.driver.find_element(By.XPATH, "//button[text()=' Change Image']").click()
            self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(self.configInfo["test_image_path"])
            self.driver.find_element(By.XPATH, "//button[text()='Save']").click()
            
            # verify the changes
            object = self.driver.find_element(By.XPATH, "//label[text()='Testing Problem']")
            assert (object.is_displayed())
            object = self.driver.find_element(By.XPATH, "//label[text()='Testing People']")
            assert (object.is_displayed())
            object = self.driver.find_element(By.XPATH, "//label[text()='Testing Solution']")
            assert (object.is_displayed())
            object = self.driver.find_element(By.XPATH, "//label[text()='Released']")
            assert (object.is_displayed())
            object = self.driver.find_element(By.XPATH, "//label[text()='Low']")
            assert (object.is_displayed())
            object = self.driver.find_element(By.XPATH, "//div/img[contains(@src, 'https://upload.digitalauto.tech/data')]")
            assert (object.is_displayed())
            
            self.logger.info("Success. Edited succesfully the information of prototype.")
        except Exception as e:
            error_handler("warning", self.logger, "", "Failure. Failed to edit the information of prototype.", e, "", "")
                
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
            
                time.sleep(5) # wait for the update in the Dashboard tab
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
        time.sleep(3)
        create_new_model(self.driver, "Automation Test Model")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[text()='Prototype Library']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Create New Prototype']").click()
        
        # Hit Create New Prototype without entering name 
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
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
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//label[text()='{expected_name}']")))
            prototype_name_left = self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").text
            assert (prototype_name_left == expected_name)
            self.driver.find_element(By.XPATH, f"//label[text()='{expected_name}']").click()
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

        # Test case of creating a duplicate prototype
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Create New Prototype']").click()
            expected_name = "Automation Test Prototype"
            self.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(expected_name)
            self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
            message = self.driver.find_element(By.XPATH, "(//label[contains(text(),'Duplicate prototype name')])[1]").text
            assert ("Duplicate prototype name" in message)
            self.logger.info("Success. Tested the case of creating duplicate prototype name.")
        except Exception as e:
            error_handler("warning", self.logger, "", "Failure. Duplicate prototoype name passed. Broken implementation.", e, "", "")

    def use_Code_dashboardConfig(self):
        self.base.beginOfTest_logFormat("use_Code_dashboardConfig")

        self.driver.find_element(By.XPATH, "//div[text()='Code']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Dashboard Config']").click()
        
        self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='1']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='3']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='4']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='8']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='9']").click()
        
        try:
            add_widget_btn = self.driver.find_element(By.XPATH, "//button[text()='Add widget']")
            if (add_widget_btn.is_displayed()):
                error_handler(self.logger, self.configInfo, "Failure. 'Add widget' button appeared when invalid boxes are selected",
                    "", self.configError["addWidget_invalidBoxes"], "Prototype")
        except:
            self.logger.info("Success. The 'Add widget' button did not appear when invalid boxes are selected.")
            
        try:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'border')][normalize-space()='1']").click()
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
            time.sleep(5)
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
                raise Exception("Did not find the span with text 'Builtin Testing'")
            else:
                assert (span.text == '"Builtin Testing"')
                self.logger.info("Success. Tested the case of editing the widget config text.")
        
        except Exception as e:
            error_handler("error", self.logger, "", "Failure. Cannot edit the widget config text.", e, "", "")