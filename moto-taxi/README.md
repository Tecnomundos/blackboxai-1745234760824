# Moto Taxi Application

A modern motorcycle taxi service web application built with HTML, CSS (Tailwind), and JavaScript.

## Quality Assurance and Testing

### Setup Testing Environment

1. Install test dependencies:
```bash
pip install -r requirements-test.txt
```

2. Install Firefox WebDriver (required for Selenium tests):
```bash
# On Ubuntu/Debian
sudo apt-get install firefox-geckodriver

# On MacOS
brew install geckodriver

# On Windows
# Download geckodriver from https://github.com/mozilla/geckodriver/releases
```

### Running Tests

To run all tests and quality checks:
```bash
python run_tests.py
```

This will:
- Run code formatting checks (black)
- Run code quality checks (pylint)
- Execute all tests (pytest)
- Generate test coverage report
- Generate test results report

### Test Reports

After running tests, you can find:
- Test results report at: `test-reports/report.html`
- Coverage report at: `htmlcov/index.html`

### Continuous Integration

The test suite includes:
1. **Frontend Tests** (`tests/test_frontend.py`):
   - UI component testing
   - User interaction testing
   - Responsive design testing

2. **Quality Checks**:
   - Code formatting (black)
   - Code quality (pylint)
   - Test coverage reporting

### Development Workflow

1. **Before Making Changes**:
   - Create a new branch for your feature/fix
   - Run tests to ensure everything is working

2. **During Development**:
   - Write tests for new features
   - Keep code coverage high
   - Follow code style guidelines

3. **Before Committing**:
   - Run `black .` to format code
   - Run `pylint moto-taxi` to check code quality
   - Run all tests to ensure nothing is broken

### Code Quality Standards

- Maintain test coverage above 80%
- Follow PEP 8 style guide
- Keep pylint score above 8/10
- Document all functions and classes

## Application Structure

```
moto-taxi/
├── index.html          # Main application page
├── styles.css         # CSS styles
├── script.js         # JavaScript functionality
├── ai_improvements.py # AI-powered code improvements
├── tests/            # Test suite
│   ├── test_frontend.py
│   └── conftest.py
├── requirements-test.txt
└── run_tests.py      # Test runner script
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Run tests and ensure they pass
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
