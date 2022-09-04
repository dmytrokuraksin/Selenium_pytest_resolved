from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.XPATH, '//button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # получаем значение атрибута для х
    x = browser.find_element(By.ID, "input_value").text

    # считаем функцию
    y = str(math.log(abs(12 * math.sin(int(x)))))

    # вводим в поле
    field = browser.find_element(By.ID, "answer").send_keys(y)

    # нажатие на кнопку
    buttton = browser.find_element(By.TAG_NAME, "button").click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()