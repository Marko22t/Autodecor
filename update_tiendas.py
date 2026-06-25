import re

with open('c:/Autodecor-web/tiendas.html', 'r', encoding='utf-8') as f:
    html = f.read()

def update_card(title_marker, new_badge, old_landline=None, new_landline=None, add_landline=None):
    global html
    idx = html.find(title_marker)
    if idx == -1:
        print(f"NOT FOUND: {title_marker}")
        return
    
    start_card = html.rfind('<div class="tienda-card">', 0, idx)
    end_card = html.find('<a href="https://www.google', idx)
    if end_card == -1: end_card = html.find('</div>\n        <a href="', idx)
    if end_card == -1: end_card = html.find('</div>\n      </div>', idx)
    
    if start_card == -1 or end_card == -1:
        print(f"CARD BOUNDARIES NOT FOUND for {title_marker}")
        return

    card = html[start_card:end_card]
    new_card = card
    
    # 1. Replace badge
    # find the badge span content
    badge_start = new_card.find('<span class="tienda-badge')
    if badge_start != -1:
        badge_inner_start = new_card.find('>', badge_start) + 1
        badge_inner_end = new_card.find('</span>', badge_inner_start)
        old_badge_full = new_card[badge_inner_start:badge_inner_end]
        
        # Keep any prefix like ⭐ if it's there in the new badge
        new_card = new_card[:badge_inner_start] + new_badge + new_card[badge_inner_end:]
    
    # 2. Update landline if modifying
    if old_landline and new_landline:
        old_tel = old_landline.replace("-", "")
        new_tel = new_landline.replace("-", "")
        # replace the tel string in href
        new_card = new_card.replace(f'href="tel:+5913{old_tel}"', f'href="tel:+5913{new_tel}"')
        # replace the visible text
        new_card = new_card.replace(f'>{old_landline}<', f'>{new_landline}<')
        
    # 3. Add landline if needed
    if add_landline:
        # Check if already exists to avoid duplicates
        if add_landline not in new_card:
            tel_num = add_landline.replace("-", "")
            landline_html = f'          <div class="tienda-info-row">\n            <span class="icon">📞</span>\n            <a href="tel:+5913{tel_num}">{add_landline}</a>\n          </div>\n        '
            
            # Find where to insert: right before the last closing </div> of tienda-info
            tienda_info_end = new_card.rfind('</div>')
            if tienda_info_end != -1:
                new_card = new_card[:tienda_info_end] + landline_html + new_card[tienda_info_end:]

    html = html.replace(card, new_card)
    print(f"Updated {title_marker}")

# The changes requested:
update_card('<h3>Importadora AUTO DECOR GROUP (A0)</h3>', 'Sucursal A-0 · Central', add_landline='3-547150')
update_card('<h3>Importadora Auto Decor Parts A1</h3>', 'Sucursal A-11') # landline 3-598338 is kept
update_card('<h3>Importadora Auto Decor Parts A2</h3>', 'Sucursal A-2', add_landline='3-537899')
update_card('<h3>Importadora AUTO DECOR GROUP (Kia, Hyundai)</h3>', 'Sucursal A-8') # landline correct
update_card('<h3>Sucursal Principal', '⭐ Sucursal A-21 · Principal', old_landline='3-596851', new_landline='3-488925')
update_card('<h3>Importadora AUTO DECOR GROUP (A8)</h3>', 'Sucursal A-1', old_landline='3-519706', new_landline='3-556190')
update_card('<h3>AUTO DECOR GROUP PARAGU', 'Sucursal A-7') # landline correct
update_card('<h3>AUTO DECOR GROUP PAMPA-A3</h3>', 'Sucursal A-10') # landline correct
update_card('<h3>Importadora AUTO DECOR GROUP (A11)</h3>', 'Sucursal A-11', old_landline='3-640162', new_landline='3-598338')
update_card('<h3>Importadora AUTO DECOR GROUP (A9)</h3>', 'Sucursal A-3') # landline correct
update_card('<h3>AUTO DECOR GROUP PLAN 3000 PAURITO</h3>', 'Sucursal A-4') # landline correct
update_card('<h3>Auto Decor Banzer</h3>', 'Sucursal A-18') # landline correct
update_card('<h3>Autodecor</h3>', 'Sucursal A-22', add_landline='3-542131')
update_card('<h3>Imp.AutoDecorGroup</h3>', 'Sucursal A-100', add_landline='3-519706')
update_card('<h3>Importadora AutoDecor Banzer</h3>', 'Sucursal A-24', add_landline='3-518800')

# Adding new card for Montero
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
# Insert before <!-- SIDEBAR -->
sidebar_idx = html.find('<!-- SIDEBAR -->')
html = html[:sidebar_idx] + new_card + "      " + html[sidebar_idx:]

# JS Array replacements
js_replacements = [
    ("{ id: 'A-5',", "{ id: 'A-8',"),
    ("{ id: 'A-7',", "{ id: 'A-21',"),
    ("{ id: 'A-8',", "{ id: 'A-1',"),
    ("{ id: 'A-9',", "{ id: 'A-7',"),
    ("{ id: 'A-12',", "{ id: 'A-3',"),
    ("{ id: 'A-13',", "{ id: 'A-4',"),
    ("{ id: 'A-14',", "{ id: 'A-18',"),
    ("{ id: 'A-15',", "{ id: 'A-22',"),
    ("{ id: 'A-16',", "{ id: 'A-100',"),
    ("{ id: 'A-17',", "{ id: 'A-24',"),
]
for old, new in js_replacements:
    html = html.replace(old, new)

# add montero entry
montero_js = "      { id: 'A-16', lat: -17.3400, lng: -63.2567, title: 'AUTO DECOR GROUP MONTERO', address: 'Av. Circunvalación #755', phone: '9-225335', wp: '' },\n"
idx_js_end = html.find('    ];', html.find('const sucursales = ['))
html = html[:idx_js_end] + montero_js + html[idx_js_end:]

with open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("All done.")
