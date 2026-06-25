html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

# We know the bad Montero JS text at the end of the file is exactly this:
bad_js = "      { id: 'A-16', lat: -17.3400, lng: -63.2567, title: 'AUTO DECOR GROUP MONTERO', address: 'Av. Circunvalación #755', phone: '9-225335', wp: '' },\n"

# Remove all occurrences of bad_js
html = html.replace(bad_js, '')
# Also remove the one that might be somewhat deformed at the end of the file if needed.
# Since we just appended it in the previous script, it should match `bad_js` exactly.
import re
# Remove the exact bad string from the end of the file if it's there
if html.endswith("wp: '' },\\n"):
   pass # string replacement should have caught it

# Find the array end using regex
match = re.search(r'\];\s*var sucursalActiva = null;', html)
if match:
    idx = match.start()
    html = html[:idx] + bad_js + '    ' + html[idx:]
    open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
    print('Fixed JS array')
else:
    print('Could not find ]; var sucursalActiva')
