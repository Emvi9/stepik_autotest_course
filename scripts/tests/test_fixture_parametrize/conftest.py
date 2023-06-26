import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('headless')  with this option u won't see how browser opens
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


