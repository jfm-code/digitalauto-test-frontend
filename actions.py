import requests
import json
from selenium.webdriver.common.by import By

def click_sign_in(driver, logger, config):
    try:
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
    
def click_select_model(driver, logger):
    driver.find_element(By.CSS_SELECTOR, "a[href='/model']").click()
    logger.debug("Clicked the Select Model button")

def click_prototype_library(driver, logger):
    driver.find_element(By.XPATH, "//label[text()='Prototype Library']").click()
    logger.debug("Clicked the Prototype Library button")
    
def click_create_prototype(driver, logger):
    driver.find_element(By.XPATH, "//button[text()='Create New Prototype']").click()
    logger.debug("Clicked the Create New Prototype button")

# def cannotOpenPopUp_errorHandler(exception, logger, configError, configInfo, mode):
#     if (mode == "sign_in"):
#         error_message = "Failure. Cannot open the Sign In pop up"
#         email_content = configError["cannot_open_signIn_popup"]
#     elif (mode == "register"):
#         error_message = "Failure. Cannot open the Register pop up"
#         email_content = configError["cannot_open_register_popup"]
#     logger.error(f"{error_message}: {exception}")
#     email_subject = get_emailSubject("Home")
#     send_email(configInfo, email_content, email_subject)
    
def error_handler(logger, configInfo, error_message, exception, email_content, place_occur):
    logger.error(f"{error_message}: {exception}")
    email_subject = f"An error occured in the {place_occur} page"
    send_email(configInfo, email_content, email_subject)

# Postman helper functions
def send_email(config, email_content, email_subject):
    url = config["email_url"]
    sending_obj = {
        "to": config["developer_email"],
        "subject": email_subject,
        "content": email_content
    }
    requests.post(url, json = sending_obj)
    
def get_user_info(config, element, mode):
    if (mode == "signIn"):
        email = config["signIn_email"]
        password = config["correct_password"]
    elif (mode == "signUp"):
        email = config["signUp_email"]
        password = config["correct_password"]
    elif (mode == "admin"):
        email = config["admin_email"]
        password = config["admin_password"]
    url = "https://backend-core-etas.digital.auto/v2/auth/login"
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

def delete_model(token, model_id):
    url = f"https://backend-core-etas.digital.auto/v2/models/{model_id}"
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(url, headers=headers)
    
def delete_prototype(token, prototype_id):
    url = f"https://backend-core-etas.digital.auto/v2/prototypes/{prototype_id}"
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(url, headers=headers)
    
def delete_user(admin_token, user_id):
    url = f"https://backend-core-etas.digital.auto/v2/users/{user_id}"
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.delete(url, headers=headers)
    # data = json.loads(response.content)
    # return data

