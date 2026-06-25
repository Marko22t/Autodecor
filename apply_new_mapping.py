import re

with open('c:/Autodecor-web/tiendas.html', 'r', encoding='utf-8') as f:
    html = f.read()

# First, let's remove the Montero card from HTML if it exists (my previous script added it)
html = re.sub(r'[\s]*<div class="tienda-card">\s*<span class="tienda-badge">Sucursal A-16</span>\s*<h3>AUTO DECOR GROUP MONTERO</h3>[\s\S]*?</div>\s*</div>', '\n    </div>', html)
# If my regex matched the list closing div, I just replaced it with `</div>`. Let's be safer.
html = re.sub(r'\s*<div class="tienda-card">\s*<span class="tienda-badge">Sucursal A-16</span>\s*<h3>AUTO DECOR GROUP MONTERO</h3>[\s\S]*?</div>\s*', '\n', html)
# This one removes the card up to its first closing div, wait it might have nested divs.
# I'll just use a safer string replacement since I know the exact string I generated earlier.
old_card_text1 = """      <div class="tienda-card">
        <span class="tienda-badge">Sucursal A-16</span>
        <h3>AUTO DECOR GROUP MONTERO</h3>
        <div class="tienda-info">
          <div class="tienda-info-row">
            <span class="icon">📍</span>
            <span>Av. Circunvalación #755, entre carretera Montero rotonda sur - calle 24 de septiembre</span>
          </div>
          <div class="tienda-info-row">
            <span class="icon">📞</span>
            <a href="tel:+59179225335">9-225335</a>
          </div>
        </div>
      </div>
"""
old_card_text2 = """      <div class="tienda-card">
          <span class="tienda-badge">Sucursal A-16</span>
          <h3>AUTO DECOR GROUP MONTERO</h3>
          <div class="tienda-info">
            <div class="tienda-info-row">
              <span class="icon">📍</span>
              <span>Av. Circunvalación #755, entre carretera Montero rotonda sur - calle 24 de septiembre</span>
            </div>
            <div class="tienda-info-row">
              <span class="icon">📞</span>
              <a href="tel:+59179225335">9-225335</a>
            </div>
          </div>
        </div>
"""
html = html.replace(old_card_text1, '')
html = html.replace(old_card_text2, '')

# Remove Montero from JS
html = re.sub(r"\s*\{\s*id:\s*'A-16',.*?\},", "", html)

# Re-read JS array to apply mappings safely
def replace_js_id(nombre_substring, new_id):
    global html
    idx = html.find(nombre_substring)
    if idx != -1:
        id_idx = html.rfind("id: '", 0, idx)
        if id_idx != -1:
            end_quote = html.find("'", id_idx + 5)
            html = html[:id_idx + 5] + new_id + html[end_quote:]

replace_js_id('Importadora Auto Decor Parts A1', 'A-11')
replace_js_id('Importadora AUTO DECOR GROUP (Kia, Hyundai)', 'A-12')
replace_js_id('Sucursal Principal', 'A-21')
replace_js_id('AUTO DECOR GROUP PARAGU', 'A-7')
replace_js_id('Importadora AUTO DECOR GROUP (A11)', 'A-1')
replace_js_id('Importadora AUTO DECOR GROUP (A9)', 'A-9')
replace_js_id('AUTO DECOR GROUP PLAN 3000 PAURITO', 'A-4')
replace_js_id('Auto Decor Banzer', 'A-18')
replace_js_id('Quinto Anillo, Av. San Mart', 'A-22')
replace_js_id('Imp.AutoDecorGroup', 'A-100')
replace_js_id('Importadora AutoDecor Banzer', 'A-24')

# Add new Montero JS
correct_montero_js = "    { id: 'A-16', nombre: 'AUTO DECOR GROUP MONTERO', direccion: 'Av. Circunvalación #755, entre carretera Montero rotonda sur - calle 24 de septiembre', lat: -17.3519002, lng: -63.2491338, wa: '', principal: false, gmaps: 'https://www.google.com/maps/place/Importadora+Auto+Decor+sucursal+Montero/@-17.5187629,-63.5306572,10.25z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684397!2d-17.7846097!4e1!1m6!1m2!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!2sImportadora+Auto+Decor+sucursal+Montero,+Circunvalaci%C3%B3n+2do+Anillo+rotonda,+Montero!2m2!1d-63.2491338!2d-17.3519002!3m5!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!8m2!3d-17.3519002!4d-63.2491338!16s%2Fg%2F11s_vf3hhh?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D' },\n"
match = re.search(r'\];\s*var sucursalActiva = null;', html)
if match:
    html = html[:match.start()] + correct_montero_js + '  ' + html[match.start():]

