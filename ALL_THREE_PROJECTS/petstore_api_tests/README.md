# PetStore API Test Automation

Comprehensive API test automation for Swagger PetStore API using Python, Requests, and Pytest.

## Project Structure

```
petstore_api_tests/
│
├── tests/
│   ├── conftest.py              # Pytest configuration
│   └── test_pet_crud.py         # Main CRUD test cases
│
├── utils/
│   ├── api_client.py            # API client and helper methods
│   └── test_data.py             # Test data generators and validators
│
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Features

✅ Complete CRUD operations testing (Create, Read, Update, Delete)
✅ Positive test scenarios (happy paths)
✅ Negative test scenarios (error handling)
✅ Data validation and schema verification
✅ Response time validation
✅ Comprehensive error handling
✅ Detailed test reporting
✅ Reusable API client
✅ Test data generators

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Internet connection (to access https://petstore.swagger.io/)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## API Endpoint Tested

**Base URL:** `https://petstore.swagger.io/v2`

**Endpoints:**
- `POST /pet` - Create a new pet
- `GET /pet/{petId}` - Get pet by ID
- `PUT /pet` - Update an existing pet
- `DELETE /pet/{petId}` - Delete a pet
- `GET /pet/findByStatus` - Find pets by status

## Running Tests

### Run all tests with verbose output:
```bash
pytest tests/test_pet_crud.py -v -s
```

### Run with HTML report:
```bash
pytest tests/test_pet_crud.py -v -s --html=api_test_report.html --self-contained-html
```

### Run specific test:
```bash
pytest tests/test_pet_crud.py::TestPetStoreCRUD::test_create_pet_with_valid_data -v -s
```

### Run only positive tests:
```bash
pytest tests/test_pet_crud.py -v -s -k "not negative"
```

### Run only negative tests:
```bash
pytest tests/test_pet_crud.py -v -s -k "negative"
```

## Test Scenarios

### CREATE (POST) Operations

#### Positive Tests:
1. ✅ **test_create_pet_with_valid_data**
   - Create pet with all valid fields
   - Expected: 200 OK

2. ✅ **test_create_pet_with_minimal_data**
   - Create pet with only required fields
   - Expected: 200 OK

#### Negative Tests:
3. ❌ **test_create_pet_with_missing_required_fields**
   - Missing name and photoUrls
   - Expected: 400 Bad Request

4. ❌ **test_create_pet_with_invalid_data_types**
   - Wrong data types (string for ID, number for name)
   - Expected: 400 Bad Request

5. ❌ **test_create_pet_with_empty_body**
   - Empty JSON body
   - Expected: 400 Bad Request

---

### READ (GET) Operations

#### Positive Tests:
6. ✅ **test_get_existing_pet**
   - Retrieve pet by valid ID
   - Expected: 200 OK with pet data

7. ✅ **test_find_pets_by_status_available**
   - Find all pets with status 'available'
   - Expected: 200 OK with list of pets

#### Negative Tests:
8. ❌ **test_get_non_existent_pet**
   - Get pet with non-existent ID
   - Expected: 404 Not Found

9. ❌ **test_get_pet_with_invalid_id**
   - Get pet with negative ID
   - Expected: 400 or 404

10. ❌ **test_find_pets_with_invalid_status**
    - Find pets with invalid status value
    - Expected: 400 or empty list

---

### UPDATE (PUT) Operations

#### Positive Tests:
11. ✅ **test_update_existing_pet**
    - Update existing pet's name and status
    - Expected: 200 OK

12. ✅ **test_update_pet_status_only**
    - Update only the status field
    - Expected: 200 OK

#### Negative Tests:
13. ❌ **test_update_non_existent_pet**
    - Update pet that doesn't exist
    - Expected: 404 (may create new pet - API quirk)

14. ❌ **test_update_pet_with_invalid_status**
    - Update with invalid status value
    - Expected: 400 or accept with default

---

### DELETE Operations

#### Positive Tests:
15. ✅ **test_delete_existing_pet**
    - Delete an existing pet
    - Verify deletion with GET
    - Expected: 200 OK, then 404 on GET

#### Negative Tests:
16. ❌ **test_delete_non_existent_pet**
    - Delete pet that doesn't exist
    - Expected: 404

17. ❌ **test_delete_already_deleted_pet**
    - Delete the same pet twice
    - Expected: 404 on second delete

---

### Integration Test

18. ✅ **test_complete_crud_flow**
    - Complete lifecycle: Create → Read → Update → Delete
    - Validates entire workflow

## Test Data

