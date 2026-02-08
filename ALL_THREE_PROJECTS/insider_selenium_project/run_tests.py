#!/usr/bin/env python3
"""
Run script for Insider Selenium Tests
Usage:
    python run_tests.py              # Run with Chrome (default)
    python run_tests.py chrome       # Run with Chrome
    python run_tests.py firefox      # Run with Firefox
"""

import sys
import os
import subprocess

def main():
    # Parse arguments
    browser = "chrome"
    
    # Check if browser argument provided
    if len(sys.argv) > 1 and sys.argv[1] in ['chrome', 'firefox']:
        browser = sys.argv[1]
    
    # Build pytest command - run from project root
    cmd = [
        sys.executable,  # Use current Python interpreter
        "-m", "pytest",
        "tests/test_insider_careers.py",
        "-v",
        "-s",
        f"--browser={browser}"
    ]
    
    print("="*70)
    print(f"Running Insider Selenium Tests with {browser.upper()}")
    print("="*70)
    print(f"Command: {' '.join(cmd)}")
    print(f"Working directory: {os.getcwd()}")
    print("="*70)
    print()
    
    # Run tests
    result = subprocess.run(cmd)
    
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
