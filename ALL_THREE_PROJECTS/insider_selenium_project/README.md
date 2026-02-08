# Insider Selenium Automation Project

This project automates testing of the Insider careers page using Python, Selenium, and the Page Object Model (POM) design pattern.

## Project Structure

```
insider_selenium_project/
│
├── pages/                          # Page Object classes
│   ├── home_page.py               # Home page object
│   ├── careers_page.py            # Careers page object
│   └── lever_application_page.py  # Lever application page object
│
├── resources/                      # Common resources and utilities
│   └── base_page.py               # Base page with common methods
│
├── tests/                         # Test files
│   ├── conftest.py               # Pytest configuration and fixtures
│   └── test_insider_careers.py   # Main test cases
│
├── screenshots/                   # Auto-generated screenshots on failure
├── simple_run.py                 # Easiest way to run tests
├── run_tests.py                  # Run with browser selection
├── conftest.py                   # Pytest config (project root)
└── requirements.txt              # Python dependencies
```

## Features

✅ Page Object Model (POM) implementation
✅ Common methods in BasePage resource file
✅ Parameterized browser support (Chrome/Firefox)
✅ Automatic screenshot on test failure
✅ Explicit waits for stable test execution
✅ Comprehensive logging and reporting

## Prerequisites

- Python 3.10 or higher
- Chrome and/or Firefox browser installed
- pip (Python package manager)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### ⚠️ IMPORTANT: Run from project root directory
```bash
cd insider_selenium_project
```

### Method 1: Simple Runner (Easiest - Recommended!)
```bash
python simple_run.py
```

### Method 2: Using run_tests.py
```bash
# Run with Chrome (default)
python run_tests.py

# Run with Firefox
python run_tests.py firefox
```

### Method 3: Using pytest directly
```bash
# Make sure you're in the project root directory first!
cd insider_selenium_project

# Run with Chrome
python -m pytest tests/test_insider_careers.py -v -s --browser=chrome

# Run with Firefox
python -m pytest tests/test_insider_careers.py -v -s --browser=firefox

# Run with HTML report
python -m pytest tests/test_insider_careers.py -v -s --browser=chrome --html=report.html --self-contained-html
```

### Troubleshooting: If you get "unrecognized arguments: --browser" error

Make sure:
1. You're in the project root directory: `cd insider_selenium_project`
2. conftest.py exists in both root and tests/ folder
3. Run: `python simple_run.py` (simplest method)

## Test Scenarios

The automation covers the following test steps:

1. **Visit Insider home page** - Verify the page loads with all main blocks
2. **Navigate to QA Careers** - Go to https://useinsider.com/careers/quality-assurance/
3. **Click "See all QA jobs"** - Open the jobs listing page
4. **Filter jobs** - Filter by Location (Istanbul, Turkey) and Department (Quality Assurance)
5. **Verify jobs list** - Check that jobs are displayed
6. **Verify job criteria** - Ensure all jobs contain:
   - Position: "Quality Assurance"
   - Department: "Quality Assurance"
   - Location: "Istanbul, Turkey"
7. **Click "View Role"** - Click the button for the first job
8. **Verify Lever redirect** - Confirm redirection to Lever Application form page

## Page Object Model (POM) Structure

### BasePage (resources/base_page.py)
Contains common methods used across all pages:
- `navigate_to()` - Navigate to URL
- `find_element()` - Find element with explicit wait
- `find_elements()` - Find multiple elements
- `click_element()` - Click with wait for clickability
- `is_element_visible()` - Check element visibility
- `scroll_to_element()` - Scroll to element
- `take_screenshot()` - Capture screenshot
- `wait_for_page_load()` - Wait for page to load
- `switch_to_new_window()` - Switch to new tab/window

### Page Objects
- **HomePage** - Handles home page interactions
- **CareersPage** - Handles careers page and job filtering
- **LeverApplicationPage** - Handles Lever application page verification

## Screenshot on Failure

The framework automatically captures screenshots when:
- A test step fails
- An element is not found
- An assertion fails

Screenshots are saved in the `screenshots/` directory with timestamps.

## Browser Configuration

The browser type is parameterized through pytest command line:
```bash
--browser=chrome   # Run with Chrome
--browser=firefox  # Run with Firefox
```

Browser settings are configured in `tests/conftest.py`.

## Dependencies

- **selenium** - Web automation framework
- **pytest** - Testing framework
- **webdriver-manager** - Automatic driver management
- **pytest-html** - HTML test reports
- **Pillow** - Image processing for screenshots

## Troubleshooting

1. **Browser driver issues**: The project uses webdriver-manager which automatically downloads and manages browser drivers.

2. **Element not found errors**: The framework uses explicit waits. If elements are not found, screenshots will be captured automatically.

3. **Dynamic content loading**: Some pages have dynamic content. The framework includes appropriate waits and sleeps where necessary.

## Notes

- The project strictly follows POM design pattern
- No BDD frameworks are used (as per requirements)
- Tests work on both Chrome and Firefox browsers
- All common methods are in the BasePage resource file
- Screenshots are automatically taken on failure
