from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    treasure = browser.find_element(By.ID, 'treasure')
    # получаем значение атрибута для х
    x = treasure.get_attribute("valuex")
    # считаем функцию
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input4 = browser.find_element(By.ID, "answer")
    input4.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button0 = browser.find_element(By.ID, "robotsRule")
    button0.click()

    button1 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button1.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()