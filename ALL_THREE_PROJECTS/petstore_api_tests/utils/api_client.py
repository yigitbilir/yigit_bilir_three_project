import requests
import json
from typing import Dict, Any, Optional


class PetStoreAPIClient:
    """API Client for PetStore Swagger API"""
    
    BASE_URL = "https://petstore.swagger.io/v2"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    # ==================== PET ENDPOINTS ====================
    
    def create_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        """
        Create a new pet (POST /pet)
        
        Args:
            pet_data: Dictionary containing pet information
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=pet_data)
        return response
    
    def get_pet(self, pet_id: int) -> requests.Response:
        """
        Get pet by ID (GET /pet/{petId})
        
        Args:
            pet_id: Pet ID
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.get(url)
        return response
    
    def update_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        """
        Update an existing pet (PUT /pet)
        
        Args:
            pet_data: Dictionary containing updated pet information
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=pet_data)
        return response
    
    def delete_pet(self, pet_id: int, api_key: Optional[str] = None) -> requests.Response:
        """
        Delete a pet (DELETE /pet/{petId})
        
        Args:
            pet_id: Pet ID to delete
            api_key: Optional API key
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        headers = {}
        if api_key:
            headers['api_key'] = api_key
        response = self.session.delete(url, headers=headers)
        return response
    
    def find_pets_by_status(self, status: str) -> requests.Response:
        """
        Find pets by status (GET /pet/findByStatus)
        
        Args:
            status: Status value (available, pending, sold)
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet/findByStatus"
        response = self.session.get(url, params={'status': status})
        return response
    
    def update_pet_with_form(self, pet_id: int, name: str = None, status: str = None) -> requests.Response:
        """
        Update pet with form data (POST /pet/{petId})
        
        Args:
            pet_id: Pet ID to update
            name: Updated name
            status: Updated status
            
        Returns:
            Response object
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        data = {}
        if name:
            data['name'] = name
        if status:
            data['status'] = status
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = self.session.post(url, data=data, headers=headers)
        return response


class APITestHelper:
    """Helper methods for API testing"""
    
    @staticmethod
    def validate_status_code(response: requests.Response, expected_code: int) -> bool:
        """Validate response status code"""
        return response.status_code == expected_code
    
    @staticmethod
    def validate_response_time(response: requests.Response, max_time_ms: int = 3000) -> bool:
        """Validate response time is within acceptable range"""
        return response.elapsed.total_seconds() * 1000 <= max_time_ms
    
    @staticmethod
    def validate_json_response(response: requests.Response) -> bool:
        """Validate response contains valid JSON"""
        try:
            response.json()
            return True
        except json.JSONDecodeError:
            return False
    
    @staticmethod
    def print_response(response: requests.Response, title: str = "Response"):
        """Pretty print response for debugging"""
        print(f"\n{'='*60}")
        print(f"{title}")
        print(f"{'='*60}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response.elapsed.total_seconds() * 1000:.2f}ms")
        print(f"Headers: {dict(response.headers)}")
        try:
            print(f"Body: {json.dumps(response.json(), indent=2)}")
        except:
            print(f"Body: {response.text}")
        print(f"{'='*60}\n")
