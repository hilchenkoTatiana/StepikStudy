import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    time.sleep(2)

    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text
    sum = int(x1) + int(x2)
    select = Select(browser.find_element_by_id("dropdown"))
    print(sum)
    select.select_by_value(f"{sum}")
    browser.find_element_by_css_selector("[type='submit']").click()
    time.sleep(5)
finally:
    browser.close()

