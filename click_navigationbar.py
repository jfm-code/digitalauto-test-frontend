import requests
from selenium.webdriver.common.by import By

def click_sign_in(driver, logger, config):
    try:
        logger.info("Started Signing In")
        driver.find_element(By.XPATH, "//div[text()='Sign in']").click()
        logger.debug("Clicked the Sign In button")
    except Exception as e:
        logger.error(f"Failed to load the Sign In button: {e}")
        url = config["email_url"]
        sending_obj = {
            "to": config["developer_email"],
            "subject": "Error occurred in the Home page",
            "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to load the Sign In button.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Wait to see if the Sign In button can be loaded.</li></ol></p></body></html>"
        }
        requests.post(url, json=sending_obj)
