import os.path
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    WebDriverWait(browser, 5).until(EC.visibility_of(browser.find_element_by_css_selector("input[name='firstname']")))
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Test1")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("Test2")
    browser.find_element_by_css_selector("input[name='email']").send_keys("Test@test.ten")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '../text.txt')
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(5)
finally:
    browser.quit()

