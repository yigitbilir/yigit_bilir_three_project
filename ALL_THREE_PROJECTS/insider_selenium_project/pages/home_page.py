from selenium.webdriver.common.by import By
from insider_selenium_project.resources.base_page import BasePage


class HomePage(BasePage):
    """Page Object for Insider Home Page"""
    
    # Locators
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "nav#navigation")
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[text()='Careers']")
    HERO_SECTION = (By.CSS_SELECTOR, ".hero-section, #hero, section.hero, .main-hero")
    ACCEPT_COOKIES_BTN = (By.ID, "wt-cli-accept-all-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"
        
    def load(self):
        """Navigate to home page"""
        self.navigate_to(self.url)
        self.wait_for_page_load()
        self.accept_cookies_if_present()
        
    def accept_cookies_if_present(self):
        """Accept cookies popup if it appears"""
        try:
            if self.is_element_visible(self.ACCEPT_COOKIES_BTN, timeout=5):
                self.click_element(self.ACCEPT_COOKIES_BTN)
        except:
            pass  # Cookie popup didn't appear
            
    def is_home_page_loaded(self):
        """Verify home page is loaded by checking main elements"""
        try:
            logo_visible = self.is_element_visible(self.LOGO, timeout=10)
            nav_visible = self.is_element_visible(self.NAVIGATION_MENU, timeout=10)
            return logo_visible and nav_visible
        except Exception as e:
            self.take_screenshot("home_page_load_failed")
            raise AssertionError(f"Home page did not load properly: {str(e)}")
            
    def navigate_to_careers(self):
        """Navigate to Careers page through menu"""
        try:
            # Hover over Company menu
            self.click_element(self.COMPANY_MENU)
            # Click Careers link
            self.click_element(self.CAREERS_LINK)
            self.wait_for_page_load()
        except Exception as e:
            self.take_screenshot("navigate_to_careers_failed")
            raise
