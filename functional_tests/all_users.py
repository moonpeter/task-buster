# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/moonpeter/Downloads/chromedriver_4")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get("http://localhost:9999")
        self.assertIn("The install worked successfully! Congratulations!", self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
