from utils.page_elements import PageElements
from utils.helper_methods import click_element
import pytest

@pytest.mark.usefixtures("setup_browser")
class TestNavigation:

    def test_navigate_women_section(self, setup_browser):
        driver = setup_browser
        click_element(driver, PageElements.WOMEN_CATEGORY)
        assert "Women" in driver.title, "Navigation to Women category failed."

    def test_navigate_dresses_section(self, setup_browser):
        driver = setup_browser
        click_element(driver, PageElements.DRESSES_CATEGORY)
        assert "Dresses" in driver.title, "Navigation to Dresses category failed."

    def test_navigate_tshirts_section(self, setup_browser):
        driver = setup_browser
        click_element(driver, PageElements.TSHIRTS_CATEGORY)
        assert "T-shirts" in driver.title, "Navigation to T-shirts category failed."
