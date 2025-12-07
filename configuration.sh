jupyter_path="${HOME}/.jupyter"
user_settings="${jupyter_path}/lab/user-settings"

mkdir -p $user_settings
cp configuration/jupyter_lab_config.py ${jupyter_path}

cp -r configuration/@jupyterlab ${user_settings}