# Now fix HTML cards
def set_badge(title_marker, new_badge):
    global html
    idx = html.find(title_marker)
    if idx == -1: return
    start_card = html.rfind('<div class="tienda-card">', 0, idx)
    
    # robust end of card finding
    end_card = html.find('</div>\n      </div>', idx)
    if end_card == -1: end_card = html.find('<a href="https://www.google', idx)
    if end_card == -1: end_card = html.find('<!-- SIDEBAR -->', idx)
    
    card = html[start_card:end_card]
    new_card = card
    
    badge_start = new_card.find('<span class="tienda-badge')
    if badge_start != -1:
        badge_inner_start = new_card.find('>', badge_start) + 1
        badge_inner_end = new_card.find('</span>', badge_inner_start)
        new_card = new_card[:badge_inner_start] + new_badge + new_card[badge_inner_end:]
    
    html = html.replace(card, new_card)

set_badge('<h3>Importadora Auto Decor Parts A1</h3>', 'Sucursal A-11')
set_badge('<h3>Importadora AUTO DECOR GROUP (Kia, Hyundai)</h3>', 'Sucursal A-12')
set_badge('<h3>Sucursal Principal', '⭐ Sucursal A-21 · Principal')
set_badge('<h3>AUTO DECOR GROUP PARAGU', 'Sucursal A-7')
set_badge('<h3>Importadora AUTO DECOR GROUP (A11)</h3>', 'Sucursal A-1')
set_badge('<h3>Importadora AUTO DECOR GROUP (A9)</h3>', 'Sucursal A-9')
set_badge('<h3>AUTO DECOR GROUP PLAN 3000 PAURITO</h3>', 'Sucursal A-4')
set_badge('<h3>Auto Decor Banzer</h3>', 'Sucursal A-18')
set_badge('<h3>Autodecor</h3>', 'Sucursal A-22')
set_badge('<h3>Imp.AutoDecorGroup</h3>', 'Sucursal A-100')
set_badge('<h3>Importadora AutoDecor Banzer</h3>', 'Sucursal A-24')

# Add Montero card properly
new_montero_html = """      <div class="tienda-card">
        <span class="tienda-badge">Sucursal A-16</span>
        <h3>AUTO DECOR GROUP MONTERO</h3>
        <div class="tienda-info">
          <div class="tienda-info-row">
            <span class="icon">📍</span>
            <span>Av. Circunvalación #755, entre carretera Montero rotonda sur - calle 24 de septiembre</span>
          </div>
          <div class="tienda-info-row">
            <span class="icon">📞</span>
            <a href="tel:+59179225335">9-225335</a>
          </div>
        </div>
        <a href="https://www.google.com/maps/place/Importadora+Auto+Decor+sucursal+Montero/@-17.5187629,-63.5306572,10.25z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684397!2d-17.7846097!4e1!1m6!1m2!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!2sImportadora+Auto+Decor+sucursal+Montero,+Circunvalaci%C3%B3n+2do+Anillo+rotonda,+Montero!2m2!1d-63.2491338!2d-17.3519002!3m5!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!8m2!3d-17.3519002!4d-63.2491338!16s%2Fg%2F11s_vf3hhh?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D" target="_blank" class="tienda-map-btn">📍 Ver en Google Maps</a>
      </div>
"""
aside_idx = html.find('</aside>')
if aside_idx != -1:
    list_end = html.rfind('</div>', 0, aside_idx)
    html = html[:list_end] + new_montero_html + html[list_end:]

html = html.replace('<div class="mapa-counter" id="mapaCounter">15 sucursales</div>', '<div class="mapa-counter" id="mapaCounter">16 sucursales</div>')

open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
print("Updated successfully")
