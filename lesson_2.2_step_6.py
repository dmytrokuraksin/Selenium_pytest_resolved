from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    browser.execute_script("window.scrollBy(0, 50);")
    input4 = browser.find_element(By.ID, "answer")
    input4.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button0 = browser.find_element(By.ID, "robotsRule")
    button0.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()