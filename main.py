import selenium, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = selenium.webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
driver.implicitly_wait(5)


def calculate(n):
    return math.log(abs(12 * math.sin(n)))


try:
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element(('id', 'price'), '$100'))
    book_btn = driver.find_element(By.ID, 'book')
    book_btn.click()

    n = int(driver.find_element(By.ID, 'input_value').text)

    form_input = driver.find_element(By.ID, 'answer')
    form_input.send_keys(calculate(n))

    solve_btn = driver.find_element(By.ID, 'solve')
    solve_btn.click()
finally:
    time.sleep(5)
    print('[INFO] Выполнено успешно.')
    driver.quit()
