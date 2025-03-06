# Contributing to Holded API Wrapper

Thank you for considering contributing to the Holded API Wrapper! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:

- A clear, descriptive title
- A detailed description of the bug
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any relevant logs or error messages
- Your environment (Python version, operating system, etc.)

### Suggesting Enhancements

If you have an idea for an enhancement, please create an issue on GitHub with the following information:

- A clear, descriptive title
- A detailed description of the enhancement
- Any relevant examples or use cases
- Any potential implementation details

### Pull Requests

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Add or update tests as necessary
5. Run the tests to ensure they pass
6. Update documentation as necessary
7. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/BonifacioCalindoro/holded-python.git
   cd holded-python
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. Install development dependencies:
   ```bash
   pip install pytest pytest-cov flake8
   ```

## Running Tests

Run the tests with pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=holded
```

## Code Style

This project follows the PEP 8 style guide. You can check your code with flake8:

```bash
flake8 holded tests
```

## Documentation

Please update the documentation when making changes to the code. This includes:

- Docstrings for new functions, classes, and methods
- Updates to the README.md file if necessary
- Updates to the documentation in the docs/ directory if necessary

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License. 