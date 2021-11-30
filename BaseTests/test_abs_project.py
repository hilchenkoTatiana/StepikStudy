import unittest

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAbs(unittest.TestCase):
    @pytest.fixture
    def test_abs1(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of(browser.find_element_by_css_selector("input.form-control.first")))
        browser.find_element_by_css_selector("div.first_block input.form-control.first").send_keys("Test")
        browser.find_element_by_css_selector("div.first_block input.form-control.second").send_keys("Test")
        browser.find_element_by_css_selector("div.first_block input.form-control.third").send_keys("Test")
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text,
                         "Congratulations! You have successfully registered!",
                         "First test has not same text")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # закрываем браузер после всех манипуляций

    @pytest.fixture()
    def test_abs2(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of(browser.find_element_by_css_selector("input.form-control.first")))
        browser.find_element_by_css_selector("div.first_block input.form-control.first").send_keys("Test")
        browser.find_element_by_css_selector("div.first_block input.form-control.second").send_keys("Test")
        browser.find_element_by_css_selector("div.first_block input.form-control.third").send_keys("Test")
        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text,
                         "Congratulations! You have successfully registered!",
                         "Second test has not same text")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # закрываем браузер после всех манипуляций


if __name__ == "__main__":
    unittest.main()
