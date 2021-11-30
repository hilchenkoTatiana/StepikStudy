import math
import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestProject:
    message = ""

    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"])
    def test_links(self, browser, links):
        answer = math.log(int(time.time()))
        browser.get(str(links))
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "textarea")))
        browser.find_element(By.TAG_NAME, "textarea") \
            .send_keys(str(answer))
        submit_button = browser.find_element(By.CLASS_NAME, "submit-submission")
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(submit_button))
        submit_button.click()
        time.sleep(5)
        # WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located(browser.find_element(By.CSS_SELECTOR, "div>pre")))
        answer = browser.find_element(By.CSS_SELECTOR, "div>pre").text
        if answer != "Correct!":
            self.message += answer
            assert self.message == False
        print("\n" + self.message)


if __name__ == "__main__":
    unittest.main()
