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
✔ registrar formulario Fabián
- que el registro del formulario active una suscripción (acceso al contenido bajo un cierto
periodo de tiempo)

PRÓXIMOS PASOS DE ESTO:
✔ registrar formulario de suscripción organización
* corregir acá, en vez de guardar la última suscirpción a partir de una consulta, utilizar el mismo objeto que ya fue guardado

SIGUIENTE:
✔ crear plantilla detalle suscripción individual
✔ crear la solicitud post con el detalle de la suscripción y almacenarlo en la bbdd

SIGUIENTE:
✔ crear tarea diaria que compruebe vigencia de todas las suscripciones
- lógica cuando el usuario ya tiene una suscripción (pedir suscripciones con esstado = 1 donde el usuario asociado sea el usuario logueado), si tiene una suscripción vigente, enviar mensaje de error y cerrar el proceso. Si no, crear la suscripción.
- lógica para cambiar el estado del perfil del usuario según el tipo de suscripción que compre. Lo mismo cuando caduque la suscripción. Lo mismo cuando el usuario esté inhabilitado ??

SIGUIENTE:
- comenzar integración pasarela de pagos(con eso termina app suscripciones)

SIGUIENTE:
- CURSOS: cursos se pueden ver, si tiene suscripción vigente, enviar capítulo, si no tiene, enviar trailer
- SUSCRIPCIONES: si ya tiene una suscripción vigente, no dejar que se vuelva a suscribir
- PERFIL: crear vista que recoja todos los datos del perfil del usuario
- PERFILES CLAVE: el 000, el 100 y el 010/110. El perfil de miembro no es prioritario todavía (hasta que se produzca la primera suscripción organización
- NOTIFICACIÓN REGISTRO: crear proceso de validación del correo del usuario
- NOTIFICACIÓN SUSCRIPCIÓN: enviar detalles del plan suscrito
- NOTIFICACIÓN SOLICITUD DE SUSCRIPCIÓN ORGANIZACIÓN: enviar detalles de la solicitud de suscripción organización
- FORMULARIO SOLICITUD DE CONTENIDO + NOTIFICACIÓN DE SOLICITUD: crear formulario y notificación por correo


INTEGRACIÓN WEBPAY PLUS
- REGISTRO EMPRESA (CONSEGUIR ID EMPRESA)
- INTEGRACIÓN (MEDIANTE API)
*** FLUJO EXITOSO ***
    - CREAR TRANSACCIÓN (internamente requiere crear una orden de compra)
        - se envía la transacción
        - se recibe un token y la url de redireccionamiento
        - se realiza una petición post a la url, token se envía en la variable 'token_ws'
    *** redirecciona cliente a pasarela de pagos ***
        - el tiempo máximo en el que permanece el formulario de es de 4 minutos
    - CONFIRMAR TRANSACCIÓN
        - si se cumple el tiempo máximo, se reciben las variables 'TBK_ID_SESSION' y 'TBK_ORDEN_COMPRA'
        - si se procesa de forma exitosa, WP retorna al comercio hacia la página de transición, enviando el token de la transacción en la variable 'token_ws'. Se debe implementar la recepción de esta variable mediante el método GET y el redireccionamiento ?? del cliente
        - el sitio del comercio recibe la variable 'token_ws' e invoca el segundo método web ¿? para confirmar y obtener el resultado de la transacción. Este resultado se puee consultr con la variable 'token_ws'.
    - DESPLIEGUE DETALLE VOUCHER
        - transacción exitosa
        - transacción fallida
*** FLUJO SI USUARIO ABORTA ***
    - CREACIÓN DE TRANSACCIÓN
    *** mismo proceso ***
    *** redirecciona a pasarela ***
    - CLIENTE HACE CLIC EN ANULAR
    - WEBPAY RETORNA AL COMERCIO
        - envía pot GET el token 'TBK_TOKEN' y las variables 'TBK_ORDEN_COMPRA' y 'TBK_ID_SESION' (en integración, el redireccionamiento es por POST)
        - el comercio consulta la transacción para validar el estado usando la variable 'TBK_TOKEN' (no es necesario confirmar)
    - DESPLIEGUE PANTALLA QUE EL PAGO NO SE COMPLETÓ
- PROCESO VALIDACIÓN (RELLENAR FORMULARIO DE EVIDENCIAS, RESPUESTA TARDA 24 HORAS HÁBILES)

AMBIENTE DE INTEGRACIÓN
webpay_url: "https://webpay3gint.transbank.cl"
webpay_id: "597055555532"
webpay_secret: "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"

- HEADERS (VAN EN TODAS LAS PETICIONES)
    - Tbk-Api-Key-Id: Código de comercio
        - "597055555532"
    - Tbk-Api-Key-Secret: Llave secreta
        - "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
    - Content-Type: application/json

PARA CREAR TRANSACCIÓN
- PAYLOAD: POST
    - buy_order: str(26). Número único para cada transacción. ID suscripción.
    - session_id: str(61). Identificador de sesión, uso interno comercio. Este valor es devuelto al final de la transacción
    - amount: dec(17). Monto de la transacción, máximo 2 decimales
    - return_url: str(256). URL del comercio a la cual WP redireccionará posterior al proceso de autorización

- RESPUESTA A CREAR TRANSACCIÓN
    - token: str(64). Token de la transacción
    - url: str(255). URL del formulario de pago WP

- PAYLOAD COMMIT TRANSACCIÓN
    - MÉTODO PUT
    - token: el mismo recibido anteriormente. Se envía en la URL no en el body

- RESPUESTA A COMMIT TRANSACCIÓN
    - vci: string. Resultado de la autenticación del dueño de la tarjeta.
    - amount: decimal. Mismo tamaño que el anterior.
    - status: str(64). Estado de la transacción: INITIALIZED, AUTHORIZED, REVERSED, FAILED, NULLIFIED, PARTIALLY_NULLYFIED, CAPTURED.
     - buy_order: str(26). Orden de compra de la tienda, indicado en la creación de la transacción
     - session_id: str(61). Mismo que el anterior.
     - card_detail: Objeto que representa los datos de la tarjeta.
        - card_detail.card_number: 4 últimos números de la tarjeta.
    - accounting_date: fecha de autorización. Largo: 4. Formato MMDD.
    - transaction_date: str(24). Formato ISO 8601, yyyy-mmddTHH:mm:ss.xxx.Z
    - authorization_code: str(6). Código de autorización de la transacción
    - payment_type_code: str. Tipo de pago de la transacción
        - VD = Venta Débito
        - VN = Venta Normal
        - VC = Venta Cuotas
        - SI = 3 cuotas sin interés
        - S2 = 2 cuotas sin interés
        - NC = N Cuotas sin interés
        - VP = Venta Prepago
    response_code: number. Código de respuesta de la autorización. Valores posibles:
        - 0 = Transacción aprobada
        - **Códigos de rechazo
    - installments_amount: number(17). Monto de las cuotas
    - installments_number: number(2). Cantidad de cuotas
    - balance: number(17). Monto restante para un detalle anulado

ESTADO DE LA TRANSACCIÓN: permite recuperar el estado de la transacción y tomar las acciones correspondientes ante un error inesperado. Normalmente, no se aplica.

REVERSAR O ANULAR UN PAGO.

CAPTURAR UNA TRANSACCIÓN. Permite solicitar a WP la captura diferida de una transacción con autorización y sin captura simultánea


PROCESO:
- DETALLE.HTML BOTÓN PAGAR > CREAR TRANSACCIÓN
- WEBPAY.HTML RECIBE URL, PEQUEñO FORMULARIO QUE RECIBE EL TOKEN, SCRIPT JS QUE ENVÍA EL FORMULARIO CON LA ACCIÓN ON_LOAD
- CLIENTE EN LA PLATAFORMA WEBPAY
    - HACER LAS COMPRAS CORRESPONDIENTES CON TODAS LAS TARJETAS
- CONFIRMACION.HTML > CONFIRMAR TRANSACCIÓN


qué son los planes? son precios que nosotros te ofrecemos para que puedas acceder a nuestro contenido.
qué pasa si no puedo pagar el precio de los planes? tenemos descuentos para estudiantes y personas pertenecientes al pueblo mapuche
qué otras opciones tengo para acceder al contenido? si perteneces a una organización, puedes contactarnos para establecer un trato directo con nosotros


APUNTES INTEGRACIÓN WEBPAY:
        # esta persona tiene estados de orden de compra: activo, no activo, ingresado, finalizado, cancelado, en curso
        # En mi caso, me va a servir hacer la validación acá
        # ¿tiene suscripción activa?
        # estados suscripción: activa: 1, finalizada: 2, 


ESTADOS SUSCRIPCIÓN
- 0: CADUCA
- 1: ACTIVA
- 2: EN CURSO
- 2 + session_id = DESTROYED: INTENTO DE PAGO FALLIDO, PERO PROCESO FINALIZADO CORRECTAMENTE


ESTADOS TRANSBANK:
*** PEGAR ***

PARA CONTINUAR:
✔ revisar cómo funciona la view con la validación de la suscripción existente.
✔ revisar en qué rutas será necesario manejar el id del plan desde los parámetros
✔ terminar proceso pago FAILED
✔ no poder pagar otra suscripción cuando ya tengo una vigente
✔ que el usuario no se desloguee cuando vuelva a la página
✔ ver qué otros estados hay que manejar: USUARIO ANULA EL PAGO
✔ actualizar código perfil
✔ realizar pruebas documentación TB (HASTA AHORA, ESTÁN PASANDO)
✔ enviar correos electrónicos por suscripción exitosa
✔ REALIZAR PRUEBAS CON USUARIOS NUEVOS, CON NAVEGADOR INCÓGNITO, CON CHROME
✔ DESPLEGAR VERSIÓN CON WEBPAY
✔ RELLENAR FORMULARIO TB


DEBUG SUSCRIPCIONES:
- QUÉ ES MEJOR? crear un nuevo registro de suscripción (nueva orden de compra) cada vez? o crear 1 registro y actualizar sus datos. Lo primero me va a dejar también registro de las transacciones fallidas. Lo segundo es más limpio el términos de datos. Solo voy a quedarme en la bbdd con las suscripciones caducas. Las suscripciones fallidas también son importantes para tener un respaldo de todas las transacciones que se llevan a cabo. El estado '2' reflejaría una suscripción fallida. El estado_transbank mostrará la razón de por qué falló. La categoría la voy a llamar "en curso", pero si el estado transbank dice "FAILED", entonces significa que la suscripción quedó en curso para nosotros, pero falló para transbank. En consecuencia, el proceso deberá comenzar de nuevo creando un nuevo registro
✔ EL SESSION_ID DEBE SER DESTRUIDO UNA VEZ QUE SE TERMINE DE UTILIZAR PARA NO GENERAR CONFLICTOS: no se destruye, se reemplaza por la palabra "destruido"
✔ MANEJAR EL CASO DONDE SE ANULA LA TRANSACCIÓN (CASO 'VACIO')
✔ CUANDO INTENTA LOGUEAR Y EL USUARIO NO EXISTE, IGUAL CREA LA ORDERN DE COM¿¿PRA DE LA SUSCRIPCIÓN
- MEJORAR EL FORMATO DE LA FECHA, QUITARLE LA HROA Y EL UTC
✔ CORREGIDO, PERO HACER LA PRUEBA: A JOSÉ SE LE DESLOGUEA CUANDO SE CONFIRMA LA TRANSACCIÓN
✔ CORREGIDO, PERO HACER LA PRUEBA: A JOSÉ NO LE RECONOCE LA SUSCRIPCIÓN UNA VEZ QUE ESTÁ HECHA
✔ LA TAREA DE REVISAR LAS SUSCRIPCIONES ACTIVAS ES UNA TAREA AUTOMATIZADA Y TIENE COMO RESULTADO LA ACTUALIZACIÓN DEL CÓDIGO PERFIL. ENTONCES, DEBO ASUMIR QUE SI EL CÓDIGO PERFIL ESTÁ BIEN, ENTONCES TODAS LAS SUSCRIPCIONES SON ACTIVAS. SI LA PERSONA YA TIENE UNA SUSCRIPCIÓN INDIVIDUAL, ENTONCES NO LE VA A DEJAR ENTRAR A LA PANTALLA DE PAGO. EN UNA SEGUNDA INSTANCIA, LE DEBERÍA PREGUNTAR SI QUIERE EXTENDER SU SUSCRIPCIÓN, COSA QUE NO HEMOS DISEñADO TODAVÍA


DESARROLLOS FUTUROS
APP SUSCRIPCIONES:
- views.py > PagarView > post(): FALTARÍA MANEJAR EL CASO CUANDO suscripcion_activa() devuelve una suscripción de organización (numero_usuarios > 1)
- BOTÓN "QUIERO CAMBIAR MI SUSCRIPCIÓN" en PANTALLA_COMPRA, en caso de que la persona quiera cambiar el plan que va a pagar (habiendo elegido otro anteriormente)


APP PERFILES
- botón favoritos necesita lógica


DEBUG EN PRODUCCIÓN:
- suscripciones/services.py: comenté líneas 30-32. Al parecer, la excepción interrumpe el flujo del programa cuando no encuentra el perfil (el usuario todavía no tiene código '100'). Actualización: Así funciona bien.
- cambiar a bbdd postgresql. En postgresql existe el arrayField que almacena listas. Por ahora, en sqlite, lo haré con json
- botón más de los contenidos perdió funcionalidad
- subir tareas cron

ETAPA FINAL DE DETALLES:
✔ recopilar contenidos de capítulos y agregarlos a videos lengua mapuche (lo hará Fabián)


MAñANA:
MAIN
✔ Quitar botón cuenta institución en el login
- Correo registro: mejorar wording
✔ URL sobre nosotros

SUSCRIPCIONES
✔ integrar descuento estudiante/comunero
    - LÓGICA: Si alguien quiere pagar con descuento estudiante.
    1. Si no tiene descuento estudiante, que le despliegue una alerta con la información (básicamente, hazte usuario, si no tienes una cuenta, regístrate, luego, escríbenos a contacto@creactivaanimaciones.cl con asunto "Descuento Creactiva" y adjunta tu certificado de alumno regular de tu institución educativa o tu certificado de pertenencia al pueblo mapuche entregado por CONADI. Nosotros te responderemos a la brevedad y habilitaremos tu descuento)
    2. Administrador valida el documento, checkea campo "descuento creactiva" en bbdd y responde por mail.
    3. Si el usuario tiene check "descuento creactiva" == True, entonces aplicación suscripciones le permite pagar utilizando plan descuento creactiva
    ✔ Banner o bloque explicando descuento creactiva
    ✔ Corrección tarjeta planes: Eliminar contenido innecesario, duración por mes
    ✔ ***	Descripción detalle: ***
    ✔	Tu suscripción termina el día fecha_termino
    ✔	Acceso a todo el contenido educativo
    ✔	Valor
    ✔ *** formatear fechas sin hora ***
    ✔ falta conteo de días
    ✔ *** Pestañas para ver planes estándar y dcto creactiva ***
    ✔ Planes: valor mensual + cantidad de mensual
    ✔ Número de tarjeta quitar, solo monto y tipo plan
✔ Descuento Creactiva: Integrante de la comunidad mapuche/estudiante
✔ Agregar campo boolean para boletas entregadas en perfilsuscripcion
- Datos para correo post suscripción digirido a contacto@creactivaanimaciones.cl : nombre, apellido, correo,. Monto, tipo de plan
✔ Mensaje de fallo o éxito transacción debe durar más
✔ Códigos promocionales: ver lógica
- Debug: Que el form de elegir organización recupere todas las solicitudes
- Formulario solicitudes falta ver tema países, comunas

CURSOS
✔ botones para compartir curso y capítulo no están funcionales
✔ Revisar los headers para volver atrás. Trailer debe volver al curso
✔ *** Etiqueta “próximamente” curso cultura mapuche con fecha de lanzamiento para cada capítulo. Si no tiene fecha de lanzamiento, aparece solo próximamente. ***
*** Botón replay quiebra el reproductor ***
- Dar funcionalidad de play al botón reproducir de abajo
✔ Botón compartir link
- ESTADOS CURSOS ??

PERFILES
✔ permite mostrar datos, pero todavía no permite editarlos: datos perfil y suscripción
- falta mostrar historial de pagos
- falta mostrar cursos suscritos ?? No, porque los planes vigentes son por todo el contenido
Sección: "Actualmente suscrito:"
✔ formatear fechas sin hora
✔ falta conteo de días

SEMANA 17 DE FEBRERO:
SUSCRIPCIONES 
- Datos para correo post suscripción digirido a contacto@creactivaanimaciones.cl : nombre, apellido, correo,. Monto, tipo de plan
✔ Mensaje de fallo o éxito transacción debe durar más
✔ Códigos promocionales: ver lógica
- Debug: Que el form de elegir organización recupere todas las solicitudes
- Formulario solicitudes falta ver tema países, comunas
CURSOS
✔ botones para compartir curso y capítulo no están funcionales
✔ Revisar los headers para volver atrás. Trailer debe volver al curso
✔ *** Etiqueta “próximamente” curso cultura mapuche con fecha de lanzamiento para cada capítulo. Si no tiene fecha de lanzamiento, aparece solo próximamente. ***
*** Botón replay quiebra el reproductor ***
- Dar funcionalidad de play al botón reproducir de abajo
✔ Botón compartir link
- ESTADOS CURSOS ??
- sección principal cursos
PERFILES
- falta mostrar historial de pagos
- falta mostrar cursos suscritos ?? No, porque los planes vigentes son por todo el contenido
DESPLIEGUE
✔ Subir versión de producción
- Migrar a bbdd postgresql
- Conectar a github repo para realizar cambios desde local y automatizar despliegue


CÓDIGOS PROMOCIONALES:
- Permiten al usuario portador a acceder a una suscripción precio descuento creactiva por 1 vez. Puede ser cualquiera de los 3 planes creactiva. Un usuario puede ocupar más de 1 código. Un código solo puede ser usado un determinado número de veces.
    - Da lo mismo si el mismo usuario usó el mismo código dos veces? Por ejemplo, el código dura 2 meses, y uso el mismo código para conseguir 2 meses precio creactiva. Yo creo que sí.
    - Cuando la suscripción pagada con el código caduca, el usuario debe volver a ser estándar (deja de ser plan descuento). Por lo tanto, se debe tener trazabilidad respecto a qué suscripciones fueron pagadas con código promocional. Cuando caduque esa suscripción, el usuario vuelve a ser estándar.
    - El usuario que ingrese ese código, echa a andar un script que reescriba su perfil, haciendo el campo descuento_promocional = True. Esto le permitirá pagar una suscripción precio creactiva hasta que el código caduque.
    - Hay dos formas a través de las que caduca un código: 1) Se ocupó el número de veces para las que fue creado, 2) LLegó la fecha de caducidad.
    - En el fondo, el código promocional interviene al perfil del usuario que lo usa por un cierto periodo de tiempo. Lo hace usuario Creactiva hasta que el código caduque.
    - Por lo tanto, lo más importante, es llevar trazabilidad de los usuarios que ingresan el código. Así, cuando llegue la fecha de caducidad, sabemos qué usuarios deben volver a usuario estándar.
    - Un usuario puede ocupar puede ocupar muchos códigos, y un código puede ser ocupado muchas veces por el mismo usuario (siempre que la fecha de caducidad y la cantidad de usos lo permitan)
    - ¿Un usuario puede tener una suscripción vigente pagada con código promocional y mientras la suscripción sigue vigente perder su estado de usuario creactiva? Debería poder. Y creo que se puede, ya que el tema código promocional es un estado extra del perfil, y no se ve reflejado en el código de acceso 1XX. Además, una vez pagada la suscripción, al usuario no se le pregunta si tiene descuento promocional para ingresar o para ver los cursos. Eso solo se pregunta cuando quiere pagar. Por lo tanto, el tener descuento es una condición independiente de tener suscripción. La duración de la suscripción individual es independiente del precio que se pagó por ella.
    - Entonces, ¿es mejor dejarlos en tablas separadas o en perfilsuscripcion?
    - En la suscripción así como está, se va a ver si el usuario pagó plan con descuento. No se va a ver si el usuario pagó con código promocional. ¿Pero importa eso? Por ahora, no mucho.
    - Lo que sí importa es tener trazabilidad de qué usuario activó un código para saber cuándo caduca. Y tener trazabilidad de cuándo un código deja de ser vigente. Neceistamos una relación entre usuarios y códigos. De muchos a muchos.
    - Si el usuario usó un código, no puede usar el mismo hasta que finalice su suscripción (porque en rigor, ya no puede comprar otra suscripción cuando todavía tiene una vigente). Podrá usar el mismo código siempre y cuando el código siga vigente.
    - Si el usuario ya usó un código, no puede usar otro hasta que caduque (no tiene sentido, ya que el código solo le da check al campo descuento promocional).
    - La promoción creactiva tiene 3 ciclos, dependiendo del tipo de promoción:
        - Estudiante: Caduca el 1 de marzo del año siguiente? (lógica puede escribirse después)
        - Pueblo mapuche: De por vida.
        - Promocional: Código activa 1 pago a precio descuento. Se puede usar el código hasta la fecha establecida o hasta agotar stock. No hace check a descuento creactiva.

    - El check al descuento se logra de dos maneras:
        - Estudiante y pueblo mapuche: Manual mediante validación del administrador.
        - Promocional: Código autoriza 1 pago a precio descuento.

