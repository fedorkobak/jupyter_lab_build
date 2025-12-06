jupyter_path="${HOME}/.jupyter"
user_settings="${jupyter_path}/lab/user-settings/@jupyterlab"

mkdir -p $user_settings
cp configuration/jupyter_lab_config.py ${jupyter_path}


mkdir ${user_settings}/shortcuts-extension/
cp configuration/shortcuts.jupyterlab-settings ${user_settings}/shortcuts-extension/

mkdir ${user_settings}/filebrowser-extension/
cp configuration/browser.jupyterlab-settings ${user_settings}/filebrowser-extension/
