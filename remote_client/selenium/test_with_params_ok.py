import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities
import os
browser = os.getenv("Browser") 

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        if browser == "FIREFOX":
            options=webdriver.FirefoxOptions()
        else:
            options=webdriver.ChromeOptions()        

        capabilities = getattr(desired_capabilities.DesiredCapabilities, browser).copy()
        options.set_capability('browserName', capabilities['browserName'])

        self.driver = webdriver.Remote(command_executor="http://selenium-hub:4444", options=options)     

        self.driver.get("http://www.python.org")

#     def setUp2(self):
#         self.driver = webdriver.Remote(
#             if browser == "FIREFOX":
#                 command_executor='http://firefox:4444/wd/hub', 
#                 options=webdriver.FirefoxOptions()
#             else:
#                 command_executor='http://chrome:4444/wd/hub',
#                 options=webdriver.ChromeOptions()
                
#             #command_executor='http://firefox:4444/wd/hub', 

#             #options=webdriver.FirefoxOptions()
# )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()