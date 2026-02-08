import pytest
import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from insider_selenium_project.pages.home_page import HomePage
from insider_selenium_project.pages.careers_page import CareersPage
from insider_selenium_project.pages.lever_application_page import LeverApplicationPage


class TestInsiderCareers:
    """Test suite for Insider Careers automation"""
    
    def test_insider_careers_flow(self, driver):
        """
        Complete test flow for Insider Careers:
        1. Visit Insider home page and verify it loads
        2. Navigate to QA careers and filter jobs
        3. Verify all jobs match criteria
        4. Click View Role and verify Lever redirect
        """
        
        # Step 1: Visit home page and verify it's loaded
        print("\n=== Step 1: Visiting Insider Home Page ===")
        home_page = HomePage(driver)
        home_page.load()
        assert home_page.is_home_page_loaded(), "Home page did not load properly"
        print("✓ Home page loaded successfully")
        
        # Step 2: Navigate to QA Careers page
        print("\n=== Step 2: Navigating to QA Careers ===")
        careers_page = CareersPage(driver)
        careers_page.load_qa_careers()
        print("✓ QA Careers page loaded")
        
        # Step 3: Click "See all QA jobs"
        print("\n=== Step 3: Clicking 'See all QA jobs' ===")
        careers_page.click_see_all_qa_jobs()
        print("✓ Clicked 'See all QA jobs'")
        
        # Step 4: Filter by Location - Istanbul, Turkey
        print("\n=== Step 4: Filtering by Location - Istanbul, Turkey ===")
        careers_page.filter_by_location("Istanbul, Turkey")
        print("✓ Filtered by location")
        
        # Step 5: Filter by Department - Quality Assurance
        print("\n=== Step 5: Filtering by Department - Quality Assurance ===")
        careers_page.filter_by_department("Quality Assurance")
        print("✓ Filtered by department")
        
        # Step 6: Verify jobs list is present
        print("\n=== Step 6: Verifying Jobs List ===")
        jobs = careers_page.get_job_list()
        assert len(jobs) > 0, "No jobs found after filtering"
        print(f"✓ Found {len(jobs)} jobs")
        
        # Step 7: Verify all jobs match criteria
        print("\n=== Step 7: Verifying All Jobs Match Criteria ===")
        careers_page.verify_all_jobs_match_criteria()
        print("✓ All jobs verified successfully")
        
        # Step 8: Click "View Role" and verify Lever redirect
        print("\n=== Step 8: Clicking 'View Role' ===")
        careers_page.click_view_role_for_first_job()
        print("✓ Clicked 'View Role'")
        
        # Step 9: Verify redirect to Lever Application page
        print("\n=== Step 9: Verifying Lever Application Page ===")
        lever_page = LeverApplicationPage(driver)
        assert lever_page.is_lever_application_page(), "Not redirected to Lever application page"
        print("✓ Successfully redirected to Lever application page")
        
        print("\n" + "="*50)
        print("ALL TESTS PASSED SUCCESSFULLY!")
        print("="*50)


if __name__ == "__main__":
    # Run tests with Chrome by default
    pytest.main([__file__, "-v", "-s", "--browser=chrome"])
