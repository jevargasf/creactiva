# creactiva
Repositorio aplicación web Creactiva Animaciones

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
    Tareas app cursos:
        - armar el estilo de la vista general de un curso
            - botón conoce más (que redirige más abajo)
            - elemento ul desplegable para navegar por capítulos
        - armar el estilo de un capítulo
            - botón ver más que redirige más abajo
        - que josé suba todos los caps de los dos cursos y yo los linkeo a la rama dev

    ✔ ejecución asíncrona del script reproductor.js que corrige el estilo del smart player

App principal, control de permisos:
    ✔ sección login/registro
    ✔ primera restricción de permisos: invitado/usuario (usuarios no logueados no pueden acceder al contenido)
    - segunda restricción de permisos: usuario/cliente
    - registrar formulario contacto en bbdd (aprovechar el vuelo con formulario plan organización)

App suscripciones:
    ✔ templates básicos: eleccion_plan.html, plan_individual.html, plan_organizacion.html
    ✔ elementos de cada template básico.
    - registrar formularios: plan organización.
        - variables nuevas:
            1. Tipo de organización (empresa (org privada con fines de lucro), osc, fiscal)
            2. A qué se dedica (clasificación por rama de actividad)
            3. Tipos que se escapan: corporaciones municipales(dependen de la municipalidad, no son enteramente privadas), mutuales(controladas por el Estado), cooperativas(pueden repartir excedentes entre sus socios), asociaciones de propietarios(no son plenamente voluntarias), universidades estatales(pj de derecho público), asociaciones indígenas(pueden realizar actividades productivas), clubes deportivos profesionales(muchos son sociedades anónimas), asociaciones de culto religioso(no hay información exhaustiva para clasificarlas).
    Prueba planes:
        - ususario: id = 101 no se le muestra nada//  Javier
        - usuario: id = 111 se le muestra el contenido // José

App usuarios:
    - templates básicos: panel_organizacion.html, panel_individual.html, panel_admin.html
    - ver si queda mejor la estructura de 3 html distintos o si es mejor 1 solo html con bloques
    if elif según tipo de usuario.


Apuntes configuración de un capítulo:
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

Reemplazo de cap:
    - en el proyecto: solo copié los xml y xml.js a las carpetas correspondientes
    - en el hosting: subir mp4 a carpeta static/videos > collecstatic > reiniar app > copiar link en reproductor.html
    - no hay thumbnails ahora, así que no hay que manipular los archivos
    - bugs reportados con el reemplazo del cap?

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


DEBUG APP CAPÍTULOS:
    - terminar la función que recupera el momento de reproducción T_T.
    - botón comenzar: si el curso no está iniciado, entonces partir desde el capítulo 1. Si el curso está
    iniciado, entonces partir desde el último punto (y cambiar el texto a "continuar").
    - botón comenzar: envía al backend la señal de que el curso fue iniciado.
    - script reproductor: EL TIEMPO DE CARGA ÓPTIMO ESTÁ ENTRE 500ms y 5000ms en la primera carga.

DEBUG NAVEGACIÓN: RESUELTO
    SOLUCIÓN: manejo de diferentes casos con bloques if elif en snippet
    ✔ hay que ver bien dónde nos va a llevar la pestaña "capítulos" del navbar. Hasta ahora lleva al index.
    ✔ implementar botón "back" sin necesidad de repetir el snippet para cada template

DEBUG REPRODUCTOR:
    - 07/01. Se reporta falla en la carga del video servido desde hosting. Ocurrió después de reemplazar el video anterior por una nueva versión. Se reemplazaron los archivos xml y xml.js en el proyecto, se agregaron sin modificaciones.
    - 10/01. Se reporta falla en la carga del video después de implementar recarga en el minuto de visualización almacenado anteriormente. Atento al debug de la renderización del video en el minuto de visualización almacenado.

Proceso:
    - Primero, escribir el formulario de solicitud
    - Luego, revisarlo, aprobarlo y contactar organización
    - Finalmente, la suscripción organización es válida cuando el administrador la registra en otro formulario, el definitivo. Podría implementar autollenado de algunos datos en base a la info entregada en el primero. Este es el registro que el backend debe almacenar como la suscripción de organización.


Mejoras a futuro:
- El administrador tendrá la necesidad de mejorar el análisis de las organizaciones que se suscriben a su contenido. A futuro puede implementar nuevas categorías como "¿a qué se dedican?", con el fin de capturar la categoría de actividad específica de la organización. Esto permitiría comprender mejor el "público organizaciones" al que se está llegando, con el fin de buscar estrategias para ampliarlo o para elaborar productos dirigidos a ellos.
- El registro de visualizaciones genera muchos datos que pierden su utilidad rápidamente. Esto es un espacio de memoria de la bbdd que en un futuro podría causar un problema. Para solucionarlo, se puede escribir un procedimiento almacenado que limpie la bbdd todos los días a las 5AM y solo deje la última visualización. También, se podría estudiar manejar estas visualizaciones intermedias en memoria y solo escribir la bbdd con "ese" dato que a las 5AM se deja. MMmm. Hay que seguir estudiándolo.

ACTUALMENTE TRABAJANDO:
- app suscripciones/formulario solicitud organizaciones/categorías organizaciones

PRÓXIMOS PASOS:
- HTML cursos
- Agregar contenidos curso a backend
- Agregar curso a favoritos
- Bloquear barra de avance en primera reproducción
- Nuevos botones: play grande, reiniciar capítulo
- Comportamiento reproductor: al finalizar el capítulo, mostrar el índice
- Redireccionamiento registrar está roto
- Crear usuario debe incluir registro de perfil básico
- Si no hay materiales, que no se muestre recursos adicionales
- Debug primera carga reproductor
- Tarjeta estudiarntes y proceso de validación estudiante
- Corregir tilde en desplegable del form organizaciones
- Tarjetas planes editables desde backend

APP SUSCRIPCIONES:
1) INDIVIDUAL
- crear modelo bbdd planes
- registrar planes en bbdd y servirlos al front
- HTML detalle
- Integrar webpay
- Que la compra (envío del formulario detalle) active una suscripción bajo un cierto periodo de tiempo

2) ORGANIZACIÓN
- registrar formulario Fabián
- que el registro del formulario active una suscripción (acceso al contenido bajo un cierto
periodo de tiempo)

PRÓXIMOS PASOS DE ESTO:
- diseñar formularios

        # Falta: linkear con cursos a los que se dará acceso, linkear con rep organización
        # Rep org: se recupera de una lista renderizada?? o se solicita en un input y se hace la
        # búsqueda en la bbdd. Nah, de una lista nomás de los rep org.
        # Luego: los cursos se recuperan tb de una lista renderizada
        # Bueno, creo que debo usar multi-forms


        # Quizás no es necesario porque voy a pedir los cursos y el titular a través de una lista
        # Y cuando mande el formulario, escribo los modelos en el view
        # Y los campos de suscripción están listos
