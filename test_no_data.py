from util import *

class Test_NoData(BaseTest, unittest.TestCase):

    # Test Case 1
    def test_numOf_models(self):
        try:
            self.logger.info("Started counting the model components in model page")
            self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click()
            self.logger.debug("Clicked the Select Model button")
            models = self.driver.find_elements(By.CSS_SELECTOR, "a[class='mr-2 w-full']")
            assert (len(models) > 0)
            self.logger.info("Successfully tested the number of model components in model page")
        except Exception as e:
            self.logger.error(f"Failed to load the model components in model page: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Select Vehicle Models page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to load the model components in model page.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click on the 'Select Model' button.</li><li>Count the number of models.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)
    
    # Test Case 2
    def test_numOf_prototypes(self):
        try:
            self.logger.info("Started counting the prototype components in home page")
            prototypes = self.driver.find_elements(By.XPATH, "//div/div[@class='w-full h-full relative']/div/a/img")
            assert (len(prototypes) > 0)
            self.logger.info("Successfully tested the number of prototype components in home page")
        except Exception as e:
            self.logger.error(f"Failed to load the prototype components in home page: {e}")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Home page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to load the prototype components in home page.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Count the number of prototypes.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)
    
    # Test Case 3
    def test_redPin_exist(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div[class='flex h-full items-center w-full']").click() # Click the Select Model Button
            self.logger.debug("Clicked the Select Model button")
            self.driver.find_element(By.CSS_SELECTOR, "img[src='https://firebasestorage.googleapis.com/v0/b/digital-auto.appspot.com/o/media%2FE-Car_Full_Vehicle.png?alt=media&token=9c9d4cb4-fee0-42e3-bbb1-7feaa407cc8e']").click()
            self.logger.debug("Clicked the ACME Car (EV) v0.1 Model")
            self.driver.find_element(By.XPATH, "//div/div[text()='Vehicle APIs']").click()
            self.logger.debug("Clicked the Vehicle APIs button")
            self.driver.find_element(By.CSS_SELECTOR, "div[style$='cursor: default; position: relative;']")
            # Canvas that have pins will have this styling attribute
            # If I have the coordinate of one pin then I can hover on it, this styling attribute only appears when we hover once
            # Since I don't have the coord of the pin, this will always throw exception
        except NoSuchElementException:
            self.logger.error("Failed to load the red pins on the canvas")
            url = self.config["email_url"]
            sending_obj = {
                "to": self.config["developer_email"],
                "subject": "Error occured in the Vehicle APIs page",
                "content": "<!DOCTYPE html><html lang='en'><body><p>Failed to load the red pins on the canvas.</p><p>Steps to Reproduce:</p><ol><li>Navigate to the home page.</li><li>Click on the 'Select Model' button.</li><li>Click on the 'ACME Car (EV) v0.1 Model' image.</li><li>Click on the 'Vehicle APIs' button.</li><li>Check for the existence of red pins on the canvas.</li></ol></p></body></html>"
            }
            requests.post(url, json = sending_obj)
            