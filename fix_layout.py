html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

card_text = """      <div class="tienda-card">
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

# Remove the card that is placed BEFORE <!-- SIDEBAR -->
html = html.replace(card_text + "      <!-- SIDEBAR -->", "      <!-- SIDEBAR -->")
# Just in case whitespace was slightly different
html = html.replace(card_text, "")

# Find where to put it
# The list is in <div class="mapa-sidebar-list" id="sidebarList">
# It ends right before <div class="mapa-view" id="mapa"> or right before </aside>
# Actually, looking at the code, it's `</aside>\n      <!-- MAIN MAP -->`

# Let's find </aside>
aside_end = html.find('</aside>')
if aside_end != -1:
    # insert before </aside>, wait, there might be a closing </div> for mapa-sidebar-list before </aside>
    list_end = html.rfind('</div>', 0, aside_end)
    html = html[:list_end] + card_text + html[list_end:]
    open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
    print("Fixed layout")
else:
    print("Error: Could not find </aside>")
