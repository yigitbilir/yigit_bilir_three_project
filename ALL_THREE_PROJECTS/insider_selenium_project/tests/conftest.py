import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    """Setup and teardown browser driver"""
    browser = request.config.getoption("--browser").lower()
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use 'chrome' or 'firefox'")
    
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test failure and take screenshot"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                from datetime import datetime
                import os
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                
                test_name = item.name
                screenshot_path = os.path.join(screenshot_dir, f"FAILED_{test_name}_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
                print(f"\nTest failed! Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"Failed to take screenshot: {str(e)}")
