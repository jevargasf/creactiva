

async function envioData(url, csrftoken, data){
    try{
        const req = await fetch(url, {
            method: 'POST',
            mode: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
              },
            body: data
        })
        .then(res => console.log(res.status))
        console.log(req)
        //navigator.sendBeacon("/log", analyticsData);
    } catch(e) {
        console.log('Ocurrió un error', e)
    }
    
}


setTimeout(function () {
    // EL PUTO MALDITO BOTÓN PLAY
    btnComenzar = document.querySelector("button.video-click-to-play.ui.play-button-overlay-glyph");

    // EVENTO CLICK AGREGADO AL PUTO MALDITO
    btnComenzar?.addEventListener("click", () => {
        // EL BOTÓN MÁS INFO
        // MANIPULACIÓN DEL ESTILO DEL BOTÓN MÁS INFO
        document.querySelector('#btn-capitulo-out').classList.add('collapsed2');
        document.querySelector('#logo_abajo').classList.add('collapsed2');
        document.querySelector('#info-cap-player').classList.add('collapsed2');
        document.querySelector('#logo_capitulo').classList.add('collapsed');
        // BOTÓN PAUSA
        btnMasInfoCap = document.querySelector("#mas-info-cap")
        videoElem = document.getElementsByTagName("video")[0]
        btnMasInfoCap?.addEventListener("click", () => {
            videoElem.pause();
        });

        // A la función se le provee del nombre de la cookie que se necesite
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Acá comprueba si la cookie tiene el nombre que se requiere
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        document.addEventListener("visibilitychange", function logData() {
            console.log("Preparando la data...")

            if (document.visibilityState === "hidden") {
                console.log("Enviando data...")
                videoElem = document.getElementsByTagName("video")[0]
                videoElem.pause();
                segReproduccion = document.querySelector("div.progress-scrubbar-track").ariaValueNow
                url = window.location.href
                const csrftoken = getCookie('csrftoken');                
                data = JSON.stringify(segReproduccion)
                console.log(data)
                // Configuración de la solicitud POST con objeto Request
                envioData(url, csrftoken, data);
            }
            });
    });
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
    // TIEMPO DE ESPERA = 5 segundos
},500);



// LISTENER DE EVENTO BEFOREUNLOAD ACá
window.addEventListener("beforeunload", (event) => {
    event.preventDefault();
    event.returnValue = "¿Desea abandonar la reproducción del video?";

    });


// ---------- FUNCIÓN QUE MANEJA DATA RELEVANTE DEL REPRODUCTOR -------------------
// función que se dispara cuando termina de ver el video:
    // discusión: - ¿le ponemos un botón "desea salir del reproductor"? eso facilitaría el envío de info
    //              al servidor
// El evento beforeunload en window se activa cuando el usuario quiere salir de la página. 
// Si cancelamos el evento, el navegador pregunta si el usuario realmente quiere irse (por ejemplo, 
// tenemos cambios sin guardar).


// atributo del elemento que recoge el segundo de reproducción:
// let segReproduccion = document.getElementsByClassName("progress-scrubbar-track")[0].ariaValueNow;

// cómo recupero este dato desde el backend? hasta ahora solo lo tengo aislado en el navegador
// MÉTODO GET


// Estructura función asíncrona que realiza el post, capaz que hasta me sirva para hacer cualquier
// otra solicitud, como un get
// async function post(req){
//     try{
//         const response = await fetch(req);
//         const result = await response.json();
//         console.log("Success:", result)
//     } catch(err){
//         console.error("Error:", err)
//     }
// }
// Lógica: Entonces, debería configurar una URL que sirva el html y otra url que reciba las
// peticiones ?? 
// No, la misma URL del capítulo permite:
//      1. GET: Envía el html con render y en el context envía toda la data del cap + la data
//              de la última reproducción (si es que existe)
//      2. POST: Del lado del front-end, permite "salir/finalizar el reproductor", y desde
//              el backend permite recuperar la última reproducción y mandarla en el body
//              de una solicitud POST. El backend la recibe y la almacena.


// la estructura sería:
// manejador del evento (el código que quiero que se ejecute)

// llamado al elemento del DOM que gatilla el beforeUnload. O sea, si aprieta "ese" elemento, entonces
// pide confirmación antes de salir. Yo creo que para nosotros será el botón Comenzar.

// console.log(btnReproduccion, btnMasInfo)
// el event listener para el evento
    // por ejemplo, la persona reproduce el video (onclick botón play)
    // si cierra la ventana, escribe otra dirección o vuelve a la página anterior, antes de que salga,
    // el navegador pregunta confirmación. 
    // entonces, llama al manejador del beforeUnload, que recupera la data del elemento del dom
    // especificado