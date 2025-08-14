# Repository Guidelines

## Project Structure & Module Organization
- `copier.yml`: Template variables, validation, and post-render `_tasks` (e.g., `uv sync`, `pre-commit`).
- `template/`: Project scaffold rendered by Copier. Key parts:
  - `pyproject.toml.jinja`, `noxfile.py.jinja`, `README.md.jinja`, `LICENSE.jinja`.
  - `src/{{ package_name }}/`: Python package with `__init__.py.jinja` and optional `py.typed`.
  - `tests/`: Example `pytest` test (`test_{{ package_name }}.py.jinja`).
- `test-*.yml`: Example Copier answers for validation (`test-defaults.yml`, `test-invalid.yml`, `test-validation.yml`).
- `CLAUDE.md`: Notes for LLM collaborators; keep in sync with this guide.

## Build, Test, and Development Commands
- Render locally (interactive): `copier copy . ../my-lib`
- Render with canned answers: `copier copy -f -a test-defaults.yml . /tmp/out`
- Update an existing render: `copier update` (run inside the rendered project)
- After rendering, in the new project:
  - Install deps: `uv sync`
  - Lint: `nox -s lint`
  - Tests: `nox -s tests` or `uv run pytest -v`
  - Build: `nox -s build`

## Coding Style & Naming Conventions
- Python 3.11+; 4-space indentation; line length 120; double quotes.
- Lint/format via Ruff (imports sorted, common flake8 rules). Type-check with MyPy if enabled.
- Naming: `dist_name` uses hyphens (PyPI), `package_name` is `snake_case` (import path), `repo_name` mirrors `dist_name`.
- Place code under `src/{{ package_name }}` and tests under `tests/`.

## Testing Guidelines
- Framework: `pytest` with `pytest-cov`; sample test provided in `template/tests`.
- Name tests `test_*.py`; mark `unit`, `integration`, or `slow` as needed (see `pyproject` markers).
- Run via `nox -s tests`; ensure coverage reports generate without errors.

## Commit & Pull Request Guidelines
- Commits: clear, scoped messages (prefer Conventional Commits style if practical, e.g., `feat: add option enable_ruff`).
- PRs: include description of template changes, impact on rendered output, and any migration notes.
- If you add/rename variables, update `copier.yml` validators, `_exclude_if`, `_tasks`, and adjust `test-*.yml` accordingly.
- Include sample render commands in the PR to reproduce.

## Agent-Specific Tips
- Keep examples minimal and reproducible; favor commands that work with Copier ≥ 9 and `uv`/`nox-uv`.
- Validate both interactive and answers-file flows before merging.
