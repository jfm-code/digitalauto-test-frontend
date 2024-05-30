from selenium import webdriver
import logging
import time

class Base():
    def setup_browser(self):
        # Setting up Chrome Browser
        self.driver = webdriver.Chrome()
        self.driver.get("https://digitalauto.netlify.app/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # Timeout = 10s

    def setup_logger(self):
        # Setting up Logger
        self.logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.txt')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO) # Do not print the DEBUG statements

    def clean_up(self):
        time.sleep(5)
        self.driver.close()
        self.logger.info("Closed the browser and ended the session.")