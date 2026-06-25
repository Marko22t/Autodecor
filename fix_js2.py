html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()
bad_js = "      { id: 'A-16', lat: -17.3400, lng: -63.2567, title: 'AUTO DECOR GROUP MONTERO', address: 'Av. Circunvalación #755', phone: '9-225335', wp: '' },\n"
html = html.replace(bad_js, '')
# We also have an extra `    ];` at the end of the file or something. Let's fix it by replacing the `var sucursalActiva` line.
# Actually, the original array ended with `    ];`. I'll just find `    var sucursalActiva = null;` and insert before it.
idx = html.find('    var sucursalActiva = null;')
if idx != -1:
    # insert bad_js before the closing bracket of the array. The array closing bracket is `    ];` right above it.
    idx_bracket = html.rfind('];', 0, idx)
    if idx_bracket != -1:
        html = html[:idx_bracket] + bad_js + html[idx_bracket:]
        open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
        print('Fixed JS array')
    else:
        print('Could not find ];')
else:
    print('Could not find sucursalActiva')
