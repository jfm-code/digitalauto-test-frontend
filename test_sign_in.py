from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import logging
import unittest

class Test_SignIn(unittest.TestCase):
    def setUp(self):
        # Setting up Chrome Browser
        self.driver = webdriver.Chrome()
        self.driver.get("https://digitalauto.netlify.app/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # Timeout = 10s

        # Setting up Logger
        self.logger = logging.getLogger(__name__)
        self.fileHandler = logging.FileHandler('logfile.txt') 
        self.formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
        self.fileHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.fileHandler)  
        self.logger.setLevel(logging.INFO) # Do not print the DEBUG statements
        
        # Clicking the Sign In button
        try:
            self.driver.find_element(By.XPATH, "//div[text()='Sign in']").click()
            self.logger.info("Clicked the Sign In button")
        except Exception as e:
            self.logger.error(f"Failed to load the Sign In button: {e}")

    # Test Case 1
    def test_sign_in_invalid_password(self):
        try:
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("vuy4hc@bosch.com")
            self.logger.info("Entered email")
        except Exception as e:
            self.logger.error(f"Failed to open the Sign In pop up: {e}")
        wrong_pwd = "31280129850"
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(wrong_pwd)
        self.logger.info("Entered invalid password")
        self.driver.find_element(By.XPATH, "//div[@class='px-2']/div[4]").click()
        self.logger.info("Clicked the Submit button")
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']")))
            login_error = self.driver.find_element(By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']").text
            assert (login_error == "Invalid username or password")
            self.logger.info("Correctly identified invalid login attempt.")
        except Exception as e:
            self.logger.critical(f"Wrong password passed. Broken implementation: {e}")

    # Test Case 2
    def test_sign_in_valid_password(self):
        try:
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("vuy4hc@bosch.com")
            self.logger.info("Entered email")
            correct_pwd = "blablabla"
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(correct_pwd)
            self.logger.info("Entered valid password")
            self.driver.find_element(By.XPATH, "//div[@class='px-2']/div[4]").click()
            self.logger.info("Clicked the Submit button")
            try:
                user_button = self.driver.find_element(By.XPATH, "//div[@class='flex h-full text-xl items-center px-4 !w-fit max-w-fit text-center text-gray-400 cursor-pointer py-2 border-b-2 border-transparent']//*[name()='svg']")
                user_button.click()
                self.logger.info("Clicked the user icon")
                wait = WebDriverWait(self.driver, 2)
                wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text()='User Profile']")))
                dropdown_info = self.driver.find_element(By.XPATH, "//div[text()='User Profile']").text
                assert (dropdown_info == "User Profile")
                self.logger.info("Successfully signed in with the valid password.")
            except Exception as e:
                self.logger.critical(f"Failed to sign in with valid password. Broken implementation: {e}")
        except Exception as e:
            self.logger.error(f"Failed to open the Sign In pop up: {e}")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()
        self.logger.info("Closed the browser and ended the session.")
