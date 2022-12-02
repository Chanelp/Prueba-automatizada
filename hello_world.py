import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class HolaMundo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        chrome = Service(r"C:\Users\ADMIN\Desktop\selenium\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=chrome)
        WebDriverWait(cls.driver, 10)

    def test_visitar_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    def test_hola(self):
        self.driver.get("https://www.google.com/")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output="report", report_name="holareport"))
