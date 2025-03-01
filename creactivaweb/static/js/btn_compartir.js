// BTN COMPARTIR

$(document).ready(function () {
    btnCompartir = document.getElementById("btn-compartir")
    // btnCerrar = document.getElementById("modal-close")
    btnClipboard = document.getElementById("btn-clipboard")
    modalCompartir = document.getElementById("modal-compartir")
    btnCompartir.addEventListener("click", function(){
            modalCompartir.classList.toggle("modal-compartir-open")
    })
//     btnCerrar.addEventListener("click", function(){
//         modalCompartir.classList.toggle("modal-compartir-open")
// })
    btnClipboard.addEventListener("click", function(){
        link = document.getElementById("share-link")
        link.select()
        link.setSelectionRange(0,99999)
        navigator.clipboard.writeText(link.value)
        alert("Texto copiado al portapapeles." + link.value)
    })
});

// BOTON CERRAR
$("#cerrar-compartir").click(function(){
    document.querySelector('#modal-compartir').classList.toggle('modal-compartir-open');
});