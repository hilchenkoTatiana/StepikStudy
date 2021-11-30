import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    time.sleep(5)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("[type='submit']").click()
    time.sleep(20)

finally:
    browser.close()



