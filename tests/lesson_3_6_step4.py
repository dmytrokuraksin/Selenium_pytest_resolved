import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('page', ["895"])
class TestPage():
    def test_param(self, browser, page):
        link = f"https://stepik.org/lesson/236{page}/step/1"
        browser.get(link)
        time.sleep(20)
        # считаем по формуле
        answer = math.log(int(time.time()))

        # находим поле ввода
        field = browser.find_element(By.ID, "ember90")
        field.send_keys(answer)

        # нажимаем кнопку Отправить
        button = browser.find_element(By.XPATH, "//button[text()='Отправить']")
        button.click()

        # .smart-hints__hint
        # , "896","897","898","899","903","904","905"