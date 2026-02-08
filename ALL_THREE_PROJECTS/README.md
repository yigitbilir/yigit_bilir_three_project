# Test Automation Projects - Complete Suite

This repository contains three comprehensive test automation projects covering different aspects of software testing.

## 📋 Projects Overview

### 1. Selenium Web Automation - Insider Careers
**Directory:** `insider_selenium_project/`

Automated testing of the Insider careers website using Selenium WebDriver with Page Object Model (POM) design pattern.

**Technologies:**
- Python 3.10+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

**Features:**
- ✅ POM design pattern implementation
- ✅ Multi-browser support (Chrome/Firefox)
- ✅ Automatic screenshot on failure
- ✅ Comprehensive job filtering and validation
- ✅ Lever application form verification

**Quick Start:**
```bash
cd insider_selenium_project
pip install -r requirements.txt
pytest tests/test_insider_careers.py -v -s --browser=chrome
```

---

### 2. Load Testing - N11.com Search Module
**Directory:** `n11_load_test/`

Performance and load testing for the N11.com e-commerce search functionality using Locust.

**Technologies:**
- Python 3.10+
- Locust
- Requests

**Features:**
- ✅ 6 comprehensive test scenarios
- ✅ Positive and negative test cases
- ✅ Pagination testing
- ✅ Filter and sort testing
- ✅ Real-time monitoring dashboard
- ✅ HTML report generation

**Quick Start:**
```bash
cd n11_load_test
pip install -r requirements.txt
locust -f locustfile.py --host https://www.n11.com
# Then open http://localhost:8089
```

---

### 3. API Test Automation - PetStore CRUD
**Directory:** `petstore_api_tests/`

Complete API test automation for Swagger PetStore API with CRUD operations and extensive positive/negative scenarios.

**Technologies:**
- Python 3.10+
- Requests
- Pytest
- JSON Schema Validation

**Features:**
- ✅ Complete CRUD operation testing
- ✅ 18+ test scenarios (positive & negative)
- ✅ Response validation
- ✅ Data integrity checks
- ✅ Reusable API client
- ✅ Test data generators

**Quick Start:**
```bash
cd petstore_api_tests
pip install -r requirements.txt
pytest tests/test_pet_crud.py -v -s --html=report.html
```

---

## 🗂️ Repository Structure

```
.
├── insider_selenium_project/
│   ├── pages/                    # Page Object classes
│   ├── resources/                # Common methods (BasePage)
│   ├── tests/                    # Test cases
│   ├── screenshots/              # Auto-generated screenshots
│   ├── requirements.txt
│   └── README.md
│
├── n11_load_test/
│   ├── locustfile.py            # Locust load test scenarios
│   ├── TEST_SCENARIOS.md        # Detailed scenario documentation
│   ├── requirements.txt
│   └── README.md
│
├── petstore_api_tests/
│   ├── tests/                   # API test cases
│   ├── utils/                   # API client and helpers
│   ├── requirements.txt
│   └── README.md
│
└── README.md                    # This file
```

---

## 🚀 Prerequisites

All projects require:
- **Python 3.10 or higher**
- **pip** package manager

### Project-Specific Requirements:

**Project 1 (Selenium):**
- Chrome and/or Firefox browser
- WebDriver (auto-managed by webdriver-manager)

**Project 2 (Locust):**
- Internet connection to access n11.com

**Project 3 (API Tests):**
- Internet connection to access petstore.swagger.io

---

## 📦 Installation

### Install All Projects at Once

You can install dependencies for all three projects:

```bash
# Project 1 - Selenium
cd insider_selenium_project && pip install -r requirements.txt && cd ..

# Project 2 - Locust
cd n11_load_test && pip install -r requirements.txt && cd ..

# Project 3 - API Tests
cd petstore_api_tests && pip install -r requirements.txt && cd ..
```

### Or Install Individual Projects

Choose the project you want to work with and install its dependencies:

```bash
cd <project_directory>
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### Project 1: Selenium Web Automation

**Run with Chrome:**
```bash
cd insider_selenium_project
pytest tests/test_insider_careers.py -v -s --browser=chrome
```

**Run with Firefox:**
```bash
pytest tests/test_insider_careers.py -v -s --browser=firefox
```

**Generate HTML Report:**
```bash
pytest tests/test_insider_careers.py -v -s --browser=chrome --html=report.html
```

---

### Project 2: Load Testing

**Interactive Web UI (Recommended):**
```bash
cd n11_load_test
locust -f locustfile.py --host https://www.n11.com
# Open http://localhost:8089 in browser
```

**Headless Mode with Report:**
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --html=report.html --host https://www.n11.com
```

---

### Project 3: API Testing

**Run All Tests:**
```bash
cd petstore_api_tests
pytest tests/test_pet_crud.py -v -s
```

**Generate HTML Report:**
```bash
pytest tests/test_pet_crud.py -v -s --html=api_report.html --self-contained-html
```

**Run Specific Test:**
```bash
pytest tests/test_pet_crud.py::TestPetStoreCRUD::test_complete_crud_flow -v -s
```

---

## 📊 Test Coverage Summary

### Project 1: Selenium Automation
- ✅ Home page verification
- ✅ Navigation testing
- ✅ Job filtering (Location & Department)
- ✅ Data validation (Position, Department, Location)
- ✅ Redirect verification
- ✅ Multi-browser support

