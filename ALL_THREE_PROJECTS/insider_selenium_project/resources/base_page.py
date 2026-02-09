import os
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasePage:
    """Base page class containing common methods for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
        
    def find_element(self, locator):
        """Find a single element with explicit wait"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.take_screenshot(f"element_not_found_{locator[1]}")
            raise
            
    def find_elements(self, locator):
        """Find multiple elements with explicit wait"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            self.take_screenshot(f"elements_not_found_{locator[1]}")
            raise
            
    def click_element(self, locator):
        """Click on an element with explicit wait for clickability"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            self.take_screenshot(f"click_failed_{locator[1]}")
            raise
            
    def send_keys_to_element(self, locator, text):
        """Send keys to an element"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.take_screenshot(f"send_keys_failed_{locator[1]}")
            raise

    def select_from_dropdown_by_select_class(self, dropdown_id, option_text):
        self.wait_for_page_load()
        # Dropdown'ı bul
        dropdown_element = self.driver.find_element(By.ID, dropdown_id)
        # Select objesi oluştur
        select = Select(dropdown_element)
        # Text'e göre seç
        select.select_by_visible_text(option_text)
        print(f"✓ Selected: {option_text}")
            
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
            
    def is_element_present(self, locator, timeout=10):
        """Check if element is present in DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
            
    def get_element_text(self, locator):
        """Get text from an element"""
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            self.take_screenshot(f"get_text_failed_{locator[1]}")
            raise
            
    def scroll_to_element(self, locator):
        """Scroll to a specific element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
    def wait_for_page_load(self, timeout=30):
        """Wait for page to load completely"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
        
    def switch_to_new_window(self):
        """Switch to newly opened window/tab"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        
    def take_screenshot(self, name="screenshot"):
        """Take screenshot and save with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