Proceso:
1. Usuario ingresa código en un campo adicional del formulario de plan-individual. Se realiza una consulta a la tabla codigos. Si el código tiene estado 1, entonces se deja pasar a vista detalle de pago.
¿Qué pasa si el usuario vuelve y anula el plann elegido? Vuelve a ingresar el código y vuelve a evaluar si está vigente. Cuando el confirma el pago, entonces se escriben 
2. Formulario escribe el objeto perfil con descuento_promocional = True y objeto suscripción con el  codigo_promocional
3. Se realiza el proceso de pago normal
4. En la vista de respuesta webpay, si el objeto suscripción tiene código promocional distinto de cero, entonces se cambia el objeto perfil descuento_promocional = False. Además, si el código promocional de la suscripción pagada es igual a un código promocional de la tabla, entonces se resta 1 a la cantidad del código y se escribe un registro en la nub de perfiles_codigos.
FIN DEL PROCESO

*** ESTADOS DEL USO DEL CÓDIGO EN TABLA PERFILCODIGO:
- 0: Validado, pero no utilizado
- 1: Utilizado (suscripción registrada exitosamente)

- Por escribir: tarea cron que valide la vigencia de los códigos creados. Actualiza estado = 0 si la fecha de término coincide con la fecha de hoy.
- Lógica que resta contador de usos en tabla
- Lógica que restringa a un mismo usuario utilizar dos veces el mismo código


