#!/usr/bin/env python3
"""
Simple test runner - No arguments needed
Just run: python simple_run.py
"""

import subprocess
import sys
import os

# Ensure we're in the right directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("\n" + "="*70)
print("INSIDER SELENIUM TEST - SIMPLE RUNNER")
print("="*70)
print(f"Working Directory: {os.getcwd()}")
print("Browser: Chrome (default)")
print("="*70 + "\n")

# Run with Chrome by default
# Using unittest discovery instead of pytest to avoid conflicts
cmd = [
    sys.executable,
    "-m", 
    "pytest",
    "tests/test_insider_careers.py",
    "-v",
    "-s",
    "--browser=chrome",
    "--tb=short",
    "-p", "no:cacheprovider"  # Disable cache to avoid issues
]

print(f"Running: {' '.join(cmd)}\n")

try:
    result = subprocess.run(cmd)
    
    print("\n" + "="*70)
    if result.returncode == 0:
        print("✅ TESTS PASSED!")
    else:
        print("❌ TESTS FAILED - Check output above")
    print("="*70 + "\n")
    
    sys.exit(result.returncode)
    
except Exception as e:
    print(f"\n❌ Error running tests: {e}")
    print("\nTry running manually:")
    print("  cd insider_selenium_project")
    print("  python -m pytest tests/test_insider_careers.py -v -s --browser=chrome")
    sys.exit(1)
