from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(driver, locator):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    ).click()

def input_text(driver, locator, text):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator)
    ).send_keys(text)
