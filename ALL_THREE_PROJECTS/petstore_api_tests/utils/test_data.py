from typing import Dict, Any
import random


class TestDataGenerator:
    """Generate test data for API tests"""
    
    @staticmethod
    def generate_valid_pet(pet_id: int = None) -> Dict[str, Any]:
        """Generate valid pet data"""
        if pet_id is None:
            pet_id = random.randint(100000, 999999)
        
        return {
            "id": pet_id,
            "category": {
                "id": random.randint(1, 10),
                "name": "Dogs"
            },
            "name": f"TestDog{pet_id}",
            "photoUrls": [
                "https://example.com/photo1.jpg"
            ],
            "tags": [
                {
                    "id": random.randint(1, 100),
                    "name": "test-tag"
                }
            ],
            "status": "available"
        }
    
    @staticmethod
    def generate_minimal_pet(pet_id: int = None) -> Dict[str, Any]:
        """Generate minimal valid pet data"""
        if pet_id is None:
            pet_id = random.randint(100000, 999999)
        
        return {
            "id": pet_id,
            "name": f"MinimalPet{pet_id}",
            "photoUrls": []
        }
    
    @staticmethod
    def generate_invalid_pet_missing_required_fields() -> Dict[str, Any]:
        """Generate invalid pet data - missing required fields"""
        return {
            "id": random.randint(100000, 999999),
            "category": {
                "id": 1,
                "name": "Dogs"
            }
            # Missing 'name' and 'photoUrls' required fields
        }
    
    @staticmethod
    def generate_invalid_pet_wrong_types() -> Dict[str, Any]:
        """Generate invalid pet data - wrong data types"""
        return {
            "id": "not_a_number",  # Should be integer
            "name": 12345,  # Should be string
            "photoUrls": "not_an_array",  # Should be array
            "status": 123  # Should be string
        }
    
    @staticmethod
    def generate_pet_with_invalid_status() -> Dict[str, Any]:
        """Generate pet with invalid status value"""
        return {
            "id": random.randint(100000, 999999),
            "name": "InvalidStatusPet",
            "photoUrls": [],
            "status": "invalid_status"  # Valid values: available, pending, sold
        }
    
    @staticmethod
    def get_test_pet_id() -> int:
        """Get a fixed test pet ID for CRUD operations"""
        return 999999


class PetSchema:
    """Expected schema for pet objects"""
    
    VALID_STATUSES = ["available", "pending", "sold"]
    
    REQUIRED_FIELDS = ["id", "name", "photoUrls"]
    
    OPTIONAL_FIELDS = ["category", "tags", "status"]
    
    @staticmethod
    def validate_pet_structure(pet_data: Dict[str, Any]) -> bool:
        """Validate pet data structure"""
        # Check required fields
        for field in PetSchema.REQUIRED_FIELDS:
            if field not in pet_data:
                print(f"Missing required field: {field}")
                return False
        
        # Validate data types
        if not isinstance(pet_data.get("id"), int):
            print("ID must be an integer")
            return False
        
        if not isinstance(pet_data.get("name"), str):
            print("Name must be a string")
            return False
        
        if not isinstance(pet_data.get("photoUrls"), list):
            print("photoUrls must be a list")
            return False
        
        # Validate status if present
        if "status" in pet_data:
            if pet_data["status"] not in PetSchema.VALID_STATUSES:
                print(f"Invalid status: {pet_data['status']}")
                return False
        
        return True
