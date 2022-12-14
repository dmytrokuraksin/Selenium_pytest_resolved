from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//div[contains(@class, "first_class")]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//div[contains(@class, "second_class")]/input')
    input2.send_keys("Petrov")
    input4 = browser.find_element(By.XPATH, '//div[contains(@class, "third_class")]/input')
    input4.send_keys("email")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "buttonb.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()