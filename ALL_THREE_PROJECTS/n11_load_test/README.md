# N11.com Search Module - Load Testing with Locust

## Overview
This project contains load tests for the n11.com search module and result listing functionality using Locust, a modern Python-based load testing framework.

## Project Structure
```
n11_load_test/
│
├── locustfile.py          # Main Locust test file
├── TEST_SCENARIOS.md      # Detailed test scenarios documentation
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Test Scenarios

The load test includes 6 scenarios covering both positive and negative test cases:

1. **Search for Electronics** (Weight: 5) - Most common user behavior
2. **Search for Clothing** (Weight: 3) - Category-specific searches
3. **Search with Filters** (Weight: 2) - Advanced filtering and sorting
4. **Browse Search Results** (Weight: 4) - Pagination testing
5. **Empty Search Query** (Weight: 1) - Negative test for robustness
6. **Special Characters** (Weight: 1) - Security and input validation test

See `TEST_SCENARIOS.md` for detailed documentation.

## Running the Tests

### Method 1: Web UI (Recommended for Interactive Testing)
```bash
locust -f locustfile.py --host https://www.n11.com
```
Then open http://localhost:8089 in your browser to:
- Set number of users (start with 1 as per requirements)
- Set spawn rate
- Monitor real-time statistics
- View charts and graphs

### Method 2: Headless Mode (Automated Testing)
Run for 5 minutes with 1 user:
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --host https://www.n11.com
```

### Method 3: Generate HTML Report
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --html=n11_load_test_report.html --host https://www.n11.com
```

### Method 4: CSV Export
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --csv=n11_results --host https://www.n11.com
```

## Test Configuration

### Current Configuration (as per requirements)
- **Users:** 1 concurrent user
- **Spawn Rate:** 1 user/second
- **Host:** https://www.n11.com

### Customizing Test Parameters
You can modify:
- `--users X` - Number of concurrent users
- `--spawn-rate X` - Users spawned per second
- `--run-time Xm` - Test duration (e.g., 5m, 10m, 1h)

## Understanding the Results

### Key Metrics Displayed

1. **Type** - Request name/endpoint
2. **# Requests** - Total number of requests made
3. **# Fails** - Number of failed requests
4. **Median** - Median response time (ms)
5. **95%ile** - 95th percentile response time
6. **Average** - Average response time
7. **Min/Max** - Minimum and maximum response times
8. **RPS** - Requests per second
9. **Failures/s** - Failures per second

### Performance Benchmarks

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Response Time | < 1000ms | 1000-2000ms | > 2000ms |
| Success Rate | > 99% | 95-99% | < 95% |
| Error Rate | < 0.1% | 0.1-1% | > 1% |

## Test Scenarios Breakdown

### Positive Test Scenarios
✅ Basic search functionality
✅ Category-specific searches
✅ Filtered search with sorting
✅ Pagination through results

### Negative Test Scenarios
✅ Empty search query handling
✅ Special characters and injection attempts
✅ Invalid input validation

## Sample Output

When running the test, you'll see output like:
```
[2024-01-15 10:30:00] Starting Locust...
[2024-01-15 10:30:01] User started - visiting homepage
[2024-01-15 10:30:02] Search successful for: laptop
[2024-01-15 10:30:03] Filtered search successful
[2024-01-15 10:30:04] Pagination successful

Statistics:
Type            Name                # reqs   # fails  Median  Average  Min  Max
-----------------------------------------------------------------------------
GET             Homepage                10       0     234     245     201  312
GET             Search - Electronics    50       0     456     478     398  654
GET             Search - Clothing       30       0     423     441     387  589
GET             Search - With Filters   20       0     567     591     512  723
GET             Search - Page 2         40       0     445     462     401  598
```

## Extending the Tests

### Adding New Scenarios
To add new test scenarios, create new methods with `@task(weight)` decorator:

```python
@task(3)
def my_new_scenario(self):
    """Your test scenario description"""
    with self.client.get("/endpoint", catch_response=True) as response:
        if response.status_code == 200:
            response.success()
        else:
            response.failure("Error message")
```

### Adjusting Task Weights
Modify the weight parameter to change frequency:
- Higher weight = executed more frequently
- Lower weight = executed less frequently

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Check internet connection
   - Verify n11.com is accessible
   - Check firewall settings

2. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

3. **SSL Errors**
   - May need to disable SSL verification for some environments (not recommended for production)

## Best Practices

1. **Start Small:** Begin with 1 user to establish baseline
2. **Gradual Increase:** Increase load gradually to find breaking points
3. **Monitor Continuously:** Watch for performance degradation over time
4. **Document Findings:** Record results for comparison
5. **Test Regularly:** Run tests periodically to catch regressions

## Requirements Compliance

✅ Load test scenarios written and documented
✅ Tests investigate search module behavior
✅ Tests cover result listing after search
✅ Using Locust framework (Python-based)
✅ Configured for 1 user as specified
✅ Includes both positive and negative scenarios

## Additional Resources

- [Locust Documentation](https://docs.locust.io/)
- [Best Practices for Load Testing](https://docs.locust.io/en/stable/writing-a-locustfile.html)
- TEST_SCENARIOS.md - Detailed scenario documentation

## Notes

- This test simulates realistic user behavior with wait times between requests
- Task weights reflect typical user patterns (more electronics searches than special character tests)
- All scenarios include error handling and logging
- Tests can be easily extended or modified for different requirements
