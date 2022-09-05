import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//div[contains(@class, "first_class")]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[contains(@class, "second_class")]/input')
        input2.send_keys("Petrov")
        input4 = browser.find_element(By.XPATH, '//div[contains(@class, "third_class")]/input')
        input4.send_keys("email")
        button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//div[contains(@class, "first_class")]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[contains(@class, "second_class")]/input')
        input2.send_keys("Petrov")
        input4 = browser.find_element(By.XPATH, '//div[contains(@class, "third_class1")]/input')
        input4.send_keys("email")
        button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
    time.sleep(10)