DEBUG:
- index.js se corta desde la línea 257 hacia abajo cuando lo usamos en el trailer.html y en el reproductor.html porque llama a algunas clases que no existen y se interrumpe la ejecución del script
- mote reestrablecer contraseña
- los prints de views quiebran el programa en producción. La razón tiene que ver con el caracter de espacio indivisible '\xa0'


DETALLES FABIÁN
- textos nosotros desde bbdd
✔ etiqueta próximamente
- Tarea automatizada que quite etiquetas cuando llega la fecha de estreno

SISTEMA ETIQUETAS PROMOCIONALES:
    - ESTADOS PROMOCIONALES:
        - 0: NINGUNO
        - 1: ESTRENO/NUEVO/NOVEDAD
        - 2: PRÓXIMAMENTE
    - Para estado promocional == 2, la etiqueta muestra fecha de lanzamiento
    - Curso también tiene etiqueta promocional, se debe cambiar manual
    - Si el capítulo tiene etiqueta promocional, aunque la persona esté suscrita a la aplicación, le redirige al trailer del capítulo
    - Hay que determinar el número de días durante los cuales el capítulo se considerará en estreno. De momento, se hará manual En el futuro, se puede programar un trabajo cron para eso.


SEMANA 17 DE FEBRERO:

CURSOS
- Tarea automatizada que quite etiquetas cuando llega la fecha de estreno
- *** Botón replay quiebra el reproductor ***
- *** Dar funcionalidad de play al botón reproducir de abajo ***
- Estados cursos ??
- corrección fabián: no mostrar trailer para curso cultura
SUSCRIPCIONES
- *** Debug: Que el form de elegir organización recupere todas las solicitudes ***
- *** Formulario solicitudes falta ver tema países, comunas ***
- Datos para correo post suscripción digirido a contacto@creactivaanimaciones.cl : nombre, apellido, correo,. Monto, tipo de plan
PERFILES
X falta mostrar historial de pagos
- *** falta mostrar cursos suscritos ?? Sección: "Actualmente suscrito:" ***
MAIN
- textos nosotros desde bbdd
- correos automatizados cuando usuarios envíen formularios de contacto y solicitud de suscripción organización
DESPLIEGUE
- Subir versión de producción
- Migrar a bbdd postgresql
- Poner webpay en producción
- Conectar a github repo para realizar cambios desde local y automatizar despliegue
