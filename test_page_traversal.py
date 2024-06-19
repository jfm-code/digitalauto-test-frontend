from util import *

class Test_PageTraversal(BaseTest, unittest.TestCase):
    def test_open_links(self):
        if (self.next is True):
            self.open_partner_link()
    
    def open_partner_link(self):
        self.base.beginOfTest_logFormat("open_partner_link")
        try:
            self.driver.find_element(By.XPATH, "//a[@href='https://www.bosch.com/']").click()
            windows_opened = self.driver.window_handles
            self.driver.switch_to.window(windows_opened[1])
            assert (self.driver.current_url == self.configInfo["bosch_link"])
            self.logger.info("Success. Opened and verified Bosch Link")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot open Bosch Link in the Home Page", e,
                self.configError["bosch_link_failed"], "Home")
            
        self.driver.close()
        self.driver.switch_to.window(windows_opened[0])

        try:
            self.driver.find_element(By.XPATH, "//a[@href='https://www.covesa.global']").click()
            windows_opened = self.driver.window_handles
            self.driver.switch_to.window(windows_opened[1])
            assert (self.driver.current_url == self.configInfo["covesa_link"])
            self.logger.info("Success. Opened and verified Covesa Link")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot open Covesa Link in the Home Page", e,
                self.configError["covesa_link_failed"], "Home")
            
        self.driver.close()
        self.driver.switch_to.window(windows_opened[0])
        
        try:
            self.driver.find_element(By.XPATH, "//a[@href='https://www.eclipse.org']").click()
            windows_opened = self.driver.window_handles
            self.driver.switch_to.window(windows_opened[1])
            assert (self.driver.current_url == self.configInfo["eclipse_link"])
            self.logger.info("Success. Opened and verified Eclipse Partner Link")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot open Eclipse Link in the Home Page", e,
                self.configError["eclipse_link_failed"], "Home")
        
        self.driver.close()
        self.driver.switch_to.window(windows_opened[0])

        try:
            self.driver.find_element(By.XPATH, "//a[@href='https://ferdinand-steinbeis-institut.de']").click()
            windows_opened = self.driver.window_handles
            self.driver.switch_to.window(windows_opened[1])
            assert (self.driver.current_url == self.configInfo["institut_link"])
            self.logger.info("Success. Opened and verified Ferdinand Steinbeis Institut Partner Link")
        except Exception as e:
            error_handler(self.logger, self.configInfo, "Failure. Cannot open Ferdinand Steinbeis Institut Link in the Home Page", e,
                self.configError["institut_link_failed"], "Home")

    