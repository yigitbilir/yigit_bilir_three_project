from selenium.webdriver.common.by import By
from resources.base_page import BasePage
import time


class CareersPage(BasePage):
    """Page Object for Insider Careers Page"""
    
    # Locators
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    FILTER_LOCATION = (By.ID, "filter-by-location")
    FILTER_DEPARTMENT = (By.ID, "filter-by-department")
    LOCATION_OPTION_ISTANBUL = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    DEPARTMENT_OPTION_QA = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOB_LIST = (By.CSS_SELECTOR, ".position-list-item")
    POSITION_TITLE = (By.CSS_SELECTOR, ".position-title")
    POSITION_DEPARTMENT = (By.CSS_SELECTOR, ".position-department")
    POSITION_LOCATION = (By.CSS_SELECTOR, ".position-location")
    VIEW_ROLE_BTN = (By.CSS_SELECTOR, ".position-list-item-wrapper a")
    
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
            self.scroll_to_element(self.SEE_ALL_QA_JOBS_BTN)
            time.sleep(1)
            self.click_element(self.SEE_ALL_QA_JOBS_BTN)
            self.wait_for_page_load()
            time.sleep(3)  # Wait for jobs to load
        except Exception as e:
            self.take_screenshot("click_see_all_qa_jobs_failed")
            raise
            
    def filter_by_location(self, location="Istanbul, Turkey"):
        """Filter jobs by location"""
        try:
            # Click location dropdown
            self.click_element(self.LOCATION_OPTION_ISTANBUL)
            time.sleep(1)
            
            # Select location from dropdown
            location_option = (By.XPATH, f"//li[contains(text(),'{location}')]")
            self.click_element(location_option)
            time.sleep(2)  # Wait for filter to apply
        except Exception as e:
            self.take_screenshot("filter_by_location_failed")
            raise
            
    def filter_by_department(self, department="Quality Assurance"):
        """Filter jobs by department"""
        try:
            # Click department dropdown
            self.click_element(self.DEPARTMENT_OPTION_QA)
            time.sleep(1)
            
            # Select department from dropdown
            dept_option = (By.XPATH, f"//li[contains(text(),'{department}')]")
            self.click_element(dept_option)
            time.sleep(2)  # Wait for filter to apply
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
        jobs = self.get_job_list()
        
        if not jobs:
            self.take_screenshot("no_jobs_found")
            raise AssertionError("No jobs found in the list")
            
        print(f"\nFound {len(jobs)} jobs. Verifying each job...")
        
        for index, job in enumerate(jobs, 1):
            try:
                position = job.find_element(*self.POSITION_TITLE).text
                department = job.find_element(*self.POSITION_DEPARTMENT).text
                location = job.find_element(*self.POSITION_LOCATION).text
                
                print(f"\nJob {index}:")
                print(f"  Position: {position}")
                print(f"  Department: {department}")
                print(f"  Location: {location}")
                
                # Verify criteria
                assert "Quality Assurance" in position, f"Position '{position}' does not contain 'Quality Assurance'"
                assert "Quality Assurance" in department, f"Department '{department}' does not contain 'Quality Assurance'"
                assert "Istanbul, Turkey" in location, f"Location '{location}' does not contain 'Istanbul, Turkey'"
                
            except AssertionError as e:
                self.take_screenshot(f"job_verification_failed_{index}")
                raise
            except Exception as e:
                self.take_screenshot(f"job_element_error_{index}")
                raise
                
        return True
        
    def click_view_role_for_first_job(self):
        """Click 'View Role' button for the first job"""
        try:
            jobs = self.get_job_list()
            if jobs:
                view_role_btn = jobs[0].find_element(*self.VIEW_ROLE_BTN)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", view_role_btn)
                time.sleep(1)
                view_role_btn.click()
                time.sleep(3)  # Wait for new page to load
                self.switch_to_new_window()
            else:
                raise AssertionError("No jobs available to click")
        except Exception as e:
            self.take_screenshot("click_view_role_failed")
            raise
