import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')


browser.find_element(By.CSS_SELECTOR, 'div[class="form-group"] button[class="btn btn-primary"]').click()


time.sleep(1)

alert = browser.switch_to.alert
alert.accept()

time.sleep(1.5)

x = int(browser.find_element(By.ID, 'input_value').text)


def calc(x):
    return math.log(abs(12 * math.sin(x)))


input_elem = browser.find_element(By.ID, 'answer')
input_elem.send_keys(calc(x))


browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(10)
browser.quit()

