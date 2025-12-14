# JupyterLab build

Custom JupyterLab build.

## Dependencies

Uses `PyGObject` to run JupyterLab in a special window. This require special packages from your system so check [Installing PyGObject in Ubuntu/Debian](https://pygobject.gnome.org/getting_started.html#ubuntu-logo-ubuntu-debian-logo-debian).

## Configuration

Install configuration run script `configuration.sh`.

To configure the `pycodestyle` put the configuration:

```ini
[pycodestyle]
ignore = E303,E402
```

To the `setup.cfg` of the project or `~/.config/pycodestyle` for the user scope configuration.