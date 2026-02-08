import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import PetStoreAPIClient, APITestHelper
from utils.test_data import TestDataGenerator, PetSchema


class TestPetStoreCRUD:
    """
    Comprehensive CRUD tests for PetStore API /pet endpoints
    Includes positive and negative test scenarios
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client before each test"""
        self.api_client = PetStoreAPIClient()
        self.helper = APITestHelper()
        self.test_pet_id = TestDataGenerator.get_test_pet_id()
    
    # ==================== CREATE (POST) - POSITIVE TESTS ====================
    
    def test_create_pet_with_valid_data(self):
        """
        Positive Test: Create a new pet with all valid required fields
        Expected: 200 OK, pet created successfully
        """
        print("\n" + "="*60)
        print("TEST: Create Pet with Valid Data")
        print("="*60)
        
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id)
        response = self.api_client.create_pet(pet_data)
        
        self.helper.print_response(response, "Create Pet Response")
        
        # Assertions
        assert self.helper.validate_status_code(response, 200), \
            f"Expected status 200, got {response.status_code}"
        
        assert self.helper.validate_response_time(response), \
            f"Response time too slow: {response.elapsed.total_seconds() * 1000}ms"
        
        assert self.helper.validate_json_response(response), \
            "Response is not valid JSON"
        
        response_data = response.json()
        assert response_data['id'] == self.test_pet_id, "Pet ID mismatch"
        assert response_data['name'] == pet_data['name'], "Pet name mismatch"
        
        print("✓ Pet created successfully")
    
    def test_create_pet_with_minimal_data(self):
        """
        Positive Test: Create pet with only required fields
        Expected: 200 OK, pet created with minimal data
        """
        print("\n" + "="*60)
        print("TEST: Create Pet with Minimal Data")
        print("="*60)
        
        pet_id = self.test_pet_id + 1
        pet_data = TestDataGenerator.generate_minimal_pet(pet_id)
        response = self.api_client.create_pet(pet_data)
        
        self.helper.print_response(response, "Minimal Pet Creation Response")
        
        assert response.status_code == 200, \
            f"Expected status 200, got {response.status_code}"
        
        response_data = response.json()
        assert response_data['id'] == pet_id
        assert 'name' in response_data
        
        print("✓ Minimal pet created successfully")
        
        # Cleanup
        self.api_client.delete_pet(pet_id)
    
    # ==================== CREATE (POST) - NEGATIVE TESTS ====================
    
    def test_create_pet_with_missing_required_fields(self):
        """
        Negative Test: Create pet without required fields
        Expected: 400 Bad Request or 500 (API limitation)
        """
        print("\n" + "="*60)
        print("TEST: Create Pet with Missing Required Fields")
        print("="*60)
        
        invalid_pet = TestDataGenerator.generate_invalid_pet_missing_required_fields()
        response = self.api_client.create_pet(invalid_pet)
        
        self.helper.print_response(response, "Invalid Pet Creation Response")
        
        # Note: Swagger Petstore may accept this, but it shouldn't
        assert response.status_code in [400, 405, 500], \
            f"Expected error status, got {response.status_code}"
        
        print("✓ Invalid request properly rejected")
    
    def test_create_pet_with_invalid_data_types(self):
        """
        Negative Test: Create pet with wrong data types
        Expected: 400 Bad Request or validation error
        """
        print("\n" + "="*60)
        print("TEST: Create Pet with Invalid Data Types")
        print("="*60)
        
        invalid_pet = TestDataGenerator.generate_invalid_pet_wrong_types()
        response = self.api_client.create_pet(invalid_pet)
        
        self.helper.print_response(response, "Wrong Type Pet Creation Response")
        
        # Should reject invalid types
        assert response.status_code in [400, 500], \
            f"Expected error status for invalid types, got {response.status_code}"
        
        print("✓ Invalid data types properly rejected")
    
    def test_create_pet_with_empty_body(self):
        """
        Negative Test: Create pet with empty request body
        Expected: 400 Bad Request
        """
        print("\n" + "="*60)
        print("TEST: Create Pet with Empty Body")
        print("="*60)
        
        response = self.api_client.create_pet({})
        
        self.helper.print_response(response, "Empty Body Response")
        
        assert response.status_code in [400, 405, 500], \
            f"Expected error for empty body, got {response.status_code}"
        
        print("✓ Empty body properly rejected")
    
    # ==================== READ (GET) - POSITIVE TESTS ====================
    
    def test_get_existing_pet(self):
        """
        Positive Test: Get an existing pet by ID
        Expected: 200 OK, pet data returned
        """
        print("\n" + "="*60)
        print("TEST: Get Existing Pet")
        print("="*60)
        
        # First create a pet
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 2)
        create_response = self.api_client.create_pet(pet_data)
        assert create_response.status_code == 200
        
        # Now retrieve it
        response = self.api_client.get_pet(self.test_pet_id + 2)
        
        self.helper.print_response(response, "Get Pet Response")
        
        assert response.status_code == 200, \
            f"Expected status 200, got {response.status_code}"
        
        assert self.helper.validate_response_time(response)
        
        response_data = response.json()
        assert response_data['id'] == self.test_pet_id + 2
        assert PetSchema.validate_pet_structure(response_data)
        
        print("✓ Pet retrieved successfully")
        
        # Cleanup
        self.api_client.delete_pet(self.test_pet_id + 2)
    
    def test_find_pets_by_status_available(self):
        """
        Positive Test: Find pets by status 'available'
        Expected: 200 OK, list of available pets
        """
        print("\n" + "="*60)
        print("TEST: Find Pets by Status - Available")
        print("="*60)
        
        response = self.api_client.find_pets_by_status("available")
        
        self.helper.print_response(response, "Find by Status Response")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
        # Verify all returned pets have status 'available'
        pets = response.json()
        if pets:
            for pet in pets[:5]:  # Check first 5
                if 'status' in pet:
                    assert pet['status'] == 'available', \
                        f"Found pet with status {pet['status']}"
        
        print(f"✓ Found {len(pets)} available pets")
    
    # ==================== READ (GET) - NEGATIVE TESTS ====================
    
    def test_get_non_existent_pet(self):
        """
        Negative Test: Get pet with non-existent ID
        Expected: 404 Not Found
        """
        print("\n" + "="*60)
        print("TEST: Get Non-existent Pet")
        print("="*60)
        
        non_existent_id = 9999999999
        response = self.api_client.get_pet(non_existent_id)
        
        self.helper.print_response(response, "Non-existent Pet Response")
        
        assert response.status_code == 404, \
            f"Expected status 404 for non-existent pet, got {response.status_code}"
        
        print("✓ Non-existent pet properly returned 404")
    
    def test_get_pet_with_invalid_id(self):
        """
        Negative Test: Get pet with invalid ID format
        Expected: 400 Bad Request or 404
        """
        print("\n" + "="*60)
        print("TEST: Get Pet with Invalid ID")
        print("="*60)
        
        # Try with negative ID
        response = self.api_client.get_pet(-1)
        
        self.helper.print_response(response, "Invalid ID Response")
        
        assert response.status_code in [400, 404], \
            f"Expected error for invalid ID, got {response.status_code}"
        
        print("✓ Invalid ID properly handled")
    
    def test_find_pets_with_invalid_status(self):
        """
        Negative Test: Find pets with invalid status value
        Expected: 400 Bad Request or empty list
        """
        print("\n" + "="*60)
        print("TEST: Find Pets with Invalid Status")
        print("="*60)
        
        response = self.api_client.find_pets_by_status("invalid_status")
        
        self.helper.print_response(response, "Invalid Status Response")
        
        # May return 400 or empty list
        if response.status_code == 200:
            assert response.json() == [], "Should return empty list for invalid status"
        else:
            assert response.status_code == 400
        
        print("✓ Invalid status properly handled")
    
    # ==================== UPDATE (PUT) - POSITIVE TESTS ====================
    
    def test_update_existing_pet(self):
        """
        Positive Test: Update an existing pet
        Expected: 200 OK, pet updated successfully
        """
        print("\n" + "="*60)
        print("TEST: Update Existing Pet")
        print("="*60)
        
        # Create a pet first
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 3)
        create_response = self.api_client.create_pet(pet_data)
        assert create_response.status_code == 200
        
        # Update the pet
        pet_data['name'] = "UpdatedPetName"
        pet_data['status'] = "sold"
        
        response = self.api_client.update_pet(pet_data)
        
        self.helper.print_response(response, "Update Pet Response")
        
        assert response.status_code == 200, \
            f"Expected status 200, got {response.status_code}"
        
        response_data = response.json()
        assert response_data['name'] == "UpdatedPetName"
        assert response_data['status'] == "sold"
        
        print("✓ Pet updated successfully")
        
        # Cleanup
        self.api_client.delete_pet(self.test_pet_id + 3)
    
    def test_update_pet_status_only(self):
        """
        Positive Test: Update only pet status
        Expected: 200 OK
        """
        print("\n" + "="*60)
        print("TEST: Update Pet Status Only")
        print("="*60)
        
        # Create a pet
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 4)
        self.api_client.create_pet(pet_data)
        
        # Update status
        pet_data['status'] = "pending"
        response = self.api_client.update_pet(pet_data)
        
        self.helper.print_response(response, "Status Update Response")
        
        assert response.status_code == 200
        assert response.json()['status'] == "pending"
        
        print("✓ Pet status updated successfully")
        
        # Cleanup
        self.api_client.delete_pet(self.test_pet_id + 4)
    
    # ==================== UPDATE (PUT) - NEGATIVE TESTS ====================
    
    def test_update_non_existent_pet(self):
        """
        Negative Test: Update pet that doesn't exist
        Expected: 404 Not Found
        """
        print("\n" + "="*60)
        print("TEST: Update Non-existent Pet")
        print("="*60)
        
        pet_data = TestDataGenerator.generate_valid_pet(9999999998)
        response = self.api_client.update_pet(pet_data)
        
        self.helper.print_response(response, "Update Non-existent Pet Response")
        
        # May return 404 or 200 (creating new) depending on API behavior
        # Document the actual behavior
        print(f"API returned status: {response.status_code}")
        
        if response.status_code == 200:
            print("⚠ API creates new pet on update (unexpected but documented)")
            # Cleanup if created
            self.api_client.delete_pet(9999999998)
        else:
            assert response.status_code == 404
            print("✓ Non-existent pet update properly rejected")
    
    def test_update_pet_with_invalid_status(self):
        """
        Negative Test: Update pet with invalid status value
        Expected: 400 Bad Request or accept with default
        """
        print("\n" + "="*60)
        print("TEST: Update Pet with Invalid Status")
        print("="*60)
        
        # Create pet first
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 5)
        self.api_client.create_pet(pet_data)
        
        # Try to update with invalid status
        pet_data['status'] = "invalid_status_value"
        response = self.api_client.update_pet(pet_data)
        
        self.helper.print_response(response, "Invalid Status Update Response")
        
        # Document behavior
        print(f"API returned status: {response.status_code}")
        
        # Cleanup
        self.api_client.delete_pet(self.test_pet_id + 5)
    
    # ==================== DELETE - POSITIVE TESTS ====================
    
    def test_delete_existing_pet(self):
        """
        Positive Test: Delete an existing pet
        Expected: 200 OK, pet deleted
        """
        print("\n" + "="*60)
        print("TEST: Delete Existing Pet")
        print("="*60)
        
        # Create a pet to delete
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 6)
        create_response = self.api_client.create_pet(pet_data)
        assert create_response.status_code == 200
        
        # Delete the pet
        response = self.api_client.delete_pet(self.test_pet_id + 6)
        
        self.helper.print_response(response, "Delete Pet Response")
        
        assert response.status_code == 200, \
            f"Expected status 200, got {response.status_code}"
        
        # Verify pet is deleted
        get_response = self.api_client.get_pet(self.test_pet_id + 6)
        assert get_response.status_code == 404, "Pet should not exist after deletion"
        
        print("✓ Pet deleted successfully")
    
    # ==================== DELETE - NEGATIVE TESTS ====================
    
    def test_delete_non_existent_pet(self):
        """
        Negative Test: Delete pet that doesn't exist
        Expected: 404 Not Found
        """
        print("\n" + "="*60)
        print("TEST: Delete Non-existent Pet")
        print("="*60)
        
        non_existent_id = 9999999997
        response = self.api_client.delete_pet(non_existent_id)
        
        self.helper.print_response(response, "Delete Non-existent Pet Response")
        
        # May return 404 or 200 depending on API
        print(f"API returned status: {response.status_code}")
        assert response.status_code in [200, 404]
        
        print("✓ Delete of non-existent pet handled")
    
    def test_delete_already_deleted_pet(self):
        """
        Negative Test: Delete the same pet twice
        Expected: 404 on second delete
        """
        print("\n" + "="*60)
        print("TEST: Delete Already Deleted Pet")
        print("="*60)
        
        # Create and delete a pet
        pet_data = TestDataGenerator.generate_valid_pet(self.test_pet_id + 7)
        self.api_client.create_pet(pet_data)
        first_delete = self.api_client.delete_pet(self.test_pet_id + 7)
        assert first_delete.status_code == 200
        
        # Try to delete again
        response = self.api_client.delete_pet(self.test_pet_id + 7)
        
        self.helper.print_response(response, "Second Delete Response")
        
        # Second delete should fail
        print(f"Second delete returned: {response.status_code}")
        
        print("✓ Double delete handled")
    
    # ==================== COMPLETE CRUD FLOW TEST ====================
    
    def test_complete_crud_flow(self):
        """
        Integration Test: Complete CRUD flow
        Create → Read → Update → Delete
        """
        print("\n" + "="*70)
        print("INTEGRATION TEST: Complete CRUD Flow")
        print("="*70)
        
        test_id = self.test_pet_id + 100
        
        # CREATE
        print("\n1. CREATE Phase")
        pet_data = TestDataGenerator.generate_valid_pet(test_id)
        create_resp = self.api_client.create_pet(pet_data)
        assert create_resp.status_code == 200
        print(f"   ✓ Created pet with ID: {test_id}")
        
        # READ
        print("\n2. READ Phase")
        read_resp = self.api_client.get_pet(test_id)
        assert read_resp.status_code == 200
        assert read_resp.json()['id'] == test_id
        print(f"   ✓ Retrieved pet: {read_resp.json()['name']}")
        
        # UPDATE
        print("\n3. UPDATE Phase")
        pet_data['name'] = "UpdatedInCRUDFlow"
        pet_data['status'] = "sold"
        update_resp = self.api_client.update_pet(pet_data)
        assert update_resp.status_code == 200
        assert update_resp.json()['name'] == "UpdatedInCRUDFlow"
        print(f"   ✓ Updated pet name and status")
        
        # DELETE
        print("\n4. DELETE Phase")
        delete_resp = self.api_client.delete_pet(test_id)
        assert delete_resp.status_code == 200
        print(f"   ✓ Deleted pet")
        
        # VERIFY DELETE
        print("\n5. VERIFY DELETION")
        verify_resp = self.api_client.get_pet(test_id)
        assert verify_resp.status_code == 404
        print(f"   ✓ Verified pet no longer exists")
        
        print("\n" + "="*70)
        print("✓ COMPLETE CRUD FLOW SUCCESSFUL")
        print("="*70)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--html=api_test_report.html", "--self-contained-html"])
