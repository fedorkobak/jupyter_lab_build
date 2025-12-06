# JupyterLab build

Custom JupyterLab build.

## Dependencies

Uses `PyGObject` to run JupyterLab in a special window. This require special packages from your system so check [Installing PyGObject in Ubuntu/Debian](https://pygobject.gnome.org/getting_started.html#ubuntu-logo-ubuntu-debian-logo-debian).

## Configuration

Install configuration:

```bash
cp shortcuts.jupyterlab-settings ~/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/
cp jupyter_lab_config.py ~/.jupyter
```
