from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import json
from set_up import Base
import requests

class Test_SignIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = Base()
        cls.base.setup_logger()
    # Making sure that logger is configured only once

    def setUp(self):
        self.base.setup_browser()
        self.driver = self.base.driver
        self.logger = self.base.logger
        with open('info.json') as config_file:
            self.config = json.load(config_file)

    def tearDown(self):
        self.base.clean_up()
    
    # Clicking the Sign In button
    def click_sign_in(self):  
        try:
            self.logger.info("Started Signing In")
            self.driver.find_element(By.XPATH, "//div[text()='Sign in']").click()
            self.logger.debug("Clicked the Sign In button")
        except Exception as e:
            self.logger.error(f"Failed to load the Sign In button: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to load the Sign In button.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Wait to see if the Sign In button can be loaded.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)

    # Test Case 1
    def test_sign_in_invalid_password(self):
        self.click_sign_in()
        
        try:
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(self.config["email"])
            self.logger.debug("Entered email")
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.config["wrong_password"])
            self.logger.debug("Entered invalid password")
        except Exception as e:
            self.logger.error(f"Failed to open the Sign In pop up: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)
 
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']")))
            login_error = self.driver.find_element(By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']").text
            assert (login_error == "Invalid username or password")
            self.logger.info("Successfully tested the invalid login attempt.")
        except Exception as e:
            self.logger.critical(f"Wrong password passed. Broken implementation: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Wrong password passed. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email but wrong password.</li><li>Click Sign In to see if the wrong password is accepted</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)

    # Test Case 2
    def test_sign_in_valid_password(self):
        self.click_sign_in()
        
        try:
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(self.config["email"])
            self.logger.debug("Entered email")
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.config["correct_password"])
            self.logger.debug("Entered valid password")
            self.driver.find_element(By.XPATH, "//div[@class='px-2']/div[4]").click()
            self.logger.debug("Clicked the Submit button")
        except Exception as e:
            self.logger.error(f"Failed to open the Sign In pop up: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to open the Sign In pop up.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Wait to see if the Sign In pop up can be loaded.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)

        try:
            user_button = self.driver.find_element(By.XPATH, "//div[@class='flex h-full text-xl items-center px-4 !w-fit max-w-fit text-center text-gray-400 cursor-pointer py-2 border-b-2 border-transparent']//*[name()='svg']")
            user_button.click()
            self.logger.debug("Clicked the user icon")
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text()='User Profile']")))
            dropdown_info = self.driver.find_element(By.XPATH, "//div[text()='User Profile']").text
            assert (dropdown_info == "User Profile")
            self.logger.info("Successfully signed in with the valid password.")
        except Exception as e:
            self.logger.critical(f"Failed to sign in with valid password. Broken implementation: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Wrong password passed. Broken implementation.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click the Sign In button</li><li>Enter the correct email and correct password.</li><li>Click Sign In to see if the correct password is accepted</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)