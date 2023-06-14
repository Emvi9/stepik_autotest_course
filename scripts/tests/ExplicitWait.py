import time, os, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(('id', 'price'), text_='$100'))
    browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element(By.ID, 'input_value').text)

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    button_solve = browser.find_element(By.ID, 'solve')
    button_solve.click()

finally:
    time.sleep(10)
    print('[INFO] # Выполнено успешно.')  # 29.031848933295468 ответ
    browser.quit()



