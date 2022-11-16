import unittest
from main import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import warnings

class SeleniumTests(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        # Set up seleniums
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        self.driver = None
        self.delay_time = 5
        try:
            self.driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=options,
            )
            self.driver.set_page_load_timeout(10)
            self.driver.get(f"http://flask-app:5000/")
            self.driver.implicitly_wait('1')
        except WebDriverException as e:
            self.driver.browser.quit()
            if "ERR_CONNECTION_REFUSED" not in e.msg:
                print(e)

    def test_with_correct_input(self):
        print("starting")
        uname = self.driver.find_element(By.ID, "uname")
        print("get uname")
        uname.send_keys("john")
        print("uname sendkey")

        self.driver.find_element(By.ID, "btn").click()
        print("click")
        
        self.driver.implicitly_wait('1')

        result = self.driver.find_element(By.ID, "clean")
        self.assertEqual(result.text , "john")

    def test_with_false_input(self):
        try: 
            self.driver.get(f"http://flask-app:5000/result")
            print("starting")
            uname = self.driver.find_element(By.ID, "uname")
            print("get uname")  
            uname.send_keys("<a>lol</a>")
            print("uname sendkey")

            self.driver.find_element(By.ID, "btn").click()
            print("click")
            
            self.driver.implicitly_wait('1')

            result = self.driver.find_element(By.ID, "clean")
            self.assertEqual(result.text , "<a>lol</a>")
        except:
            # fail
            self.assertEqual(True, False)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()