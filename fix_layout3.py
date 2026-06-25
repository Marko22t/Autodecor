import re

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

# Let's clean up the corrupted part
# Look for "<      <div class="tienda-card">"
pattern = r"<\s*<\s*div class=\"tienda-card\">\s*<span class=\"tienda-badge\">Sucursal A-16</span>[\s\S]*?/div>\s*</aside>"
html = re.sub(pattern, "    </div>\n    </aside>", html)

# If it's something else, let's just do a clean replace using a custom regex
html = re.sub(r"<\s*<div class=\"tienda-card\">.*?/div>\s*</aside>", "    </div>\n    </aside>", html, flags=re.DOTALL)
html = html.replace("<      <div class=\"tienda-card\">", "    </div>\n    </aside>")

# Remove any stray Montero card HTML block if it exists
html = re.sub(r"\s*<div class=\"tienda-card\">\s*<span class=\"tienda-badge\">Sucursal A-16</span>\s*<h3>AUTO DECOR GROUP MONTERO</h3>[\s\S]*?</div>\s*</div>\s*", "\n", html)

# Now inject it properly
# Find the exact ending of the sidebar list. It should be right before </aside>
idx = html.find('</aside>')
if idx != -1:
    # There is a closing </div> for mapa-sidebar-list right before </aside>
    last_div = html.rfind('</div>', 0, idx)
    if last_div != -1:
        html = html[:last_div] + card_text + html[last_div:]
        open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
        print("Fixed layout accurately")
    else:
        print("Could not find closing div before aside")
else:
    print("Could not find aside")
