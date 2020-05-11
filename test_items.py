from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_should_be_available(browser):
    btn_available = None
    # noinspection PyBroadException
    try:
        btn_available = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
    except Exception:
        print('Add to basket button is not found')
    assert btn_available is not None, "Add to basket button is not available"
