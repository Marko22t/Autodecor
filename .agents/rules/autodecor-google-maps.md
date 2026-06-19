---
trigger: always_on
---

Eres un experto en integración de Google Maps en sitios web estáticos (HTML/CSS/JS puro).

Tarea: Agregar una sección de mapa interactivo en tiendas.html de Importadora Autodecor Group, Santa Cruz, Bolivia.

REQUISITOS TÉCNICOS:
- Sin API key: usar Google Maps Embed con modo "search" (iframe src con URL de búsqueda)
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

SUCURSALES (coordenadas verificadas de Google Maps):
- A-0: Importadora AUTO DECOR GROUP (A0) | lat: -17.8099091, lng: -63.1937994
- A-1: Importadora Auto Decor Parts A1 | lat: -17.807548, lng: -63.1960457
- A-2: Av. Grigotá #278 | lat: -17.7994666, lng: -63.1946451
- A-3: Av. Roque Aguilera #3940, 3er anillo (Cancha Royal) | lat: -17.7983, lng: -63.1934 (aproximada)
- A-4: Av. Roque Aguilera esq. Castropinto #3580 | lat: -17.7965, lng: -63.1912 (aproximada)
- A-5: Importadora AUTO DECOR GROUP Kia/Hyundai, Av. Roque Aguilera | lat: -17.8054963, lng: -63.1981703
- A-6: Av. Radial 16 #40, Club Hípico, 3er anillo | lat: -17.8117, lng: -63.1969 (aproximada)
- A-7 (Principal): Calle San Miguel, Doble Vía La Guardia | lat: -17.809541, lng: -63.2060247
- A-8: Importadora AUTO DECOR GROUP (A8), Av. Roque Aguilera | lat: -17.8053495, lng: -63.1982955
- A-9: AUTO DECOR GROUP PARAGUÁ, Av. Paraguá | lat: -17.7668332, lng: -63.1509466
- A-10: AUTO DECOR GROUP PAMPA-A3 | lat: -17.7703583, lng: -63.1200507
- A-11: Importadora AUTO DECOR GROUP (A11), Av. Grigotá 32 | lat: -17.7983472, lng: -63.1934053
- A-12: Importadora AUTO DECOR GROUP (A9) | lat: -17.8013323, lng: -63.1346617
- A-13: AUTO DECOR GROUP PLAN 3000 PAURITO, Av. Paurito | lat: -17.8294059, lng: -63.138579
- A-14: Auto Decor Banzer | lat: -17.7607853, lng: -63.1798748
- A-15: Av. Circunvalación #755, Montero | lat: -17.3400, lng: -63.2567 (aproximada)

OUTPUT:
- Dame UN solo bloque de código para insertar en tiendas.html
- Incluir: <style> con todo el CSS + HTML de la sección + <script> con toda la lógica
- El bloque empieza con <!-- MAPA INTERACTIVO --> y termina con <!-- FIN MAPA -->
- Listo para copiar y pegar sin modificaciones