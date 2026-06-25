html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()
idx = html.find('<div class="mapa-layout">')
open('c:/Autodecor-web/temp_html_layout.txt', 'w', encoding='utf-8').write(html[idx:idx+3000])
print('done, mapa-layout starts at:', idx)
