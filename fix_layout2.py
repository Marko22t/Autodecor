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

# Let's remove the card again if it's there
html = html.replace(card_text, '')
# Now find where mapa-sidebar-list ends
idx = html.find('</div>\n      </aside>')
if idx != -1:
    html = html[:idx] + card_text + html[idx:]
    open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
    print("Fixed layout correctly inside list")
else:
    # let's try another heuristic
    idx2 = html.find('</aside>')
    html = html[:idx2-10] + card_text + html[idx2-10:]
    open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
    print("Fixed layout fallback")
