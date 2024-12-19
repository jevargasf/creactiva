# creactiva
Repositorio aplicación web Creactiva Animaciones

Enviando un saludo desde mi máquina local

admin
creactiva

próximos pasos:
- hacer un html específico que funcione como máscara de reproducción
- techsmith-smart-player.min.css es suficiente para manejar los estilos y se puede servir desde 
la app web (no así el js)
- confirmar que se puede servir el video desde app django
- para desarrollo: servir desde hosting con un link externo (y así no )
    - alternativa: que josé tenga su propia carpeta con los archivos y agregarlos BIEN al gitignore
    para que no se suban
- para probar seguridad: servir desde local
- en producción: servir desde dentro de app django (similar a pruebas desde local)
- hacer html para servir videos públicos (no hay necesidad de smart player)
- insertar c1e1_player en base.html
- servir thumbnail desde local
- recopilar los archivos que requiere cada vídeo para funcionar en el servidor:
    - thumbnail
    - xml(previamente configurado para servirse desde django)
    - first frame
    - mp4
    - ?? no sé qué más


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
    - Respuestas: 
        Me da la impresión de que servir los videos a partir de un iframe soluciona el problema.
        Me da la impresión de que esto es una limitación de SSR
        