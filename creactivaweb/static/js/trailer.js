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
        // RECUPERAR BOTÓN PAUSA
        btnMasInfoCap = document.querySelector("#mas-info-cap")
        // RECUPERAR ELEMENTO VIDEO
        videoElem = document.getElementsByTagName("video")[0]
        // EVENTO CONTROLADOR BOTÓN PAUSA
        btnMasInfoCap?.addEventListener("click", () => {
            videoElem.pause();
        });
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
        console.log("entramos en fullscreen")
        isFullScreen = true

        document.addEventListener("mousemove", mouseHandler)
    } else if (isFullScreen == true) {
        document.removeEventListener("mousemove", mouseHandler)
        console.log("saliendo de fs")
        timeoutObject.cancelarTimeout();
        defaultCursor();
        isFullScreen = false
    }

});
