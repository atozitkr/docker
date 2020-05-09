# get the config object
c = get_config()
# Location for users notebooks
c.JupyterHub.bind_url = 'http://127.0.0.1:8888'
c.JupyterHub.hub_connect_ip = 'notebook'
c.NotebookApp.base_project_url = '/notebook/'
c.NotebookApp.base_url = '/notebook/'
c.NotebookApp.trust_xheaders = True
c.NotebookApp.webapp_settings = {'static_url_prefix': '/notebook/static/'}
c.NotebookApp.token = ''
c.NotebookApp.allow_origin = '*'

