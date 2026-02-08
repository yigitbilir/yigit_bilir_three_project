# Troubleshooting Guide - Insider Selenium Tests

## Common Errors and Solutions

### Error 1: "TypeError: test_insider_careers_flow() missing 2 required positional arguments"

**Cause:** Pytest cannot find or use the driver fixture properly.

**Solutions:**

1. **Make sure you're in the project directory:**
```bash
cd insider_selenium_project
```

2. **Run using one of these commands:**
```bash
# Method 1 - Using run script
python run_tests.py

# Method 2 - Using pytest from project root
pytest tests/test_insider_careers.py -v -s --browser=chrome

# Method 3 - Simple pytest
pytest -v -s --browser=chrome
```

3. **Check that all __init__.py files exist:**
```bash
ls tests/__init__.py
ls pages/__init__.py
ls resources/__init__.py
```

---

### Error 2: "ModuleNotFoundError: No module named 'selenium'"

**Solution:**
```bash
pip install -r requirements.txt
```

---

### Error 3: "ModuleNotFoundError: No module named 'pages'"

**Cause:** Import path issue or missing __init__.py files.

**Solution:**
1. Make sure you're running from the project root:
```bash
pwd  # Should show: .../insider_selenium_project
```

2. Check __init__.py files exist:
```bash
ls tests/__init__.py pages/__init__.py resources/__init__.py
```

3. If missing, create them:
```bash
touch tests/__init__.py pages/__init__.py resources/__init__.py
```

---

### Error 4: Browser driver not found

**Solution:**
The project uses `webdriver-manager` which automatically downloads drivers.
Just make sure Chrome or Firefox is installed:

```bash
# Check Chrome
google-chrome --version
# or
chromium --version

# Check Firefox
firefox --version
```

---

### Error 5: "Session not created: This version of ChromeDriver only supports Chrome version X"

**Solution:**
```bash
# Update webdriver-manager cache
pip install --upgrade webdriver-manager

# Or clear cache and reinstall
pip uninstall webdriver-manager
pip install webdriver-manager
```

---

### Error 6: Tests run but fail to find elements

**Possible causes:**
1. Website structure changed
2. Slow internet connection
3. Elements take longer to load

**Solutions:**

1. **Increase wait times in base_page.py:**
```python
# Change line 13 in resources/base_page.py
self.wait = WebDriverWait(driver, 20)  # Increase from 15 to 20
```

2. **Run with slower connection in mind:**
- Website may have changed - this is expected with live sites
- Check if https://useinsider.com/ is accessible

---

### Error 7: "ImportError: cannot import name 'HomePage'"

**Solution:**
```bash
# Make sure all __init__.py files exist
find . -name "__init__.py"

# Should output:
# ./tests/__init__.py
# ./pages/__init__.py
# ./resources/__init__.py
```

If not, create them:
```bash
touch tests/__init__.py pages/__init__.py resources/__init__.py
```

---

### Error 8: Tests pass but no screenshots on failure

**Expected behavior:**
Screenshots are only taken when tests FAIL, not when they pass.

To test screenshot functionality:
1. Temporarily break a test
2. Run it and check the `screenshots/` folder

---

## Running Tests Successfully - Checklist

✅ **Step 1:** Navigate to project directory
```bash
cd insider_selenium_project
```

✅ **Step 2:** Verify Python version
```bash
python --version  # Should be 3.10+
```

✅ **Step 3:** Install dependencies
```bash
pip install -r requirements.txt
```

✅ **Step 4:** Verify Chrome/Firefox installed
```bash
google-chrome --version  # or firefox --version
```

✅ **Step 5:** Run tests
```bash
python run_tests.py
# or
pytest tests/test_insider_careers.py -v -s --browser=chrome
```

---

## Directory Structure Check

Your project should look like this:

```
insider_selenium_project/
├── pages/
│   ├── __init__.py              ← Must exist
│   ├── home_page.py
│   ├── careers_page.py
│   └── lever_application_page.py
├── resources/
│   ├── __init__.py              ← Must exist
│   └── base_page.py
├── tests/
│   ├── __init__.py              ← Must exist
│   ├── conftest.py
│   └── test_insider_careers.py
├── screenshots/                 ← Auto-created
├── requirements.txt
├── pytest.ini
├── run_tests.py
└── README.md
```

---

## Still Having Issues?

### Check pytest discovery:
```bash
pytest --collect-only
```

This should show:
```
<Module tests/test_insider_careers.py>
  <Class TestInsiderCareers>
    <Function test_insider_careers_flow>
```

### Verbose debug mode:
```bash
pytest tests/test_insider_careers.py -v -s --browser=chrome --tb=long
```

### Check imports manually:
```bash
python -c "from pages.home_page import HomePage; print('✓ Imports OK')"
```

---

## Environment Variables (Optional)

You can set default browser:
```bash
# Linux/Mac
export BROWSER=firefox

# Windows
set BROWSER=firefox
```

Then run:
```bash
pytest -v -s
```

---

## Clean Start

If nothing works, try a clean reinstall:

```bash
# 1. Remove virtual environment (if using one)
rm -rf venv/

# 2. Create new virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 3. Install dependencies fresh
pip install -r requirements.txt

# 4. Create __init__.py files
touch tests/__init__.py pages/__init__.py resources/__init__.py

# 5. Run tests
python run_tests.py
```

---

## Quick Fix Commands

```bash
# Fix: Missing __init__.py files
touch tests/__init__.py pages/__init__.py resources/__init__.py

# Fix: Wrong directory
cd insider_selenium_project

# Fix: Missing dependencies
pip install -r requirements.txt

# Fix: Outdated webdriver
pip install --upgrade webdriver-manager

# Run: Simplest command that should work
python run_tests.py
```

---

## Getting Help

When reporting issues, include:
1. Python version: `python --version`
2. Operating system: `uname -a` or Windows version
3. Full error message
4. Command you ran
5. Output of: `pip list | grep selenium`

---

**Most Common Solution:**

```bash
cd insider_selenium_project
touch tests/__init__.py pages/__init__.py resources/__init__.py
python run_tests.py
```

This fixes 90% of import-related issues!
