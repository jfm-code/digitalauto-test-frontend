import requests
import json
import os
import re
from urllib.parse import quote
from selenium.webdriver.common.by import By

def click_sign_in(driver, logger, config):
    try:
        driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
        logger.debug("Clicked the Sign In button")
    except Exception as e:
        error_message = "Failed to load the Sign In button"
        logger.error(f"{error_message}: {e}")
        email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to load the Sign In button.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Wait to see if the Sign In button can be loaded.</li></ol></p></body></html>"
        email_subject = "Error occurred in the Home page"
        send_email(config, email_content, email_subject)
        
def enter_name(driver, logger, config):
    driver.find_element(By.XPATH, "//input[@name='fullName']").send_keys(config["signUp_name"])
    logger.debug("Entered name")

def enter_email(driver, logger, config, email_input):
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_input)
    logger.debug("Entered email")

def enter_password(driver, logger, config, validity, mode):
    if (validity == "valid"):
        pass_to_enter = config["correct_password"]
    elif (validity == "invalid"):
        pass_to_enter = config["wrong_password"]
    if (mode == "first_enter"):
        path = "//input[@name='password']"
    elif (mode == "re_enter"):
        path = "//input[@name='confirmPassword']"
    driver.find_element(By.XPATH, path).send_keys(pass_to_enter)
    logger.debug(f"Entered {validity} password")

def submit_sign_in(driver, logger):
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    logger.debug("Clicked the Submit button")
    
def click_register(driver, logger):
    driver.find_element(By.XPATH, "//button[text()='Register']").click()
    logger.debug("Clicked the Register button")
    
def click_select_model(driver, logger):
    driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
    logger.debug("Clicked the Select Model button")

def click_prototype_library(driver, logger):
    driver.find_element(By.XPATH, "//label[text()='Prototype Library']").click()
    logger.debug("Clicked the Prototype Library button")
    
def click_create_prototype(driver, logger):
    driver.find_element(By.XPATH, "//button[text()='Create New Prototype']").click()
    logger.debug("Clicked the Create New Prototype button")
        
def error_handler(level, logger, configInfo, error_message, exception, email_content, place_occur):
    if (level == "critical"):
        logger.critical(f"{error_message}: {exception}")
        instance = get_instance_name(configInfo)
        email_subject = f"A critical error occurred in the {place_occur} page of {instance}"
        send_email(configInfo, email_content, email_subject, "now")
    elif (level == "error"):
        logger.error(f"{error_message}: {exception}")
    elif (level == "warning"):
        logger.warning(f"{error_message}: {exception}")
    
def delete_testing_object(type, driver, logger, configInfo):
    try:
        # Get ID and token
        if (type == "user"):
            id = get_user_info(configInfo, "id", "signUp")
            token = get_user_info(configInfo, "token", "admin")
        else:
            if (type == "model"):
                pattern = r"model/([a-f0-9]{24})"
            elif (type == "prototype"):
                pattern = r"/prototype/([a-f0-9]{24})/"
            current_url = driver.current_url
            match = re.findall(pattern, current_url)
            id = match[0]
            token = get_user_info(configInfo, "token", "signIn") 
        
        # Request for deletion
        instance = get_instance_name(configInfo)
        url = f"https://backend-core-{instance}.digital.auto/v2/{type}s/{id}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)
        if response.content:
            data = json.loads(response.content)
        else:
            data = {}
        
        # Check if the deletion is success
        if (data == {}):
            logger.info(f"Success. Deleted the testing {type} using Postman API.")
        else:
            raise Exception(f"Resulting JSON when deleting {type} is: {data}")
    
    except Exception as e:
        error_handler("warning", logger, "", f"Failure. Cannot use Postman API to delete the testing {type}.", e, "", "")

# Postman helper functions
def send_email(configInfo, email_content, email_subject, mode):
    if (mode == "now"):
        url = configInfo["email_url"]
        sending_obj = {
            "to": configInfo["developer_email"],
            "subject": email_subject,
            "content": email_content
        }
        requests.post(url, json = sending_obj)
    elif (mode == "later"):
        log_links = []
        for filename in os.listdir("logs"):
            file_path = os.path.join("logs", filename)
            if os.path.isfile(file_path):
                if (check_warning_error(file_path) is True):
                    file_link = upload_file(file_path)
                    log_links.append(file_link)
        if (len(log_links) > 0):
            html_content = "<!DOCTYPE html><html lang='en'><body><p>Below are the links of the log files that report errors and warnings. Please click each link to see the report.</p><ul>"
            for i, link in enumerate(log_links, start=1):
                html_content += f"<li><a href='{link}'>Log file {i}</a></li>"
            html_content += "</ul></body></html>"
            encoded_html_content = quote(html_content, safe='')
            send_email(configInfo, encoded_html_content, email_subject, "now")

def upload_file(file_path):
    with open(file_path, 'rb') as file:
        url = "https://upload.digitalauto.tech/upload/store-be"
        files = {'file': (file_path, file, 'multipart/form-data')}
        response = requests.post(url, files=files, verify=False)
        data = json.loads(response.content)
        return data["url"] # return the link to the document uploaded

def get_instance_name(configInfo):
    pattern = r"https://(.+?)\.digital\.auto/"
    instance = re.findall(pattern, configInfo["web_url"])
    if (instance[0] == "autowrx"):
        return "dev"
    else:
        return instance[0]

def check_warning_error(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            if ("ERROR" in line) or ("WARNING" in line):
                return True
        return False

def get_user_info(configInfo, element, mode):
    if (mode == "signIn"):
        email = configInfo["signIn_email"]
        password = configInfo["correct_password"]
    elif (mode == "signUp"):
        email = configInfo["signUp_email"]
        password = configInfo["correct_password"]
    elif (mode == "admin"):
        email = configInfo["admin_email"]   
        password = configInfo["admin_password"]
    instance = get_instance_name(configInfo)
    url = f"https://backend-core-{instance}.digital.auto/v2/auth/login"
    sending_obj = {"email": email, "password": password}
    response = requests.post(url, json=sending_obj)
    data = json.loads(response.content)
    if (element == "token"):
        if "tokens" in data and "access" in data["tokens"] and "token" in data["tokens"]["access"]:
            return data["tokens"]["access"]["token"]
        else:
            print("Unexpected response structure:", data)
            return None
    elif (element == "id"):
        if "user" in data and "id" in data["user"]:
            return data["user"]["id"]
        else:
            print("Unexpected response structure:", data)