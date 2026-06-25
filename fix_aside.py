import re

html = open('c:/Autodecor-web/tiendas.html', encoding='utf-8').read()

# The problematic block is this (inside <aside>):
# </div>      <- this closes the mapa-no-results incorrectly
# </div>      <- this is the extra stray </div> from my previous insertions
# <div class="tienda-card">...MONTERO...</div>
# </div>      <- stray
# </aside>

# Let's find the exact broken block and replace it with the clean version
old_block = """    </div>
      </div>
      <div class="tienda-card">
        <span class="tienda-badge">Sucursal A-16</span>
        <h3>AUTO DECOR GROUP MONTERO</h3>
        <div class="tienda-info">
          <div class="tienda-info-row">
            <span class="icon">\U0001f4cd</span>
            <span>Av. Circunvalaci\u00f3n #755, entre carretera Montero rotonda sur - calle 24 de septiembre</span>
          </div>
          <div class="tienda-info-row">
            <span class="icon">\U0001f4de</span>
            <a href="tel:+59179225335">9-225335</a>
          </div>
        </div>
        <a href="https://www.google.com/maps/place/Importadora+Auto+Decor+sucursal+Montero/@-17.5187629,-63.5306572,10.25z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684397!2d-17.7846097!4e1!1m6!1m2!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!2sImportadora+Auto+Decor+sucursal+Montero,+Circunvalaci%C3%B3n+2do+Anillo+rotonda,+Montero!2m2!1d-63.2491338!2d-17.3519002!3m5!1s0x93ee3d21244a0b3b:0x5467fa213b82bfe8!8m2!3d-17.3519002!4d-63.2491338!16s%2Fg%2F11s_vf3hhh?entry=ttu&g_ep=EgoyMDI2MDYyMy4wIKXMDSoASAFQAw%3D%3D" target="_blank" class="tienda-map-btn">\U0001f4cd Ver en Google Maps</a>
      </div>
</div>
    </aside>"""

clean_block = """    </div>
    </aside>"""

if old_block in html:
    html = html.replace(old_block, clean_block)
    print("Fixed: removed stray tienda-card from inside aside")
else:
    print("WARNING: exact block not found, trying regex approach")
    # Regex approach: find the tienda-card inside the aside
    pattern = r'(</div>\s*</div>\s*<div class="tienda-card">.*?</div>\s*</div>\s*</aside>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        replacement = '    </div>\n    </aside>'
        html = html[:match.start()] + replacement + html[match.end():]
        print("Fixed with regex")
    else:
        print("ERROR: Could not fix automatically")
        # Print the area around mapa-layout for manual inspection
        idx = html.find('mapa-no-results')
        print(repr(html[idx:idx+500]))

open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8').write(html)
print("Saved")
