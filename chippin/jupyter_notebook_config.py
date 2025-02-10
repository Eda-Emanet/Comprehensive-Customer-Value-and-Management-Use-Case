c = get_config()

# Jupyter Notebook'un kimlik doğrulamasını devre dışı bırak (şifre ve token kullanma)
c.NotebookApp.token = ''
c.NotebookApp.password = ''

# Jupyter Notebook'un belirtilen IP adresi ve port üzerinden çalışmasını sağla
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888

# Jupyter Notebook'un otomatik olarak tarayıcıda açılmasını engelle
c.NotebookApp.open_browser = False