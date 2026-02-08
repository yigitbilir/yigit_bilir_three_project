# N11.com Search Module - Load Test Scenarios

## Overview
This document outlines the load test scenarios for the n11.com search module and result listing functionality.

## Test Scenarios

### 1. Search for Electronics (Weight: 5/16 - Highest Priority)
**Purpose:** Test the most common user behavior - searching for electronic products

**Steps:**
1. User navigates to n11.com homepage
2. User enters search query (laptop, telefon, kulakl覺k, tablet)
3. System displays search results
4. Measure response time and success rate

**Expected Behavior:**
- HTTP 200 response
- Search results page loads
- Results relevant to query

**Performance Metrics:**
- Response time < 2 seconds (acceptable)
- Response time < 1 second (good)
- Success rate > 95%

---

### 2. Search for Clothing (Weight: 3/16)
**Purpose:** Test search functionality for fashion/clothing category

**Steps:**
1. User searches for clothing items (tişört, pantolon, ayakkab覺)
2. System returns filtered results
3. Verify response time and accuracy

**Expected Behavior:**
- Successful search results
- Category-specific filtering works
- Fast response time

**Performance Metrics:**
- Response time < 2 seconds
- Success rate > 95%

---

### 3. Search with Filters (Weight: 2/16)
**Purpose:** Test advanced search with sorting and filtering options

**Steps:**
1. User performs search with query
2. User applies price sorting (low to high)
3. System re-renders results with applied filters
4. Measure performance impact of filtering

**Expected Behavior:**
- Filters apply correctly
- Results are sorted as requested
- No significant performance degradation

**Performance Metrics:**
- Response time < 3 seconds (with filter processing)
- Success rate > 90%

---

### 4. Browse Search Results - Pagination (Weight: 4/16)
**Purpose:** Test pagination functionality and multi-page browsing

**Steps:**
1. User performs initial search
2. User navigates to page 2, 3, etc.
3. System loads subsequent pages
4. Verify consistent performance across pages

**Expected Behavior:**
- Smooth pagination
- Consistent load times across pages
- No data loss between pages

**Performance Metrics:**
- Response time < 2 seconds per page
- Success rate > 95%
- No broken pagination links

---

### 5. Empty Search Query (Weight: 1/16 - Negative Test)
**Purpose:** Test system robustness with invalid input

**Steps:**
1. User submits empty search query
2. System handles gracefully
3. Displays appropriate error or default page

**Expected Behavior:**
- No system crash
- Graceful error handling
- HTTP 200/400/404 (acceptable responses)
- Appropriate user feedback

**Performance Metrics:**
- Fast error response < 1 second
- No 500 server errors

---

### 6. Special Characters in Search (Weight: 1/16 - Negative Test)
**Purpose:** Test system security and robustness against special characters and potential injection attempts

**Steps:**
1. User enters special characters (@#$%, <>, SQL injection patterns)
2. System sanitizes input
3. Returns safe response

**Expected Behavior:**
- Input sanitization works
- No SQL injection vulnerabilities
- No XSS vulnerabilities
- Graceful handling

**Performance Metrics:**
- Response time < 2 seconds
- No security errors
- HTTP 200 or 400

---

## Load Test Configuration

### User Simulation
- **Number of Users:** 1 (as per requirements)
- **Spawn Rate:** 1 user
- **Run Time:** Configurable (recommended 5-10 minutes for baseline)

### Task Weights Explanation
Tasks are weighted based on real user behavior patterns:
- **5:** Most common searches (electronics) - 31.25%
- **4:** Pagination browsing - 25%
- **3:** Clothing searches - 18.75%
- **2:** Filtered searches - 12.5%
- **1:** Edge cases (empty, special chars) - 6.25% each

### Performance Thresholds

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Response Time | < 1s | 1-2s | > 2s |
| Success Rate | > 99% | 95-99% | < 95% |
| Error Rate | < 0.1% | 0.1-1% | > 1% |

### Key Performance Indicators (KPIs)

1. **Average Response Time:** Overall average for all requests
2. **95th Percentile Response Time:** Response time for 95% of requests
3. **Requests Per Second (RPS):** Throughput capability
4. **Failure Rate:** Percentage of failed requests
5. **Response Time Distribution:** Min, median, max, std deviation

---

## Running the Tests

### Command Line (Headless Mode)
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --host https://www.n11.com
```

### Web UI Mode
```bash
locust -f locustfile.py --host https://www.n11.com
```
Then open http://localhost:8089 in browser

### With HTML Report
```bash
locust -f locustfile.py --headless --users 1 --spawn-rate 1 --run-time 5m --html=report.html --host https://www.n11.com
```

---

## Expected Outcomes

### Positive Scenarios
- All search queries return results successfully
- Pagination works smoothly
- Filters apply correctly
- Performance metrics within acceptable ranges

### Negative Scenarios
- Empty searches handled gracefully
- Special characters don't break the system
- No security vulnerabilities exploited
- Appropriate error messages displayed

---

## Monitoring and Analysis

### Metrics to Monitor
1. Response time trends over duration
2. Error rate patterns
3. Throughput consistency
4. Resource utilization (if accessible)

### Red Flags to Watch For
- Increasing response times over time (memory leak indicator)
- High error rates
- Timeouts
- Inconsistent performance across similar requests

---

## Recommendations

1. **Baseline Testing:** Run with 1 user first to establish baseline
2. **Gradual Load Increase:** If expanding, increase users gradually
3. **Peak Time Simulation:** Consider time-of-day factors
4. **Geographic Distribution:** Test from different regions if applicable
5. **Cache Behavior:** Monitor cache hit/miss rates if accessible

---

## Test Deliverables

1. **Locust HTML Report:** Performance metrics and graphs
2. **Test Scenarios Document:** This document
3. **Screenshots/Charts:** Response time distribution, RPS over time
4. **Analysis Summary:** Key findings and recommendations
