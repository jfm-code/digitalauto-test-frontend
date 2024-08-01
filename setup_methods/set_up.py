from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
from datetime import datetime
import json
import os

with open('info.json') as config_file:
    configInfo = json.load(config_file)

class Base():
    def setup_browser(self):
        # Setting up Headless mode
        headless_mode = os.getenv("HEADLESS", "false").lower() == "true"
        options = Options()
        if headless_mode:
            options.add_argument("--headless=new")
            self.logger.info("Running in headless mode")
            
        # Setting up Chrome Browser
        self.driver = webdriver.Chrome(options=options)
        try:
            self.driver.get(configInfo["web_url"])
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)  # Timeout = 10s
            self.next = True
        except:
            self.logger.error("Wrong web URL, the site can't be reached.")
            self.next = False

    def setup_logger(self):
        timestamp = time.strftime("%Y-%m-%d %H.%M.%S")
        log_dir = configInfo.get("log_dir", "logs")  # Default to "logs" if not specified
        os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists
        self.log_file_name = os.path.join(log_dir, f"{timestamp}.log")
        self.logger = logging.getLogger()
        fileHandler = logging.FileHandler(self.log_file_name)
        formatter = logging.Formatter(f"{timestamp} :%(levelname)s: %(filename)s :%(message)s")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.INFO) # Do not print the DEBUG statements
        
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
                
    def logSummarizer(self):
        with open(self.log_file_name, 'r') as fileReader:
            countFailed = 0
            numOfTest = 0
            failed_tests = []
            for line in fileReader.readlines():
                if ("Begin" in line):
                    test_name = line[6:]
                if ("Success" in line) or ("Failure" in line):
                    numOfTest += 1
                if ("ERROR" in line) or ("CRITICAL" in line) or ("WARNING" in line):
                    countFailed += 1
                    failed_tests.append(test_name)
                    failed_tests.append(line[21:])
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    handler.stream.write(f"INSTANCE: {configInfo["web_url"]}\n")
                    handler.stream.write("SUMMARY:\n")
                    handler.stream.write(f"\tNumber of FAILED test cases: {countFailed} / {numOfTest}\n")
                    if (len(failed_tests) > 0):
                        handler.stream.write("\tTest cases that failed:\n")
                        for i in range(0, len(failed_tests), 2):
                            handler.stream.write(f"\t\t{failed_tests[i]}")
                            handler.stream.write(f"\t\t\t{failed_tests[i+1]}")
    
    def start_timer(self):
        self.start_time = datetime.now()
        
    def format_time(self, input_time) -> str:
        total_seconds = int(input_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600) # returns a pair of numbers consisting of their quotient and remainder
        minutes, seconds = divmod(remainder, 60)
        return f"{seconds:02}" # If we want to get hours and minutes -> f"{hours:02}:{minutes:02}:{seconds:02}"

    def clean_up(self):
        time.sleep(5)
        self.driver.close()
        self.logger.info("Closed the browser and ended the session.")
        self.endOfTest_logFormat()
