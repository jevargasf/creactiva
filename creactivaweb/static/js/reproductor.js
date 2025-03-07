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
        // RECUPERAR MIN DE REPRODUCCIÓN ALMACENADO
        minAlmacenado = document.getElementById("minuto")?.textContent

        // LISTENER DE EVENTO BEFOREUNLOAD ACá
        window.addEventListener("beforeunload", (event) => {
            event.preventDefault();
            event.returnValue = "¿Desea abandonar la reproducción del video?";

            });

        
        // EL BOTÓN MÁS INFO
        // MANIPULACIÓN DEL ESTILO DEL BOTÓN MÁS INFO
        document.querySelector('#btn-capitulo-out').classList.add('collapsed2');
        document.querySelector('#logo_abajo').classList.add('collapsed2');
        document.querySelector('#info-cap-player').classList.add('collapsed2');
        document.querySelector('#logo_capitulo').classList.add('collapsed');
        // RECUPERAR BOTÓN PAUSA
        btnMasInfoCap = document.querySelector("#mas-info-cap")
        // RECUPERAR ELEMENTO VIDEO
        videoElem = document.getElementsByTagName("video")[0]
        // VOLVER AL MIN DE REPRODUCCIÓN ALMACENADO (HAY QUE AFINAR DETALLES DE LA EJECUCIÓN)
        if (parseInt(minAlmacenado) !== NaN){
            videoElem.currentTime = minAlmacenado.replace(/"/g, '')
        }
        // EVENTO CONTROLADOR BOTÓN PAUSA
        btnMasInfoCap?.addEventListener("click", () => {
            videoElem.pause();
        });
        // monitorEvents();

        // RECUPERAR EVENTO 'ended'
        videoElem.addEventListener("ended", () => {
            document.querySelector('#btn-capitulo-out').classList.remove('collapsed2');
            document.querySelector('#logo_abajo').classList.remove('collapsed2');
            document.querySelector('#info-cap-player').classList.remove('collapsed2');
            document.querySelector('#logo_capitulo').classList.remove('collapsed');
            btnReiniciar = document.querySelector("#tscVideoContent > div.before-after-play-controls > div.video-click-to-replay-link > button")
            btnReiniciar.style.zIndex = 1
            btnReiniciar.style.pointerEvents = 'all'
            btnReiniciar.style.backgroundImage = 'none'
            btnReiniciar.addEventListener("click", ()=>{
                document.querySelector('#btn-capitulo-out').classList.add('collapsed2');
                document.querySelector('#logo_abajo').classList.add('collapsed2');
                document.querySelector('#info-cap-player').classList.add('collapsed2');
                document.querySelector('#logo_capitulo').classList.add('collapsed');  
            })
        })
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
                if (videoElem.ended === true){
                    segReproduccion = 0
                } else {
                    segReproduccion = document.querySelector("div.progress-scrubbar-track").ariaValueNow
                }
                user = document.querySelector("#user").innerHTML
                url = window.location.href
                const csrftoken = getCookie('csrftoken');                
                data = {
                    "minuto":segReproduccion,
                    "user":user
                }
                console.log(data)
                // Configuración de la solicitud POST con objeto Request
                envioData(url, csrftoken, JSON.stringify(data));
            }
            });
    });

},2000);
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
// CONSTRUIR EL SETTIMEOUT OBJECT
timeoutObject = {
    ocultarCursor(){
        if (typeof this.timeoutID === "number") {
            this.cancelarTimeout()
        }
        this.timeoutID = setTimeout(function(){
            zonaCursor.style.cursor = "none"
            console.log("timeout seteado")
        }, 1500)
    },
    cancelarTimeout(){
        clearTimeout(this.timeoutID);
        console.log("timeout cancelado")
    }
}

function mouseHandler(e) {
    zonaCursor = document.getElementById("body-trailer")
    zonaCursor.style.cursor = "auto"
    if (zonaCursor.style.cursor != "none") {
        timeoutObject.ocultarCursor();
    }

}

function defaultCursor(){
    document.getElementById("body-trailer").style.cursor = "auto"
    console.log("cursor restaurado")
}

isFullScreen = false;
document.addEventListener("fullscreenchange", () => {

    if (isFullScreen == false) {
        isFullScreen = true
        document.addEventListener("mousemove", mouseHandler)
    } else if (isFullScreen == true) {
        document.removeEventListener("mousemove", mouseHandler)
        timeoutObject.cancelarTimeout();
        defaultCursor();
        isFullScreen = false
    }

});