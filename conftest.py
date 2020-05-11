import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es is available")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    browser.get(link)
    # try:
    #     wrong_page = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//a[@onclick='javascript:history.go(-1);']"))
    #     )
    #     if wrong_page is not None:
    #         raise pytest.UsageError("--language does not exist")
    # except:
    #     print("Language does not exist")
    yield browser
    print("\nquit browser..")
    browser.quit()
