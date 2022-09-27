# Getting Started
If you would like to contribute, please follow the following steps:
1. Fork the project.
2. Clone your fork: `git clone <your_username>/gVal`
2. Create a feature branch: `git checkout -b <your_feature>`)
3. Commit your changes: `git commit -m 'feature message'`
4. Push to the branch: `git push origin <your_username> <your_feature>`
5. Open a pull request.

# Standards
- [Numpy Style Docstrings](https://numpydoc.readthedocs.io/en/v1.1.0/format.html#documenting-modules)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP8](https://pep8.org/) Styling (and [this](https://peps.python.org/pep-0008/))

# Tooling
- Code Checking with [Flake8](https://github.com/PyCQA/flake8)
    - Combines PyFlakes, pycodestyle, and others for linting and style checking.
- Testing with [PyTests](https://docs.pytest.org/en/7.1.x/contents.html)
    - Checked with [pytest-pep8](https://pypi.org/project/pytest-pep8/)
    - pytest-benchmarking for timed tests
- Dependencies and Packaging
    - [pip](https://packaging.python.org/en/latest/key_projects/#pip)
    - venv
    - Docker
    - [conda](https://www.anaconda.com/products/individual/)
- Distribution
    - [PyPI](https://pypi.org/)
    - DockerHub
    - GitHub (source, packaging, and images)
- Docs
    - [Sphinx](https://www.sphinx-doc.org/)
    - [ReadTheDocs](https://readthedocs.org/)
