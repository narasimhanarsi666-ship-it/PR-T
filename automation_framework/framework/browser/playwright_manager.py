from playwright.sync_api import sync_playwright
from framework.core.env_loader import load_env

env = load_env()

def start_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=env["HEADLESS"]=="true")
    context = browser.new_context()
    page = context.new_page()
    return playwright, browser, page
