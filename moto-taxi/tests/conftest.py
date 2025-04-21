"""
Test configuration for the moto-taxi application.
"""
import pytest
import os
import sys

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for testing."""
    return "http://localhost:8000"


@pytest.fixture(scope="session")
def browser():
    """Configure and return a browser instance for testing."""
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options

    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()
