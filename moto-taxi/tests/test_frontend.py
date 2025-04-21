"""
Frontend testing module for the moto-taxi application.
Tests the UI components and their functionality.
"""
import unittest
import os
from bs4 import BeautifulSoup


class TestFrontend(unittest.TestCase):
    """Test cases for the frontend components."""

    def setUp(self):
        """Set up the test environment."""
        # Read the HTML file
        with open(
            os.path.join("moto-taxi", "index.html"), "r", encoding="utf-8"
        ) as file:
            self.html_content = file.read()
            self.soup = BeautifulSoup(self.html_content, "html.parser")

    def test_page_title(self):
        """Test if the page title is correct."""
        title = self.soup.title.string
        self.assertEqual(title, "Moto Taxi")

    def test_search_functionality(self):
        """Test if the search form elements exist."""
        # Check for pickup location input
        pickup_input = self.soup.find("input", {"placeholder": "Local de Coleta"})
        self.assertIsNotNone(pickup_input, "Pickup location input should exist")

        # Check for dropoff location input
        dropoff_input = self.soup.find("input", {"placeholder": "Local de Destino"})
        self.assertIsNotNone(dropoff_input, "Dropoff location input should exist")

        # Check for search button
        search_button = self.soup.find("button")
        self.assertIsNotNone(search_button, "Search button should exist")

    def test_language_selector(self):
        """Test if the language selector exists with correct options."""
        # Check for language selector
        language_selector = self.soup.find("select", {"id": "language"})
        self.assertIsNotNone(language_selector, "Language selector should exist")

        # Check for language options
        options = language_selector.find_all("option")
        self.assertGreater(len(options), 1, "Should have multiple language options")

        # Verify Portuguese is the default language
        pt_option = language_selector.find("option", {"value": "pt"})
        self.assertIsNotNone(pt_option, "Portuguese option should exist")
        self.assertEqual(pt_option.text, "Português")


if __name__ == "__main__":
    unittest.main()
