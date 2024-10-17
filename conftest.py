import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    yield driver
    driver.quit()
