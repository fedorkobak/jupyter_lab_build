# Repository Guidelines

## Project Structure & Module Organization
- `jlb.py` is the main entry point. It starts a JupyterLab server (when `--url` is not provided) and opens it in a Gtk/WebKit window.
- `configuration/` contains environment-level JupyterLab defaults (server config plus `overrides.json`).
- `configuration.sh` is a legacy helper that copies settings into the user profile.
- `pyproject.toml` defines packaging metadata, dependencies, and the `jlb` console script.

## Build, Test, and Development Commands
- `pip install -e .` installs the project in editable mode and applies environment-level JupyterLab defaults.
- `jlb` runs the application via the console script defined in `pyproject.toml`.
- `python jlb.py --url http://localhost:8888` opens an existing JupyterLab instance in the Gtk/WebKit shell.

## Coding Style & Naming Conventions
- Python code uses 4-space indentation and standard PEP 8 conventions.
- `pycodestyle` is the preferred linting reference; the suggested config ignores `E303` and `E402` (see `README.md`).
- Use `snake_case` for functions and variables, and keep module-level loggers named with `__name__`.

## Testing Guidelines
- No automated tests are currently defined. If adding tests, place them under `tests/` and name files `test_*.py`.
- Recommended framework: `pytest` (run with `pytest`).

## Commit & Pull Request Guidelines
- Recent commits use short, lowercase, imperative messages (e.g., “add url parsing”). Follow that style.
- PRs should include: a brief summary, how to run or reproduce changes, and notes about any configuration updates. Add screenshots when UI behavior changes.

## Dependencies & Configuration Notes
- The app relies on `PyGObject` and requires system packages; follow the PyGObject installation guidance linked in `README.md`.
- JupyterLab extensions and runtime dependencies are listed in `pyproject.toml`.
