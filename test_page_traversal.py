from util import *

class Test_PageTraversal(BaseTest, unittest.TestCase):
    
    # Test case 1: 
    def test_link_partners(self):
        self.base.beginOfTest_logFormat("test_link_partners")
        if (self.next is True):
            try:
                self.driver.find_element(By.XPATH, "//a[@href='https://www.bosch.com/']").click()
                windows_opened = self.driver.window_handles
                self.driver.switch_to.window(windows_opened[1])
                assert (self.driver.current_url == self.configInfo["bosch_link"])
                self.logger.info("Successs. Opened and verified Bosch Link")
            except Exception as e:
                error_message = "Failure. Cannot open Bosch Link in the Home Page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["bosch_link_failed"]
                email_subject = get_emailSubject("Home")
                send_email(self.configInfo, email_content, email_subject)
                
            self.driver.switch_to.window(windows_opened[0]) # Switch back to parent window
            try:
                self.driver.find_element(By.XPATH, "//a[@href='https://www.covesa.global']").click()
                windows_opened = self.driver.window_handles
                self.driver.switch_to.window(windows_opened[2])
                assert (self.driver.current_url == self.configInfo["covesa_link"])
                self.logger.info("Successs. Opened and verified Covesa Link")
            except Exception as e:
                error_message = "Failure. Cannot open Covesa Link in the Home Page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["covesa_link_failed"]
                email_subject = get_emailSubject("Home")
                send_email(self.configInfo, email_content, email_subject)
                
            self.driver.switch_to.window(windows_opened[0])
            try:
                self.driver.find_element(By.XPATH, "//a[@href='https://www.eclipse.org']").click()
                windows_opened = self.driver.window_handles
                self.driver.switch_to.window(windows_opened[3])
                assert (self.driver.current_url == self.configInfo["eclipse_link"])
                self.logger.info("Successs. Opened and verified Eclipse Partner Link")
            except Exception as e:
                error_message = "Failure. Cannot open Eclipse Link in the Home Page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["eclipse_link_failed"]
                email_subject = get_emailSubject("Home")
                send_email(self.configInfo, email_content, email_subject)
                
            self.driver.switch_to.window(windows_opened[0])
            try:
                self.driver.find_element(By.XPATH, "//a[@href='https://ferdinand-steinbeis-institut.de']").click()
                windows_opened = self.driver.window_handles
                self.driver.switch_to.window(windows_opened[4])
                assert (self.driver.current_url == self.configInfo["institut_link"])
                self.logger.info("Successs. Opened and verified Ferdinand Steinbeis Institut Partner Link")
            except Exception as e:
                error_message = "Failure. Cannot open Ferdinand Steinbeis Institut Link in the Home Page"
                self.logger.error(f"{error_message}: {e}")
                email_content = self.configError["institut_link_failed"]
                email_subject = get_emailSubject("Home")
                send_email(self.configInfo, email_content, email_subject)
