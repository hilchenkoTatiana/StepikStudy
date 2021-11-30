import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    time.sleep(5)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("[type='submit']").click()
    time.sleep(20)

finally:
    browser.close()
