from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button = browser.find_element(By.TAG_NAME, "button")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "$100"))
print(price)
button.click()

# получаем значение атрибута для х
x = browser.find_element(By.ID, "input_value").text

# считаем функцию
y = str(math.log(abs(12 * math.sin(int(x)))))

# вводим в поле
field = browser.find_element(By.ID, "answer").send_keys(y)

# нажатие на кнопку
buttton = browser.find_element(By.ID, "solve").click()

# ждем загрузки страницы
time.sleep(1)