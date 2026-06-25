with open('c:/Autodecor-web/tiendas.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The issue is that replace_js_id used rfind which finds the closest `id:` before the nombre.
# Let's fix Kia (should be A-12) and A8 (should be A-8) which are still showing as A-1.
# We need to find their exact positions.

# Kia/Hyundai: find its entry in the JS array
kia_idx = html.find("nombre: 'Importadora AUTO DECOR GROUP (Kia, Hyundai)'")
if kia_idx != -1:
    id_idx = html.rfind("id: '", 0, kia_idx)
    end_quote = html.find("'", id_idx + 5)
    current_id = html[id_idx + 5:end_quote]
    print(f"Kia current id: {current_id}")
    html = html[:id_idx + 5] + 'A-12' + html[end_quote:]

# A8: find its entry in the JS array
a8_idx = html.find("nombre: 'Importadora AUTO DECOR GROUP (A8)'")
if a8_idx != -1:
    id_idx = html.rfind("id: '", 0, a8_idx)
    end_quote = html.find("'", id_idx + 5)
    current_id = html[id_idx + 5:end_quote]
    print(f"A8 current id: {current_id}")
    html = html[:id_idx + 5] + 'A-8' + html[end_quote:]

# Also fix the A-1 in PARTS A1: should be A-11
parts_a1_idx = html.find("nombre: 'Importadora Auto Decor Parts A1'")
if parts_a1_idx != -1:
    id_idx = html.rfind("id: '", 0, parts_a1_idx)
    end_quote = html.find("'", id_idx + 5)
    current_id = html[id_idx + 5:end_quote]
    print(f"Parts A1 current id: {current_id}")
    html = html[:id_idx + 5] + 'A-11' + html[end_quote:]

# Also fix A-11 (Av. Grigotá 32) should be A-1
a11_idx = html.find("nombre: 'Importadora AUTO DECOR GROUP (A11)'")
if a11_idx != -1:
    id_idx = html.rfind("id: '", 0, a11_idx)
    end_quote = html.find("'", id_idx + 5)
    current_id = html[id_idx + 5:end_quote]
    print(f"A11 current id: {current_id}")
    html = html[:id_idx + 5] + 'A-1' + html[end_quote:]

# A-3 (Virgen de Cotoca) should be A-9
a9_idx = html.find("nombre: 'Importadora AUTO DECOR GROUP (A9)'")
if a9_idx != -1:
    id_idx = html.rfind("id: '", 0, a9_idx)
    end_quote = html.find("'", id_idx + 5)
    current_id = html[id_idx + 5:end_quote]
    print(f"A9 current id: {current_id}")
    html = html[:id_idx + 5] + 'A-9' + html[end_quote:]

with open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done fixing JS IDs")
