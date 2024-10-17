from utils.page_elements import PageElements
from utils.helper_methods import click_element, input_text
import pytest

@pytest.mark.usefixtures("setup_browser")
class TestRegistration:

    def test_user_registration(self, setup_browser):
        driver = setup_browser
        click_element(driver, PageElements.SIGN_IN_BUTTON)
        input_text(driver, PageElements.EMAIL_INPUT, "testuser@example.com")
        click_element(driver, PageElements.CREATE_ACCOUNT_BUTTON)

        input_text(driver, PageElements.FIRST_NAME_INPUT, "Test")
        input_text(driver, PageElements.LAST_NAME_INPUT, "User")
        input_text(driver, PageElements.PASSWORD_INPUT, "password123")
        click_element(driver, PageElements.SUBMIT_ACCOUNT)

        assert "My account" in driver.title, "User registration failed."
