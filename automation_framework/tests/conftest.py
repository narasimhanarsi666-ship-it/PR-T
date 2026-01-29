import pytest
from framework.browser.playwright_manager import start_browser

@pytest.fixture
def page():
    playwright,browser,page=start_browser()
    yield page
    browser.close()
    playwright.stop()
