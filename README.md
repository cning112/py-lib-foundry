# py-lib-foundry

An opinionated Copier template for building modern Python libraries. It generates a src-layout package with typing, Ruff/MyPy, pytest + coverage, pre-commit hooks, GitHub Actions, and optional docs—ready for PyPI and CI.

## Requirements
- Rendering: Copier ≥ 9 and Python ≥ 3.11.
- Defaults note: the template’s post‑render tasks (enabled by default via `setup_dev_env: true`) call `uv`. Either install `uv` or render with `--skip-tasks` (or set `setup_dev_env: false`).
- `nox` is optional. It’s included only when `enable_nox: true` (default). You can disable it at render time and still use `pip`/`pytest`.

## Quickstart
- Interactive render: `copier copy --trust . ../my-lib`
  - The template defines post-render tasks; `--trust` allows them. Use `-T/--skip-tasks` or set `setup_dev_env: false` to skip.
- Render with answers: `copier copy --trust --data-file test-defaults.yml . _render_out`
- Update an existing render: run `copier update` inside the rendered project.

## After Rendering
- If you kept defaults (tasks ran): your environment may already be set up by `uv` and pre‑commit.

- With uv + nox (when `enable_nox: true`):
  - Install deps: `uv sync`
  - Lint/format/type-check: `nox -s lint` (Ruff/MyPy when enabled)
  - Tests: `nox -s tests`
  - Build: `nox -s build`
- Without uv and/or without nox:
  - Create venv: `python -m venv .venv && source .venv/bin/activate`
  - Install package: `pip install -e .`
  - Install tools you want: `pip install pytest pytest-cov ruff mypy build`
  - Run tests: `pytest -v --cov`
  - Build: `python -m build`

## Key Variables (copier.yml)
- `dist_name` (required), `package_name` (defaults from `dist_name`), `repo_name`, `project_name`, `description`, `license`.
- Python: `python_min`, `python_versions`.
- Build/versioning: `build_backend` (`hatchling` or `setuptools`), `versioning` (`static` or `setuptools-scm`).
- Toggles: `enable_ruff`, `enable_mypy`, `enable_precommit`, `enable_nox`, `enable_ci`, `enable_pypi`, `include_py_typed`.
- Docs: `docs_tool` (`mkdocs`, `sphinx`, or `none`).
- Setup: `setup_dev_env` (if true, runs `uv sync` and installs pre-commit).

## Developing This Template
- Try a sample render: `copier copy --trust --data-file test-defaults.yml . _render_out`
- When changing variables, update `copier.yml` validators, `_exclude_if`, and `_tasks`.
- Tag releases (e.g., `v0.1.0`) so consumers can pin versions.