### Project 2: Load Testing
- ✅ Search functionality (5 scenarios)
- ✅ Pagination testing
- ✅ Filter and sort testing
- ✅ Edge cases (empty query, special characters)
- ✅ Performance metrics
- ✅ Response time tracking

### Project 3: API Testing
- ✅ CREATE operations (2 positive, 3 negative)
- ✅ READ operations (2 positive, 3 negative)
- ✅ UPDATE operations (2 positive, 2 negative)
- ✅ DELETE operations (1 positive, 2 negative)
- ✅ Complete CRUD integration test
- ✅ Data validation & schema verification

**Total Test Scenarios: 35+**

---

## 🎯 Requirements Compliance

### Project 1 Requirements: ✅
- [x] Python + Selenium
- [x] Page Object Model (POM)
- [x] Common methods in resource file
- [x] Visit Insider home page
- [x] Navigate to QA careers
- [x] Filter jobs (Location & Department)
- [x] Verify job listings
- [x] Click View Role
- [x] Verify Lever redirect
- [x] Screenshot on failure
- [x] Multi-browser support (parametric)

### Project 2 Requirements: ✅
- [x] Load test scenarios written
- [x] Tests for search module
- [x] Tests for result listing
- [x] Using Locust
- [x] 1 user configuration
- [x] Positive scenarios
- [x] Negative scenarios

### Project 3 Requirements: ✅
- [x] Uses Pet endpoints from petstore.swagger.io
- [x] CRUD operations implemented
- [x] Positive test scenarios
- [x] Negative test scenarios
- [x] Python + Requests
- [x] Comprehensive coverage

---

## 📖 Documentation

Each project has detailed documentation:

- **insider_selenium_project/README.md** - Selenium automation guide
- **n11_load_test/README.md** - Load testing guide
- **n11_load_test/TEST_SCENARIOS.md** - Detailed test scenarios
- **petstore_api_tests/README.md** - API testing guide

---

## 🛠️ Technologies Used

| Technology | Project 1 | Project 2 | Project 3 |
|------------|-----------|-----------|-----------|
| Python 3.10+ | ✅ | ✅ | ✅ |
| Selenium | ✅ | ❌ | ❌ |
| Pytest | ✅ | ❌ | ✅ |
| Locust | ❌ | ✅ | ❌ |
| Requests | ❌ | ✅ | ✅ |
| WebDriver Manager | ✅ | ❌ | ❌ |
| JSON Schema | ❌ | ❌ | ✅ |

---

## 🔍 Key Features Across All Projects

### Code Quality
- ✅ Clean, maintainable code
- ✅ Comprehensive documentation
- ✅ Descriptive naming conventions
- ✅ Proper error handling
- ✅ Detailed logging

### Testing Best Practices
- ✅ Separation of concerns
- ✅ Reusable components
- ✅ Positive & negative scenarios
- ✅ Data validation
- ✅ Comprehensive assertions

### Reporting
- ✅ HTML test reports
- ✅ Screenshots on failure (Project 1)
- ✅ Real-time monitoring (Project 2)
- ✅ Detailed console output
- ✅ Performance metrics (Project 2)

---

## 🐛 Troubleshooting

### Common Issues

**Python Version:**
```bash
python --version  # Should be 3.10+
```

**Dependency Issues:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

**Browser Driver Issues (Project 1):**
- The project uses webdriver-manager which auto-downloads drivers
- Ensure Chrome/Firefox is installed on your system

**Network Issues:**
- Check internet connection
- Verify target websites are accessible
- Check firewall settings

---

## 📝 Project-Specific Notes

### Project 1 Notes:
- Tests may take 2-5 minutes to complete
- Screenshots saved in `screenshots/` directory
- Browser sessions are cleaned up automatically
- Dynamic content may require wait time adjustments

### Project 2 Notes:
- Start with 1 user as per requirements
- Can scale up for actual load testing
- Web UI provides real-time graphs
- Test duration is configurable

### Project 3 Notes:
- Tests create and clean up test data
- Some API quirks are documented in tests
- Response times validated (< 3000ms)
- Complete CRUD lifecycle validated

---

## 🎓 Learning Resources

Each project demonstrates different testing concepts:

**Project 1 - Selenium:**
- Page Object Model (POM) pattern
- Web UI automation
- Cross-browser testing
- Dynamic content handling

**Project 2 - Load Testing:**
- Performance testing
- Load simulation
- Metrics collection
- Scenario-based testing

**Project 3 - API Testing:**
- RESTful API testing
- CRUD operations
- Data validation
- HTTP methods (GET, POST, PUT, DELETE)

---

## 🤝 Contributing

To extend or modify any project:

1. Follow the existing code structure
2. Maintain POM pattern (Project 1)
3. Add proper documentation
4. Include both positive and negative scenarios
5. Add cleanup code for test data

---

## 📄 License

These projects are for educational and testing purposes.

---

## ✅ Quick Verification

To verify all projects are set up correctly:

```bash
# Test Project 1
cd insider_selenium_project && python -c "import selenium; print('✓ Selenium OK')" && cd ..

# Test Project 2
cd n11_load_test && python -c "import locust; print('✓ Locust OK')" && cd ..

# Test Project 3
cd petstore_api_tests && python -c "import requests; print('✓ Requests OK')" && cd ..
```

---

## 📞 Support

For issues or questions:
1. Check individual project README files
2. Review test output and error messages
3. Ensure all prerequisites are met
4. Verify Python version and dependencies

---

**Happy Testing! 🚀**
