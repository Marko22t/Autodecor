import re

with open('nosotros.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We know the content up to the first two services is correct.
# We will match up to 'Asesoría Personalizada'
good_part = content.split('<h3>Asesoría Personalizada</h3>')[0]
good_part += '<h3>Asesoría Personalizada</h3>\n        <p>Nuestros expertos te guían para encontrar el repuesto exacto que tu vehículo necesita, sin errores.</p>\n      </div>\n'

# The rest of the file
rest_of_file = """      <div class="servicio-card">
        <div class="servicio-icon">📋</div>
        <h3>Catálogo Online</h3>
        <p>Consulta nuestra amplia variedad de productos organizados por marca, modelo y categoría.</p>
      </div>
      <div class="servicio-card">
        <div class="servicio-icon">📦</div>
        <h3>Venta al Por Mayor</h3>
        <p>Precios especiales para mecánicas, talleres y distribuidores. Contáctanos para una cotización personalizada.
        </p>
      </div>
      <div class="servicio-card">
        <div class="servicio-icon">⏰</div>
        <h3>Atención Oportuna</h3>
        <p>Respondemos rápido a cada consulta. Tu tiempo es valioso y lo sabemos.</p>
      </div>
    </div>
  </section>

  <!-- BRAND SHOWCASE BANNER -->
  <section class="brand-showcase">
    <img src="img/autodecor1-hq.png" alt="Autodecor Group Banner" class="brand-showcase-img">
  </section>
  <footer>
    <div class="footer-grid">
      <div>
        <a href="index.html" class="footer-brand-logo">
          <img src="img/logo.png" alt="Autodecor">
          <div class="footer-brand-name">AUTO<span>DECOR</span> GROUP</div>
        </a>
        <p class="footer-brand">Más de 35 años siendo el proveedor de confianza en repuestos y accesorios automotrices
          en Bolivia.</p>
      </div>
      <div class="footer-col">
        <h4>Navegación</h4>
        <ul class="footer-links">
          <li><a href="index.html">Inicio</a></li>
          <li><a href="nosotros.html">Nosotros</a></li>
          <li><a href="productos.html">Productos</a></li>
          <li><a href="tiendas.html">Tiendas</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contacto</h4>
        <ul class="footer-links">
          <li><a href="mailto:gerencia@autodecor.com.bo">gerencia@autodecor.com.bo</a></li>
          <li><a href="mailto:ventas-a0@autodecor.com.bo">ventas-a0@autodecor.com.bo</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 <span>Importadora Autodecor Group</span> — Todos los derechos reservados.</p>
      <p>Fundada en <span>1988</span> · Santa Cruz, Bolivia</p>
    </div>
  </footer>

  <script>
    // Navigation Hamburger
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });

    // Theme Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');

    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }

    themeToggleBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      const isDark = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
  </script>

  <!-- FLOATING CONTACT BUTTONS -->
  <div class="floating-buttons">
    <a href="https://wa.me/59175364818" target="_blank" class="float-btn float-whatsapp" title="Escríbenos por WhatsApp">
      <svg viewBox="0 0 24 24">
        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.057 5.284 5.349 0 11.859 0c3.151.001 6.115 1.23 8.344 3.461 2.23 2.231 3.458 5.195 3.457 8.348-.003 6.557-5.297 11.84-11.807 11.84-2.001-.001-3.968-.51-5.717-1.488L0 24zm6.59-4.846c1.6.95 3.197 1.451 4.793 1.452 5.568 0 10.1-4.526 10.103-10.096.002-2.699-1.047-5.236-2.951-7.14C16.63 1.464 14.09 .417 11.858.417a10.1 10.1 0 0 0-10.097 10.1c-.001 1.761.472 3.483 1.369 5.021l-.974 3.561 3.65-.958zm12.03-5.269c-.327-.164-1.938-.956-2.237-1.064-.299-.11-.517-.164-.734.164-.217.327-.844 1.064-1.034 1.282-.19.218-.38.245-.707.081-.327-.164-1.381-.508-2.63-1.622-.972-.867-1.628-1.938-1.819-2.264-.19-.327-.02-.504.144-.666.147-.146.327-.382.49-.573.163-.19.217-.327.326-.545.11-.218.054-.409-.027-.573-.082-.164-.734-1.769-1.007-2.422-.265-.636-.53-.55-.734-.56-.19-.01-.408-.012-.625-.012-.218 0-.573.082-.872.409-.299.327-1.143 1.117-1.143 2.724 0 1.608 1.171 3.159 1.334 3.377.163.218 2.302 3.515 5.576 4.925.779.336 1.387.537 1.862.688.783.248 1.496.213 2.059.129.628-.094 1.938-.792 2.21-1.556.272-.764.272-1.418.19-1.556-.081-.136-.298-.218-.626-.382z"/>
      </svg>
    </a>
    <a href="https://www.facebook.com/importadora.autodecor.group/?locale=es_LA" target="_blank" class="float-btn float-facebook" title="Síguenos en Facebook">
      <svg viewBox="0 0 24 24">
        <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
      </svg>
    </a>
  </div>

</body>

</html>
"""

with open('nosotros.html', 'w', encoding='utf-8') as f:
    f.write(good_part + rest_of_file)
