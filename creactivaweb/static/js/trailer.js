// if pausa(), entonces despliega info planes
// if termina_video, entonces despliega info planes

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

    });
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
    // TIEMPO DE ESPERA = 5 segundos
},1000);
