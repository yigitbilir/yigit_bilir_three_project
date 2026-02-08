from locust import HttpUser, task, between, events
import logging
import time


class N11SearchUser(HttpUser):
    """
    Load test user for n11.com search module
    
    This simulates user behavior for:
    1. Visiting the homepage
    2. Performing search operations
    3. Viewing search results
    4. Navigating through search result pages
    """
    
    # Wait time between tasks (simulating realistic user behavior)
    wait_time = between(1, 3)
    
    # Base URL for n11.com
    host = "https://www.n11.com"
    
    def on_start(self):
        """
        Called when a simulated user starts.
        Can be used for login or initial setup.
        """
        logging.info("User started - visiting homepage")
        self.client.get("/", name="Homepage")
        time.sleep(1)
    
    @task(5)  # Higher weight - performed more frequently
    def search_electronics(self):
        """
        Test Scenario 1: Search for electronics products
        Simulates a user searching for electronic items
        """
        search_queries = [
            "laptop",
            "telefon",
            "kulakl覺k",
            "tablet"
        ]
        
        for query in search_queries[:1]:  # Test with one query per task
            # Perform search
            with self.client.get(
                "/arama",
                params={"q": query},
                catch_response=True,
                name="Search - Electronics"
            ) as response:
                if response.status_code == 200:
                    if "arama" in response.url.lower():
                        response.success()
                        logging.info(f"Search successful for: {query}")
                    else:
                        response.failure(f"Unexpected redirect for query: {query}")
                else:
                    response.failure(f"Search failed with status: {response.status_code}")
    
    @task(3)
    def search_clothing(self):
        """
        Test Scenario 2: Search for clothing items
        Simulates a user searching for fashion/clothing products
        """
        search_queries = [
            "tişört",
            "pantolon",
            "ayakkab覺"
        ]
        
        for query in search_queries[:1]:
            with self.client.get(
                "/arama",
                params={"q": query},
                catch_response=True,
                name="Search - Clothing"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    logging.info(f"Search successful for: {query}")
                else:
                    response.failure(f"Search failed with status: {response.status_code}")
    
    @task(2)
    def search_with_filters(self):
        """
        Test Scenario 3: Search with additional filters
        Simulates advanced search with price/category filters
        """
        with self.client.get(
            "/arama",
            params={
                "q": "laptop",
                "srt": "PRICE_LOW"  # Sort by price low to high
            },
            catch_response=True,
            name="Search - With Filters"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info("Filtered search successful")
            else:
                response.failure(f"Filtered search failed: {response.status_code}")
    
    @task(4)
    def browse_search_results(self):
        """
        Test Scenario 4: Browse through search result pages
        Simulates pagination behavior
        """
        # Search first
        search_response = self.client.get(
            "/arama",
            params={"q": "elektronik"},
            name="Search - Before Pagination"
        )
        
        if search_response.status_code == 200:
            # Navigate to page 2
            with self.client.get(
                "/arama",
                params={"q": "elektronik", "pg": "2"},
                catch_response=True,
                name="Search - Page 2"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    logging.info("Pagination successful")
                else:
                    response.failure(f"Pagination failed: {response.status_code}")
    
    @task(1)
    def search_empty_query(self):
        """
        Test Scenario 5: Negative test - Empty search
        Tests system behavior with invalid input
        """
        with self.client.get(
            "/arama",
            params={"q": ""},
            catch_response=True,
            name="Search - Empty Query"
        ) as response:
            # Empty search should handle gracefully
            if response.status_code in [200, 400, 404]:
                response.success()
                logging.info("Empty search handled correctly")
            else:
                response.failure(f"Unexpected response for empty search: {response.status_code}")
    
    @task(1)
    def search_special_characters(self):
        """
        Test Scenario 6: Negative test - Special characters
        Tests system robustness with special characters
        """
        special_queries = ["@#$%", "test<>", "' OR '1'='1"]
        
        for query in special_queries[:1]:
            with self.client.get(
                "/arama",
                params={"q": query},
                catch_response=True,
                name="Search - Special Characters"
            ) as response:
                # Should handle special characters without errors
                if response.status_code in [200, 400]:
                    response.success()
                    logging.info(f"Special character search handled: {query}")
                else:
                    response.failure(f"Special char search failed: {response.status_code}")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """
    Called when test starts
    """
    logging.info("="*50)
    logging.info("N11.com Search Module Load Test Started")
    logging.info("="*50)


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """
    Called when test stops
    """
    logging.info("="*50)
    logging.info("N11.com Search Module Load Test Completed")
    logging.info("="*50)


# Configuration for running standalone
if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=https://www.n11.com")