### Valid Pet Structure:
```json
{
  "id": 123456,
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "name": "TestDog123456",
  "photoUrls": ["https://example.com/photo1.jpg"],
  "tags": [
    {
      "id": 1,
      "name": "test-tag"
    }
  ],
  "status": "available"
}
```

### Required Fields:
- `id` (integer)
- `name` (string)
- `photoUrls` (array)

### Valid Status Values:
- `available`
- `pending`
- `sold`

## Validation Checks

Each test performs the following validations:

1. **Status Code Validation**
   - Verifies expected HTTP status code

2. **Response Time Validation**
   - Ensures response time < 3000ms

3. **JSON Structure Validation**
   - Validates response is valid JSON
   - Checks required fields are present
   - Validates data types

4. **Data Integrity Validation**
   - Verifies created/updated data matches request
   - Confirms deletions are successful

## Sample Test Output

```
======================== test session starts =========================
collected 18 items

tests/test_pet_crud.py::TestPetStoreCRUD::test_create_pet_with_valid_data 
============================================================
TEST: Create Pet with Valid Data
============================================================
✓ Pet created successfully
PASSED

tests/test_pet_crud.py::TestPetStoreCRUD::test_get_non_existent_pet 
============================================================
TEST: Get Non-existent Pet
============================================================
✓ Non-existent pet properly returned 404
PASSED

======================== 18 passed in 15.23s =========================
```

## API Client Usage

The `PetStoreAPIClient` class can be used independently:

```python
from utils.api_client import PetStoreAPIClient

client = PetStoreAPIClient()

# Create a pet
pet_data = {
    "id": 12345,
    "name": "Buddy",
    "photoUrls": []
}
response = client.create_pet(pet_data)

# Get a pet
response = client.get_pet(12345)

# Update a pet
pet_data['status'] = 'sold'
response = client.update_pet(pet_data)

# Delete a pet
response = client.delete_pet(12345)

# Find pets by status
response = client.find_pets_by_status('available')
```

## Error Handling

All tests include comprehensive error handling:

- Try-catch blocks for API calls
- Cleanup of test data in case of failures
- Detailed error messages in assertions
- Response logging for debugging

## Best Practices Implemented

1. ✅ **Separation of Concerns**
   - API client separate from tests
   - Test data generation isolated
   - Helper methods for validation

2. ✅ **Reusability**
   - Common methods in base classes
   - Configurable test data generators
   - Shared fixtures

3. ✅ **Maintainability**
   - Clear test names describing scenarios
   - Detailed docstrings
   - Organized structure

4. ✅ **Comprehensive Coverage**
   - Positive and negative scenarios
   - Edge cases tested
   - Integration tests included

## Known API Limitations

The Swagger PetStore demo API has some quirks:

1. May accept invalid data types without error
2. UPDATE of non-existent pet might create new pet
3. Some validation is lenient for demonstration purposes

These behaviors are documented in the tests.

## Dependencies

- **requests** - HTTP library for API calls
- **pytest** - Testing framework
- **pytest-html** - HTML test reports
- **jsonschema** - JSON validation

## Extending the Tests

To add new test scenarios:

```python
def test_your_new_scenario(self):
    """
    Description of test scenario
    Expected: What should happen
    """
    # Arrange
    pet_data = TestDataGenerator.generate_valid_pet()
    
    # Act
    response = self.api_client.create_pet(pet_data)
    
    # Assert
    assert response.status_code == 200
    
    # Cleanup if needed
    self.api_client.delete_pet(pet_data['id'])
```

## Troubleshooting

### Common Issues:

1. **Connection Errors**
   - Check internet connection
   - Verify API is accessible: https://petstore.swagger.io/

2. **Import Errors**
   - Ensure all dependencies installed
   - Check Python path configuration

3. **Test Failures**
   - Review test output for detailed error messages
   - Check if API endpoint is working
   - Verify test data is valid

## Requirements Compliance

✅ Uses Pet endpoints from https://petstore.swagger.io/
✅ Implements CRUD operations (Create, Read, Update, Delete)
✅ Includes positive test scenarios
✅ Includes negative test scenarios
✅ Written in Python with Requests library
✅ Uses Pytest framework for test execution
✅ Comprehensive test coverage
✅ Detailed documentation

## Contributing

To add new tests:
1. Add test method to `test_pet_crud.py`
2. Use existing API client methods
3. Follow naming convention: `test_<operation>_<scenario>`
4. Include docstring with description and expected result
5. Add cleanup code if creating test data

## License

This is a test automation project for educational and testing purposes.
