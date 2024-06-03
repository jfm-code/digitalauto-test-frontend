import requests
from selenium.webdriver.common.by import By

def click_sign_in(driver, logger, config):
    try:
        logger.info("Started Signing In")
        driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
        logger.debug("Clicked the Sign In button")
    except Exception as e:
        error_message = "Failed to load the Sign In button"
        logger.error(f"{error_message}: {e}")
        email_content = "<!DOCTYPE html><html lang='en'><body><p>Failed to load the Sign In button.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Wait to see if the Sign In button can be loaded.</li></ol></p></body></html>"
        email_subject = "Error occured in the Home page"
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
    
def send_email(config, input_content, input_subject):
    url = config["email_url"]
    sending_obj = {
        "to": config["developer_email"],
        "subject": input_subject,
        "content": input_content
    }
    requests.post(url, json = sending_obj)