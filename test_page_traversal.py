from util import *

class Test_PageTraversal(BaseTest, unittest.TestCase):
    # NOT DONE, WAIT FOR CONSISTENCY IN THE HREF LINK AND ACTUAL LINK
    def test_open_links(self):
        if (self.next is True):
            self.verify_link("Bosch")
            self.verify_link("Covesa")
            self.verify_link("Eclipse")
            self.verify_link("Ferdinand_Steinbeis_Institut")
                        
    def verify_link(self, name):
        self.base.beginOfTest_logFormat(f"open_{name}_link")
        try:
            page_url = self.configInfo[f"{name}_link"]
            self.driver.find_element(By.XPATH, f"//a[@href='{page_url}']").click()
            windows_opened = self.driver.window_handles
            self.driver.switch_to.window(windows_opened[1])
            assert (self.driver.current_url == page_url)
            self.logger.info(f"Success. Opened and verified {name} Link")
            self.driver.close()
            self.driver.switch_to.window(windows_opened[0])
        except Exception as e:
            error_handler(self.logger, self.configInfo, f"Failure. Cannot open {name} Link in the Home Page", e,
                self.configError[f"{name}_link_failed"], "Home")
