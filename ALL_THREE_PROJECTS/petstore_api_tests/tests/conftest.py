import pytest


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "positive: mark test as positive test scenario"
    )
    config.addinivalue_line(
        "markers", "negative: mark test as negative test scenario"
    )
    config.addinivalue_line(
        "markers", "crud: mark test as CRUD operation test"
    )
