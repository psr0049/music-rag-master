# Contributing to Music RAG System

We love your input! We want to make contributing to the Music RAG System as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/music-rag-system.git
   cd music-rag-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking
- **Pytest** for testing

Run these before submitting:
```bash
black src/ tests/
flake8 src/ tests/
mypy src/
pytest tests/
```

### Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Use descriptive test names

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_rag_system.py
```

### Documentation

- Update docstrings for new functions/classes
- Add type hints to function signatures
- Update README.md if needed
- Add examples for new features

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using GitHub's [issue tracker](https://github.com/yourusername/music-rag-system/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/music-rag-system/issues/new).

### Bug Reports

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

### Feature Requests

We welcome feature requests! Please:

- Check if the feature already exists
- Explain the use case
- Provide examples if possible
- Consider if it fits the project scope

## Project Structure

```
music-rag-system/
├── src/                    # Source code
│   ├── core/              # Core RAG functionality
│   ├── apps/              # Streamlit applications
│   ├── utils/             # Utility modules
│   └── rlhf/              # RLHF components
├── tests/                 # Test suite
├── docs/                  # Documentation
├── examples/              # Example scripts
└── data/                  # Sample data
```

## Coding Guidelines

### Python Style

- Follow PEP 8
- Use type hints
- Write descriptive docstrings
- Keep functions focused and small
- Use meaningful variable names

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Branch Naming

- `feature/feature-name` for new features
- `bugfix/bug-description` for bug fixes
- `docs/documentation-update` for documentation
- `refactor/component-name` for refactoring

## Areas for Contribution

### High Priority
- [ ] Performance optimizations
- [ ] Additional recommendation algorithms
- [ ] Better error handling
- [ ] More comprehensive tests

### Medium Priority
- [ ] UI/UX improvements
- [ ] Additional data sources
- [ ] Mobile responsiveness
- [ ] Internationalization

### Low Priority
- [ ] Additional visualizations
- [ ] Export functionality
- [ ] Advanced filtering options
- [ ] Theme customization

## Getting Help

- Check existing issues and discussions
- Join our community discussions
- Reach out to maintainers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Don't hesitate to ask questions! Create an issue or reach out to the maintainers.

---

Thank you for contributing to the Music RAG System! 🎵