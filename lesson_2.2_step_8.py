from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    input1.send_keys("TEST")
    input2 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    input2.send_keys("TEST")
    input4 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    input4.send_keys("TEST")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    # нажимаем сабмит
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(6)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()