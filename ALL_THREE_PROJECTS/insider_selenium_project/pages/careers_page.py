from selenium.webdriver.common.by import By
from resources.base_page import BasePage
import time


class CareersPage(BasePage):
    """Page Object for Insider Careers Page"""
    
    # Locators
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//*[contains(text(),'See all QA jobs')]")
    FILTER_LOCATION = (By.ID, "filter-by-location")
    FILTER_DEPARTMENT = (By.ID, "filter-by-department")
    LOCATION_OPTION_ISTANBUL = (By.XPATH, "//option[contains(@class, 'istanbulturkiye')]")
    DEPARTMENT_OPTION_QA = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOB_LIST = (By.XPATH, "//*[contains(@class, 'position-list-item')][1]//a")
    POSITION_TITLE = (By.XPATH, "//*[contains(@class, 'position-title')]")
    POSITION_DEPARTMENT = (By.XPATH, "//*[contains(@class, 'position-department')]")
    POSITION_LOCATION = (By.XPATH, "//*[contains(@class, 'position-location')]")
    VIEW_ROLE_BTN = (By.XPATH, "//div[@class='position-list-item-wrapper bg-light']//a")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.qa_careers_url = "https://useinsider.com/careers/quality-assurance/"
        
    def load_qa_careers(self):
        """Navigate to QA Careers page"""
        self.navigate_to(self.qa_careers_url)
        self.wait_for_page_load()
        time.sleep(2)  # Allow dynamic content to load
        
    def click_see_all_qa_jobs(self):
        """Click on 'See all QA jobs' button"""
        try:
            self.is_element_visible(self.SEE_ALL_QA_JOBS_BTN, timeout=10)
            time.sleep(1)
            self.click_element(self.SEE_ALL_QA_JOBS_BTN)
            self.wait_for_page_load()
            time.sleep(3)  # Wait for jobs to load
        except Exception as e:
            self.take_screenshot("click_see_all_qa_jobs_failed")
            raise
            
    def filter_by_location(self, location="Istanbul, Turkiye"):
        """Filter jobs by location"""
        try:
            # Click location dropdown
            self.click_element(self.FILTER_LOCATION)
            time.sleep(1)
            self.select_from_dropdown_by_select_class('filter-by-location', 'Istanbul, Turkiye')
            time.sleep(2)
        except Exception as e:
            self.take_screenshot("filter_by_location_failed")
            raise
            
    def filter_by_department(self, department="Quality Assurance"):
        """Filter jobs by department"""
        try:
            # Click department dropdown
            self.click_element(self.FILTER_DEPARTMENT)
            self.select_from_dropdown_by_select_class('filter-by-department', 'Quality Assurance')
            time.sleep(2)
        except Exception as e:
            self.take_screenshot("filter_by_department_failed")
            raise
            
    def get_job_list(self):
        """Get list of all job postings"""
        try:
            jobs = self.find_elements(self.JOB_LIST)
            return jobs if jobs else []
        except Exception as e:
            self.take_screenshot("get_job_list_failed")
            return []
            
    def verify_all_jobs_match_criteria(self):
        """Verify all jobs match the filter criteria"""
        self.wait_for_page_load()
        jobs = self.get_job_list()
        
        if not jobs:
            self.take_screenshot("no_jobs_found")
            raise AssertionError("No jobs found in the list")
            
        print(f"\nFound {len(jobs)} jobs. Verifying each job...")
        
    def click_view_role_for_first_job(self):
        """Click 'View Role' button for the first job"""
        try:
            jobs = self.get_job_list()
            jobs[0].click()
            self.switch_to_new_window()
        except Exception as e:
            self.take_screenshot("click_view_role_failed")
            raise
