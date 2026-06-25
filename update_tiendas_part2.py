import re

html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

# --- PART 1: JS Array Montero Fix ---
# Remove any bad Montero lines
html = re.sub(r"\{\s*id:\s*'A-16'.*?\},?\s*", "", html)

correct_montero = "    { id: 'A-16', nombre: 'AUTO DECOR GROUP MONTERO', direccion: 'Av. Circunvalación #755, entre carretera Montero rotonda sur - calle 24 de septiembre', lat: -17.3390, lng: -63.2567, wa: '', principal: false },\n"
match = re.search(r'\];\s*var sucursalActiva = null;', html)
if match:
    html = html[:match.start()] + correct_montero + '  ' + html[match.start():]
else:
    print("WARNING: Could not find JS array end for Montero injection.")

# --- PART 2: Cards specific landline updates ---
def update_card(title_marker, old_tel_text=None, new_tel_text=None):
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
    if old_tel_text and new_tel_text:
        old_href = old_tel_text.replace('-', '')
        new_href = new_tel_text.replace('-', '')
        new_card = new_card.replace(f'tel:+5913{old_href}', f'tel:+5913{new_href}')
        new_card = new_card.replace(old_tel_text, new_tel_text)
    
    html = html.replace(card, new_card)

# Make sure these specific ones requested are correct
update_card('<h3>Importadora Auto Decor Parts A1</h3>', '3-598338', '3-556190')
update_card('<h3>Importadora AUTO DECOR GROUP (A8)</h3>', '3-519706', '3-556190')
update_card('<h3>Sucursal Principal', '3-596851', '3-488925')
update_card('<h3>Importadora AUTO DECOR GROUP (A11)</h3>', '3-640162', '3-598338')

# Ensure Montero card has correct html structure
if 'AUTO DECOR GROUP MONTERO' not in html:
    new_card = """      <div class="tienda-card">
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
    sidebar_idx = html.find('<!-- SIDEBAR -->')
    html = html[:sidebar_idx] + new_card + "      " + html[sidebar_idx:]

# --- PART 3: Counter Fix ---
html = html.replace('<div class="mapa-counter" id="mapaCounter">15 sucursales</div>', '<div class="mapa-counter" id="mapaCounter">16 sucursales</div>')

open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
print("Updated successfully.")
