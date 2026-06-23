# Plan: Fix Google Maps Links — Mostrar nombre del negocio

## Problema
Los enlaces "Abrir en Maps" y "Ver en Google Maps" usan `?api=1&query=lat,lng` que solo muestra un pin genérico sin el nombre de la tienda.

## Solución
Cambiar formato a: `https://www.google.com/maps/search/NOMBRE/@lat,lng,17z`

---

## Cambio 1 — Popups del mapa (`tiendas.html:2043`)

**Actual:**
```js
var mapsUrl = 'https://www.google.com/maps/search/?api=1&query=' + s.lat + ',' + s.lng;
```

**Nuevo:**
```js
var mapsUrl = 'https://www.google.com/maps/search/' + encodeURIComponent(s.nombre + ' ' + s.direccion) + '/@' + s.lat + ',' + s.lng + ',17z';
```

---

## Cambio 2 — Botón "Abrir en Maps" (`tiendas.html:2140`)

**Actual:**
```js
document.getElementById('mapaMapsBtn').href = 'https://www.google.com/maps/search/?api=1&query=' + s.lat + ',' + s.lng;
```

**Nuevo:**
```js
document.getElementById('mapaMapsBtn').href = 'https://www.google.com/maps/search/' + encodeURIComponent(s.nombre + ' ' + s.direccion) + '/@' + s.lat + ',' + s.lng + ',17z';
```

---

## Cambio 3 — Tarjetas HTML estáticas

Cada enlace `tienda-map-btn` debe cambiarse al nuevo formato.

### A-0 (línea 1135)
```
https://www.google.com/maps/search/Av.+Grigot%C3%A1+y+4to+Anillo+Santa+Cruz+Bolivia
```
→
```
https://www.google.com/maps/search/Importadora+AUTO+DECOR+GROUP+(A0)/@-17.8099091,-63.1937994,17z
```

### A-1 (línea 1156)
```
https://www.google.com/maps/search/?api=1&query=2do+anillo+Av.+Grigot%C3%A1+%2338+Santa+Cruz+Bolivia
```
→
```
https://www.google.com/maps/search/Importadora+Auto+Decor+Parts+A1/@-17.807548,-63.1960457,17z
```

### A-2 (línea 1183)
```
https://www.google.com/maps/search/?api=1&query=Av.+Grigot%C3%A1+%23278+Santa+Cruz+Bolivia
```
→
```
https://www.google.com/maps/search/Av.+Grigot%C3%A1+#278/@-17.7994666,-63.1946451,17z
```

### A-3 (línea 1204) — SIN COORDENADAS, dejar igual
```
https://www.google.com/maps/search/?api=1&query=Av.+Roque+Aguilera+%233940+Santa+Cruz+Bolivia
```

### A-4 — SIN COORDENADAS, dejar igual
```
https://www.google.com/maps/search/?api=1&query=Av.+Roque+Aguilera+castropinto+%233580+Santa+Cruz+Bolivia
```

### A-5 (línea 1249)
```
https://www.google.com/maps/search/?api=1&query=-17.8054963,-63.1981703
```
→
```
https://www.google.com/maps/search/Importadora+AUTO+DECOR+GROUP+Kia+Hyundai/@-17.8054963,-63.1981703,17z
```

### A-6 — SIN COORDENADAS, dejar igual
```
https://www.google.com/maps/search/?api=1&query=Av.+Radial+16+club+h%C3%ADpico+%2340+Santa+Cruz+Bolivia
```

### A-7 (línea 1297)
```
https://www.google.com/maps/search/?api=1&query=-17.809541,-63.2060247
```
→
```
https://www.google.com/maps/search/Sucursal+Principal+Doble+V%C3%ADa+La+Guardia/@-17.809541,-63.2060247,17z
```

### A-8 (línea 1319)
```
https://www.google.com/maps/search/?api=1&query=-17.8053495,-63.1982955
```
→
```
https://www.google.com/maps/search/Importadora+AUTO+DECOR+GROUP+(A8)/@-17.8053495,-63.1982955,17z
```

### A-9 (línea 1339)
```
https://www.google.com/maps/search/?api=1&query=-17.7668332,-63.1509466
```
→
```
https://www.google.com/maps/search/AUTO+DECOR+GROUP+PARAGU%C3%81/@-17.7668332,-63.1509466,17z
```

### A-10 (línea 1360)
```
https://www.google.com/maps/search/?api=1&query=-17.7703583,-63.1200507
```
→
```
https://www.google.com/maps/search/AUTO+DECOR+GROUP+PAMPA-A3/@-17.7703583,-63.1200507,17z
```

### A-11 (línea 1381)
```
https://www.google.com/maps/search/?api=1&query=-17.7983472,-63.1934053
```
→
```
https://www.google.com/maps/search/Importadora+AUTO+DECOR+GROUP+(A11)/@-17.7983472,-63.1934053,17z
```

### A-12 (línea 1401)
```
https://www.google.com/maps/search/?api=1&query=-17.8013323,-63.1346617
```
→
```
https://www.google.com/maps/search/Importadora+AUTO+DECOR+GROUP+(A9)/@-17.8013323,-63.1346617,17z
```

### A-13 (línea 1422)
```
https://www.google.com/maps/search/?api=1&query=-17.8294059,-63.138579
```
→
```
https://www.google.com/maps/search/AUTO+DECOR+GROUP+PLAN+3000+PAURITO/@-17.8294059,-63.138579,17z
```

### A-14 (línea 1443)
```
https://www.google.com/maps/search/?api=1&query=-17.7607853,-63.1798748
```
→
```
https://www.google.com/maps/search/Auto+Decor+Banzer/@-17.7607853,-63.1798748,17z
```

### A-15 — SIN COORDENADAS, dejar igual
```
https://www.google.com/maps/search/?api=1&query=Av.+circunvalaci%C3%B3n+%23755+Montero+Bolivia
```
