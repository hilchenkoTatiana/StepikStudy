import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(expected_conditions.
                                     text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element_by_id("book").click()
    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    x = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(5)
finally:
    browser.quit()
