from selenium.webdriver.common.by import By
from resources.base_page import BasePage


class LeverApplicationPage(BasePage):
    """Page Object for Lever Application Form Page"""
    
    # Locators
    LEVER_APPLICATION_FORM = (By.CSS_SELECTOR, ".application-form, .lever-jobs-container")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".postings-btn")
    JOB_TITLE = (By.CSS_SELECTOR, ".posting-headline h2")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def is_lever_application_page(self):
        """Verify we are on Lever application page"""
        try:
            current_url = self.get_current_url()
            print(f"\nCurrent URL: {current_url}")
            
            # Check if URL contains 'lever' or 'jobs.lever.co'
            is_lever_url = "lever" in current_url.lower()
            
            if not is_lever_url:
                self.take_screenshot("not_on_lever_page")
                raise AssertionError(f"Not redirected to Lever page. Current URL: {current_url}")
                
            return True
            
        except Exception as e:
            self.take_screenshot("lever_page_verification_failed")
            raise
