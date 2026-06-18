---
trigger: always_on
---

Eres un experto en integración de Google Maps en sitios web estáticos (HTML/CSS/JS puro).

Tarea: Agregar una sección de mapa interactivo en tiendas.html de Importadora Autodecor Group, Santa Cruz, Bolivia.

REQUISITOS TÉCNICOS:
- Sin API key: usar Google Maps Embed con modo "search" (iframe src con URL de búsqueda)
- Para el mapa general usar: https://www.google.com/maps/embed/v1/search?q=Importadora+Autodecor+Santa+Cruz+Bolivia (o similar sin key)
- Al seleccionar sucursal: cambiar el src del iframe con coordenadas específicas vía JS
- Sin frameworks, sin librerías externas

DISEÑO:
- Colores: azul #1565c0, amarillo #f5c518
- Fuentes: Bebas Neue (títulos), Barlow (cuerpo)
- Modo oscuro/claro compatible con variables CSS existentes
- Layout: sidebar izquierdo con lista de sucursales + mapa a la derecha
- Mobile: lista arriba, mapa abajo (stack vertical)
- Buscador para filtrar sucursales en tiempo real
- Tarjeta de info al seleccionar (nombre, dirección, botón WhatsApp, botón "Abrir en Maps")

SUCURSALES (usar estas coordenadas aproximadas de Santa Cruz de la Sierra):
- A-1: Av. Grigotá #38, 2do anillo | coords: -17.7756, -63.1827
- A-2: Av. Grigotá #278, entre 2do y 3er anillo | coords: -17.7821, -63.1834
- A-3: Av. Roque Aguilera #3940, 3er anillo | coords: -17.7983, -63.1934
- A-4: Av. Roque Aguilera esq. Castropinto #3580 | coords: -17.7965, -63.1912
- A-5: Av. Roque Aguilera #3940, 3er anillo interno | coords: -17.7990, -63.1940
- A-6: Av. Radial 16 #40, 3er anillo | coords: -17.7845, -63.2015
- A-7 (Principal): Calle San Miguel, Doble Vía La Guardia | coords: -17.8102, -63.1456
- A-8: 4to anillo #4596, Av. Grigotá sur | coords: -17.7980, -63.1820
- A-9: Av. Paraguá #3600, antes del 4to anillo | coords: -17.7634, -63.1923
- A-10: Av. Moscú #5120, La Cuchilla, 5to anillo | coords: -17.7523, -63.2145
- A-11: Av. 3 Pasos al Frente #5035, 6to anillo | coords: -17.8234, -63.1678
- A-12: Av. Virgen de Cotoca, 5to-6to anillo | coords: -17.8312, -63.1345
- A-13: Av. Paurito, Plan 3000, 7mo anillo | coords: -17.8456, -63.1234
- A-14: Av. Banzer, 7mo-8vo anillo | coords: -17.7412, -63.2234
- A-15: Av. Circunvalación #755, Montero | coords: -17.3412, -63.2567

OUTPUT:
- Dame UN solo bloque de código para insertar en tiendas.html
- Incluir: <style> con todo el CSS + HTML de la sección + <script> con toda la lógica
- El bloque empieza con <!-- MAPA INTERACTIVO --> y termina con <!-- FIN MAPA -->
- Listo para copiar y pegar sin modificaciones