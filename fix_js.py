html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

bad_js = "      { id: 'A-16', lat: -17.3400, lng: -63.2567, title: 'AUTO DECOR GROUP MONTERO', address: 'Av. Circunvalación #755', phone: '9-225335', wp: '' },\n"

html = html.replace(bad_js, '')
# Find where the js array ends
array_end = html.find('  ];\n  \n    var sucursalActiva = null;')
if array_end != -1:
    html = html[:array_end] + bad_js + html[array_end:]
    open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
    print('Fixed JS array')
else:
    print('Could not find JS array end')
