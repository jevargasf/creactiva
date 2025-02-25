setTimeout(function () {
    // EL PUTO MALDITO BOTÓN PLAY
    btnComenzar = document.querySelector("button.video-click-to-play.ui.play-button-overlay-glyph");
    divAdvertenciaReproductor = document.querySelector("#tscVideoContent > div.message-bar-view-container")
    divAdvertenciaReproductor.style.display = 'none'
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
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
    
},700);
