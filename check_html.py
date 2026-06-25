import re
html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

sidebar_idx = html.find('<!-- SIDEBAR -->')
print(html[sidebar_idx-1000:sidebar_idx+1000].encode('utf-8'))
