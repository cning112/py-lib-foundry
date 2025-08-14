# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Copier template for Python packages (repo: "py-lib-foundry"). It generates modern Python projects with comprehensive tooling including testing, linting, formatting, documentation, and CI/CD.

## Architecture

- **Template Engine**: Uses Copier with Jinja2 templating
- **Configuration**: `copier.yml` defines all template variables and conditional file generation
- **Template Structure**: All template files are in the `template/` directory with `.jinja` extensions
- **Generated Project Structure**: 
  - `src/{{ package_name }}/` - Main package code
  - `tests/` - Test files using pytest
  - `pyproject.toml` - Project configuration with uv dependency management
  - Optional tooling based on template choices (ruff, mypy, nox, pre-commit, CI/CD)

## Development Commands

### Template Testing and Generation
```bash
# Generate a new project from template
copier copy . /path/to/new-project

# Update existing project with template changes  
copier update /path/to/existing-project
```

### Generated Project Commands
The template generates projects with these standard commands:

#### Testing
```bash
# Run tests (for generated projects)
uv run pytest
uv run pytest --cov={{ package_name }} --cov-report=html
uv run pytest tests/test_{{ package_name }}.py -v

# Via nox (if enabled)
nox -s tests
```

#### Code Quality
```bash
# Formatting and linting (if ruff enabled)
uv run ruff format
uv run ruff check --fix

# Type checking (if mypy enabled)
uv run mypy src

# All quality checks via nox (if enabled)
nox -s lint

# Pre-commit hooks (if enabled)
pre-commit run --all-files
```

#### Building
```bash
# Build package
uv build

# Build and verify via nox
nox -s build

# Clean artifacts
nox -s clean
```

## Template Configuration

### Key Variables in copier.yml
- `dist_name`: PyPI distribution name
- `package_name`: Python import name (derived from dist_name)
- `python_min/python_versions`: Python version support
- `build_backend`: hatchling or setuptools
- `versioning`: static or setuptools-scm
- Feature toggles: `enable_ruff`, `enable_mypy`, `enable_precommit`, `enable_nox`, `enable_ci`, `enable_pypi`
- `docs_tool`: mkdocs, sphinx, or none

### Conditional File Generation
Files are conditionally generated based on template variables using `_exclude_if` in copier.yml. For example, CI workflows are only generated if `enable_ci` is true.

### Post-Generation Tasks
The template automatically runs setup tasks after generation:
- `uv sync --all-extras --all-groups` (if setup_dev_env enabled)
- `uv run pre-commit install` (if setup_dev_env and enable_precommit)

## Common Modifications

When updating the template:
1. Modify template files in `template/` directory
2. Update `copier.yml` for new variables or conditional logic
3. Test generation with different variable combinations
4. Ensure generated projects follow modern Python packaging best practices

The template emphasizes uv for dependency management, comprehensive testing with pytest, modern linting with ruff, and optional automation with nox.
