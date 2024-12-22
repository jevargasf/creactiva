# creactiva
Repositorio aplicación web Creactiva Animaciones

Enviando un saludo desde mi máquina local

admin
creactiva

javier@creactiva.cl
usuario1

próximos pasos:

App cursos:
    ✔ sistema de permisos: bloque if else para manejar permisos de visualización en template
    ✔ insertar c1e1_player en base.html: ahora será un html aparte exclusivo para servir los videos
    ✔ curso: público, capítulo: privado
    - problema: ¿cómo restringir el acceso a los links de los mp4 que están alojados en el hosting?
    - ¿qué necesita un capítulo? *diferenciarlo de los archivos necesarios para el reproductor, que son todos el mismo
        - config.xml: img/1.png
        - config_xml.js: scripts/config_xml.js // Ojo, en este se deben configurar más links, pero todavía no puedo hacerlo desde el backend, se debe hacer manual
        - thumbnails.png: c1e1_Thumbnails.png
        - first_frame.png: img/1.png
        - mp4: https://www.creactivaanimaciones.cl/static/media/c1e1.mp4

    -  generar un uuid para que no se "note" que el id del curso es 1, 2, etc

App principal, control de permisos:
    ✔ sección login/registro
    ✔ primera restricción de permisos: invitado/usuario (usuarios no logueados no pueden acceder al contenido)
    - segunda restricción de permisos: usuario/cliente

Tareas app principal:
    ✔ login y registro no se ven porque el estilo del fondo está por encima
    ✔ quitar el fondo animado, no sé por qué se sigue visualizando si el josé lo corrigió (parece que  solo
    en la versión desplegada)
    ✔ disponibilizar registro y login público
    ✔ botón de logout, ¿dónde va según diseño?
    - estilo navbar (tirarlo pa la derecha)

Tareas app cursos:
    - subir un curso completo: básicamente, agregar el registro de 5 capítulos
    - armar el estilo de la vista general de un curso
        - imagen referencial de fondo
        - botón conoce más (que redirige más abajo)
        - botón comenzar (darle estilo al botón play de smart player)
        - información del curso
        - slide de 5 caps
        - elemento ul desplegable para navegar por capítulos
    - armar el estilo de un capítulo
        ✔ botón reproducir (darle estilo al botón play de smart player)
        - botón ver más que redirige más abajo
        - first frame del cap (configurar en smart player)


Apuntes configuración de un capítulo:
- usar XXXX_player.html (sin iframe)
- smart player:
    - servir min.css desde django, editar el aspecto del reproductor desde este archivo
    - servir min.js desde cdn de techsmith
    - servir thumbnail desde hosting creactiva (porque lo necesita el js y no sirven las rutas que ofrece
    django)
    - video: no funciona servido desde django, tiene que ser servido desde afuera, si no, ocurre el error
    de que no funciona la barra de progreso
    - config_xml.js llega desde local, thumbnail servido desde hosting
    - XXXX_config.xml servido desde local, thumbnail y first frame pueden ser servidos desde django, cap
    desde hosting
    - first frame servido desde django

Investigación:
- Problema: ¿cómo hacer para que el link no sea visible de esta manera?
![Alt text](debug/debug-link-video.png)
    - Desarrollo: ¿por quién es realmente visible? Por la persona a la que la app django le da acceso pues.
    - Vulnerabilidad: la persona podría tomar el link del video mirando el código con las herramientas de 
    desarrollador, copiarlo y compartirlo.
    - Solución 1: Agregar una capa de seguridad desde el servidor donde se estén almacenando los videos. El
    tema será que para que django pueda acceder a esos videos también debo agregarle un sistema de auten-
    tificación. Lo bueno, es que eso solucionaría 100% el problema.
    - Solución 2: Buscar una funcionalidad django que permita servir videos ?? pero eso significaría perder
    el smart player y descartar camtasia xd.
    - Respuestas: 
        Me da la impresión de que servir los videos a partir de un iframe soluciona el problema (no, porque
        desde el iframe se puede ver el html que está sirviendo)
        Me da la impresión de que esto es una limitación de SSR (en parte, porque el código del smart player
        se renderiza desde el navegador) -> ¿y si lo integro con react?
        
- Problema: Servir js minificados desde el servidor que requieren un mapeo. No solo pasa con smartplayer,
            también pasa con jquery. Quizás por ahí podría encontrar solución al problema en general.
    - Solución 1: Se puede descargar el archivo map de jqery acá: https://www.cdnpkg.com/jquery/1.11.3
    ¿Servirá servir este archivo? ¿Cómo se puede linkear



Debug estilo:
- menú slider inicial queda fijo a la pantalla y no al carrusel de imágenes
- todos los elementos del fondo animado tienen z-index -1 para solucionar el problema con la "carga" de los
links
- si necesitamos que un mismo elemento tenga un estilo diferente en otro template, hacemos una hoja de
estilos propia para ese template y así no sobreescribimos el estilo original
- hay que arreglar slick del template cursos (el snipper fila.html no está configurado para funcionar
solo, depende todavía de incluir slider-main.html)

