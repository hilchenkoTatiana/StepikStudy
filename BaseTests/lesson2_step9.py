import math

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    first_button = browser.find_element_by_css_selector("button[type='submit']")
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of(first_button))
    first_button.click()
    alert = browser.switch_to.alert
    alert.accept()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of(browser.find_element_by_id("input_value")))
    x = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    browser.quit()

