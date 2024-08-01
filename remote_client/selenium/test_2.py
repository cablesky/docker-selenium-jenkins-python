import unittest
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://firefox:4444/wd/hub",options=webdriver.FirefoxOptions())
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        driver = self.driver
        self.assertIn("Python", self.driver.title)
        elem = driver.find_element("name","q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_go_to_about(self):
        aboutLink = self.driver.find_element("xpath","//li[@id='about']/a")
        self.assertEqual("About", aboutLink.text)
        aboutLink.click()
        self.assertIn("About", self.driver.title)

    def test_go_to_community(self):
        communityLink = self.driver.find_element("xpath","//li[contains(@class, 'shop-meta')]//a")
        communityLink.click()
        title = self.driver.find_element("xpath","//h1[@class='call-to-action']//a")
        self.assertEqual("Python’s community is vast", title.text)

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
