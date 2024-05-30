from selenium import webdriver
import logging
import time
import json
import os

with open('user_info.json') as config_file:
            config = json.load(config_file)

class Base():
    def setup_browser(self):
        # Setting up Chrome Browser
        self.driver = webdriver.Chrome()
        self.driver.get(config["web_url"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # Timeout = 10s

    def setup_logger(self):
        # Setting up Logger
        timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
        log_file_name = f"{config['log_file']}_{timestamp}.log"
        log_dir = config.get("log_dir", "logs")  # Default to "logs" if not specified
        os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists
        log_file_name = os.path.join(log_dir, f"{config['log_file']}_{timestamp}.log")
        self.logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler(log_file_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO) # Do not print the DEBUG statements

    def clean_up(self):
        time.sleep(5)
        self.driver.close()
        self.logger.info("Closed the browser and ended the session.")