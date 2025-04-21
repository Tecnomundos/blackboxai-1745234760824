"""
Test runner script for the moto-taxi application.
This script runs all tests and generates reports.
"""
import subprocess
import os
import sys


def run_style_checks():
    """Run code style checks using black and pylint."""
    print("Running style checks...")

    # Run Black formatter
    subprocess.run(["black", "."], check=True)

    # Run Pylint with disabled invalid-name warning for the module
    subprocess.run(
        ["pylint", "--disable=C0103", "moto-taxi"],  # Disable invalid-name warning
        check=True,
    )


def run_tests():
    """Run all tests and generate coverage report."""
    print("Running tests with coverage...")

    # Create reports directory if it doesn't exist
    os.makedirs("test-reports", exist_ok=True)

    # Run pytest with coverage and generate HTML report
    subprocess.run(
        [
            "pytest",
            "--cov=moto-taxi",
            "--cov-report=html",
            "--html=test-reports/report.html",
            "moto-taxi/tests/",  # Updated path to tests directory
        ],
        check=True,
    )


if __name__ == "__main__":
    try:
        # Create reports directory if it doesn't exist
        os.makedirs("test-reports", exist_ok=True)

        # Run style checks
        run_style_checks()

        # Run tests
        run_tests()

        print("\nAll tests and checks completed successfully!")
        print("Test report available at: test-reports/report.html")
        print("Coverage report available at: htmlcov/index.html")

    except subprocess.CalledProcessError as e:
        print(f"\nError: {e}")
        sys.exit(1)
