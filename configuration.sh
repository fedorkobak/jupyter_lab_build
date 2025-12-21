jupyter_path="${HOME}/.jupyter"
user_settings="${jupyter_path}/lab/user-settings"

mkdir -p $user_settings

cp -r configuration/@jupyterlab ${user_settings}
