html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()
idx = html.find('mapa-layout')
open('c:/Autodecor-web/temp_layout.txt', 'w', encoding='utf-8').write(html[idx:idx+4000])
print('done')
