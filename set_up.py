from selenium import webdriver
import logging
import time
from datetime import datetime
import json
import os

with open('info.json') as config_file:
    config = json.load(config_file)

class Base():
    def setup_browser(self):
        # Setting up Chrome Browser
        self.driver = webdriver.Chrome()
        try:
            self.driver.get(config["web_url"])
            self.driver.maximize_window()
            self.driver.implicitly_wait(10) # Timeout = 10s
            self.next = True
        except:
            self.logger.error("Wrong web URL, the site can't be reached.")
            self.next = False

    def setup_logger(self):
        # Setting up Logger
        timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
        log_file_name = f"logfile_{timestamp}.log"
        log_dir = config.get("log_dir", "logs")  # Default to "logs" if not specified
        os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists
        log_file_name = os.path.join(log_dir, f"logfile_{timestamp}.log")
        self.logger = logging.getLogger(config["test_file"])
        fileHandler = logging.FileHandler(log_file_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO) # Do not print the DEBUG statements
        #self.beginOfTest_logFormat()
        
    def beginOfTest_logFormat(self, test_name):
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.stream.write(f"Begin {test_name}\n")
                handler.flush()
        
    def endOfTest_logFormat(self):
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        duration_reformat = self.format_time(duration)
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.stream.write(f"Duration of the test case: {duration_reformat} seconds")
                handler.stream.write("\n------------------------------------------------------------------------------------\n")
                handler.flush()
                
    def start_timer(self):
        self.start_time = datetime.now()
        
    def format_time(self, input_time) -> str:
        total_seconds = int(input_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600) #returns a pair of numbers consisting of their quotient and remainder
        minutes, seconds = divmod(remainder, 60)
        # return f"{hours:02}:{minutes:02}:{seconds:02}"
        return f"{seconds:02}"

    def clean_up(self):
        time.sleep(5)
        self.driver.close()
        self.logger.info("Closed the browser and ended the session.")
        self.endOfTest_logFormat()
