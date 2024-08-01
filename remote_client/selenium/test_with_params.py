from copy import copy
import unittest
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.keys import Keys

import os
browser = os.getenv("Browser") 

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        capabilities = getattr(desired_capabilities.DesiredCapabilities, browser).copy()
        self.driver = webdriver.Remote(command_executor="http://selenium-hub:4444", desired_capabilities=capabilities)     
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        driver = self.driver
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
