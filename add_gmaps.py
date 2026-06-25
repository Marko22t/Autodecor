with open('c:/Autodecor-web/tiendas.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map of links to add by nombre substring (key) → gmaps URL
# Cross-referenced by lat/lng matching between user-provided links and current JS array entries

gmaps_to_add = {
    # A-11 (lat -17.807548) ← user's "A1" link (matches coords)
    "Importadora Auto Decor Parts A1": "https://www.google.com/maps/place/Importadora+%22Auto+Decor+Parts%22+A1/@-17.8075336,-63.2320905,14z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684186!2d-17.7846239!4e1!1m6!1m2!1s0x93f1e825c61f1021:0x129c8be685c21c57!2sImportadora+%22Auto+Decor+Parts%22+A1,+Santa+Cruz+de+la+Sierra!2m2!1d-63.1960364!2d-17.8075417!3m5!1s0x93f1e825c61f1021:0x129c8be685c21c57!8m2!3d-17.807548!4d-63.1960457!16s%2Fg%2F11gcm2ckw_?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
    # A-2 (lat -17.7994666) ← user's "A2" link (matches coords)
    "Importadora Auto Decor Parts A2": "https://www.google.com/maps/place/Importadora+%22Auto+Decor+Parts%22+A2/@-17.7994638,-63.2306957,14z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684397!2d-17.7846097!4e1!1m6!1m2!1s0x93f1e91165f32881:0xa94aea7d0100f958!2sImportadora+%22Auto+Decor+Parts%22+A2,+Av.+Grigot%C3%A1+278,+Santa+Cruz+de+la+Sierra!2m2!1d-63.1946451!2d-17.7994666!3m5!1s0x93f1e91165f32881:0xa94aea7d0100f958!8m2!3d-17.7994666!4d-63.1946451!16s%2Fg%2F11rylgjjry?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
    # A-8 (lat -17.8053495) ← user's "A8" link (matches coords)
    "Importadora AUTO DECOR GROUP (A8)": "https://www.google.com/maps/place/Importadora+AUTO+DECOR+GROUP+(A8)/@-17.8053477,-63.2343435,14z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684186!2d-17.7846239!4e1!1m6!1m2!1s0x93f1e90003a44f8d:0x5634a62ad89e072b!2sImportadora+AUTO+DECOR+GROUP+(A8),+5RV2%2BQJC,+Santa+Cruz+de+la+Sierra!2m2!1d-63.1982962!2d-17.80535!3m5!1s0x93f1e90003a44f8d:0x5634a62ad89e072b!8m2!3d-17.8053495!4d-63.1982955!16s%2Fg%2F11w98lnypl?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
    # A-7 (lat -17.7668332) ← user's "A7" link (matches coords)
    "AUTO DECOR GROUP PARAGU": "https://www.google.com/maps/place/AUTO+DECOR+GROUP+PARAGU%C3%81/@-17.7757584,-63.1700993,15z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684186!2d-17.7846239!4e1!1m6!1m2!1s0x93f1e62bdacdc171:0x38fb0ce88807c695!2sAUTO+DECOR+GROUP+PARAGU%C3%81,+Av.+Paragu%C3%A1,+Santa+Cruz+de+la+Sierra!2m2!1d-63.1509466!2d-17.7668332!3m5!1s0x93f1e62bdacdc171:0x38fb0ce88807c695!8m2!3d-17.7668332!4d-63.1509466!16s%2Fg%2F11cnb6q2cv?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
    # A-10 (lat -17.7703583, Av. Moscú La Cuchilla) ← user's "A3" link (coords match: -17.7703583, -63.1200507)
    "AUTO DECOR GROUP PAMPA-A3": "https://www.google.com/maps/place/AUTO+DECOR+GROUP+PAMPA-A3/@-17.7788785,-63.1863389,13z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684186!2d-17.7846239!4e1!1m6!1m2!1s0x93f1e93583c84f75:0x4a75a1fc8ce6a647!2sAUTO+DECOR+GROUP+PAMPA-A3,+000000!2m2!1d-63.1200507!2d-17.7703583!3m5!1s0x93f1e93583c84f75:0x4a75a1fc8ce6a647!8m2!3d-17.7703583!4d-63.1200507!16s%2Fg%2F11t36p9rc3?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
    # A-4 (lat -17.8294059, Plan 3000) ← user's "A4" link (matches coords)
    "AUTO DECOR GROUP PLAN 3000 PAURITO": "https://www.google.com/maps/place/AUTO+DECOR+GROUP+PLAN+3000+PAURITO/@-17.8064177,-63.1970001,13z/data=!4m20!1m13!4m12!1m4!2m2!1d-63.1684186!2d-17.7846239!4e1!1m6!1m2!1s0x93f1e99e10f0688f:0xbd4486e4429d8743!2sAUTO+DECOR+GROUP+PLAN+3000+PAURITO,+pasando+la,+Entel+-+Plan+3000,+Sobre+la+Av.+Paurito,+Av.+Principal+Plan+3+Mil,+Santa+Cruz+de+la+Sierra!2m2!1d-63.138579!2d-17.8294059!3m5!1s0x93f1e99e10f0688f:0xbd4486e4429d8743!8m2!3d-17.8294059!4d-63.138579!16s%2Fg%2F11vqpd78tc?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D",
}

# Note: user's "A10" link (lat -17.809541) → same coords as A-21 (already has gmaps) → skip
# Note: user's "A18" link (lat -17.7220507) → same coords as A-24 (already has gmaps) → skip
# Note: user's "A100" link (lat -17.809541) → same coords as A-21 (already has gmaps) → skip
# Note: user's "A22" link has different coords from A-22 in array → user instruction says don't touch coords → skip

def add_or_replace_gmaps(nombre_substr, gmaps_url):
    global html
    idx = html.find(f"nombre: '{nombre_substr}")
    if idx == -1:
        print(f"NOT FOUND: {nombre_substr}")
        return
    
    # Find end of this entry (next `},` or `}`)
    entry_end = html.find('},', idx)
    entry = html[idx:entry_end+2]
    
    if 'gmaps:' in entry:
        # Replace existing gmaps value
        gstart = entry.find("gmaps: '") + 8
        gend = entry.find("'", gstart)
        new_entry = entry[:gstart] + gmaps_url + entry[gend:]
        print(f"Replaced gmaps for {nombre_substr}")
    else:
        # Add gmaps before closing }
        close = entry.rfind('}')
        new_entry = entry[:close] + f", gmaps: '{gmaps_url}' " + entry[close:]
        print(f"Added gmaps for {nombre_substr}")
    
    html = html.replace(entry, new_entry)

for nombre, url in gmaps_to_add.items():
    add_or_replace_gmaps(nombre, url)

with open('c:/Autodecor-web/tiendas.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done.")
