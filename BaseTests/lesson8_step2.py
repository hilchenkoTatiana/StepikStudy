import math
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    WebDriverWait(browser, 5).until(EC.visibility_of(browser.find_element_by_id("input_value")))
    x = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(x)
    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    submit_button.click()
    time.sleep(5)

finally:
    browser.close()