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
        // RECUPERAR EVENTO 'ended'
        videoElem.addEventListener("ended", () => {
            console.log("EL VIDEO HA FINALIZADO")
            // DESPLIEGO UN BOTÓN
            document.querySelector('#btn-capitulo-out').classList.remove('collapsed2');
            document.querySelector('#logo_abajo').classList.remove('collapsed2');
            document.querySelector('#info-cap-player').classList.remove('collapsed2');
            document.querySelector('#logo_capitulo').classList.remove('collapsed');
            divBtnComenzar = document.querySelector("div.video-click-to-play-link")
            // #tscVideoContent > div.before-after-play-controls > div.video-click-to-play-link
            divBtnComenzar.style.display = "block";
            divBtnComenzar.addEventListener("click", () => {
                videoElem.currentTime = 0;
                videoElem.play()
            })
        })

    });
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
    // TIEMPO DE ESPERA = 5 segundos
},1000);
