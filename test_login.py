from utils.page_elements import PageElements
from utils.helper_methods import click_element, input_text
import pytest

@pytest.mark.usefixtures("setup_browser")
class TestLogin:

    def test_user_login(self, setup_browser):
        driver = setup_browser
        click_element(driver, PageElements.SIGN_IN_BUTTON)
        
        input_text(driver, PageElements.LOGIN_EMAIL_INPUT, "testuser@example.com")
        input_text(driver, PageElements.LOGIN_PASSWORD_INPUT, "password123")
        click_element(driver, PageElements.LOGIN_BUTTON)

        assert "My account" in driver.title, "User login failed."
