# Contributing to Leaditor

Thank you for your interest in contributing to Leaditor! We appreciate your help and value your contributions, whether they are issues, code improvements, or new features. Please follow these guidelines to contribute effectively.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Style Guide](#style-guide)
- [License](#license)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all participants to adhere to it and will not tolerate any form of harassment or discrimination.

## How to Contribute

### Reporting Bugs

If you encounter any bugs, please report them by opening an issue. Make sure to include detailed information about the bug, steps to reproduce it, and any relevant screenshots or logs.

### Suggesting Enhancements

We welcome suggestions for new features and improvements. Please open an issue to discuss your ideas. Provide as much detail as possible, including potential use cases and benefits.

### Submitting Pull Requests

1. Fork the repository and create your branch from `main`.
2. Ensure your code follows the [Style Guide](#style-guide).
3. Write clear and concise commit messages.
4. Update or add documentation as needed.
5. Test your changes thoroughly.
6. Submit a pull request with a detailed description of your changes.

## Development Setup

To set up your development environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ponram7/leaditor.git
   cd leaditor
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Style Guide

Please follow these guidelines to maintain code consistency:

- **Python**: Follow PEP 8 guidelines. Use `black` for formatting and `flake8` for linting.
- **HTML/CSS**: Use semantic HTML and follow best practices for CSS. Ensure styles are responsive and accessible.
- **JavaScript**: Use ES6+ features and follow best practices. Use `prettier` for formatting and `eslint` for linting.

## License

By contributing to Leaditor, you agree that your contributions will be licensed under the [MIT License](LICENSE).

Thank you for contributing to Leaditor!