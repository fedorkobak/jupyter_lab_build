# JupyterLab build

Custom JupyterLab build that launches JupyterLab inside a Gtk/WebKit window.

## Requirements

- Python 3.8+
- System packages for `PyGObject` (see [Installing PyGObject in Ubuntu/Debian](https://pygobject.gnome.org/getting_started.html#ubuntu-logo-ubuntu-debian-logo-debian))


## Usage

Run the bundled app (starts a JupyterLab server if no URL is provided):

```bash
jlb
```

Open an existing JupyterLab instance:

```bash
jlb --url http://localhost:8888
```

## Configuration

Apply the repository configuration:

```bash
bash configuration.sh
```

Settings live under `configuration/` with per-extension `.jupyterlab-settings` files.

## Coding Style

Use `pycodestyle` and ignore `E303` and `E402`:

```ini
[pycodestyle]
ignore = E303,E402
```

Place this in `setup.cfg` or `~/.config/pycodestyle`.
