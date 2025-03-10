function updateProgressBar(event) {
    let progressBar = document.getElementById("progressBar");
    let loaded = event.loaded;
    let total = event.total;
    let progress = (loaded / total) * 100;
    progressBar.style.width = progress + "%";
}

window.addEventListener("load", function () {
    let progressBar = document.getElementById("progressBar");
    progressBar.style.width = "100%";
    setTimeout(() => {
        $('#progressContainer').css('opacity', '0');
        $('#transicion').css('opacity', '0');
        $('body').css('overflow-y', 'auto');

        // Después de 2 segundos, ocultar los elementos
        setTimeout(() => {
            $('#progressContainer').hide();
            $('#transicion').hide();
        }, 2000); // Espera 2 segundos antes de ocultarlos
    }, 500); // Delay de 500 ms antes de comenzar el fade
});

document.onreadystatechange = function () {
    let progressBar = document.getElementById("progressBar");
    let progress = (document.readyState === "interactive") ? 50 : (document.readyState === "complete") ? 100 : 0;
    progressBar.style.width = progress + "%";
};


// $(document).ready(function(){   
//     $(".categoria1").click(function(){
//         if ( $(this).attr('class') == 'categoria1') {
//             $(this).removeClass('categoria1');
//             $(this).addClass('categoria2');
//         } else {
//             $(this).removeClass('categoria2');
//             $(this).addClass('categoria1');
//         }
//     });
// });

$("#btn-menu").click(function(event){
    // Previene que el clic en el botón de menú cierre el menú inmediatamente
    event.stopPropagation();
    
    // Alterna la clase 'collapsed' en el menú y en el botón
    document.querySelector('#menudesplegabe').classList.toggle('collapsed');
    document.querySelector('#btn-menu').classList.toggle('collapsed');
});

// Detecta un clic en cualquier parte del documento
$(document).click(function(event){
    // Verifica si el clic fue fuera del botón de menú y del menú desplegable
    if (!$(event.target).closest('#btn-menu, #menudesplegabe').length) {
        // Elimina la clase 'collapsed' si fue un clic fuera de los elementos
        document.querySelector('#menudesplegabe').classList.remove('collapsed');
        document.querySelector('#btn-menu').classList.remove('collapsed');
    }
});

// BOTON CERRAR ALERTA
$("#cerrarAlerta").click(function(){
    document.querySelector('#alerta').classList.add('collapsed');
});


// $(document).ready(function(){   
//     $("#add-favoritos").click(function(){
//         if ( $(this).attr('class') == 'collapsed') {
//             $(this).removeClass('collapsed');
//             $("#add-favoritos img").attr("src", "/static/icon/fav-on.svg");
//             $("#add-favoritos h1").text("FAVORITO");
//         } else {
//             $(this).addClass('collapsed');
//             $("#add-favoritos img").attr("src", "/static/icon/fav-off.svg");
//             $("#add-favoritos h1").text("A�0�5ADIR A FAVORITOS");
//         }
//     });
// });



// Botones scroll

$("#mas-info").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cur-info").offset().top + (-180)},'slow');
});


$("#btn-curso1").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cur-info").offset().top + (-180)},
        'slow');
});


$("#mas-info-cap").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-info").offset().top + (-120)},
        'slow');
});

$("#btn-capitulo-out").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-info").offset().top + (-120)},
        'slow');
});


$("#cap-reproducir").click(function() {
    $('html,body').animate({
        scrollTop: $("html").offset().top},
        'slow');
});




// Animaci��n T��tulo Principal con scroll



   window.onscroll = function() {
    if (scrollY > 100) {
        $('#bannerback').css('opacity', '1');
    } else if (scrollY <= 100) {
        $('#bannerback').css('opacity', '0');
    }     if (scrollY > 150) {
        $('#mas-info').css('opacity', '0');
        $('#mas-info-cap').css('opacity', '0');
    } else if (scrollY <= 150) {
        $('#mas-info').css('opacity', '1');
        $('#mas-info-cap').css('opacity', '1');
    }
};


// BOTONES PLANES

$('#btn-estandar').click(function(){
    $('#btn-descuento').css('opacity', '0.5');
    $('#btn-estandar').css('opacity', '1');
    $('.plan-estandar').css('display', 'inline-block');
    $('.plan-descuento').css('display', 'none');

});

$('#btn-descuento').click(function(){
    $('#btn-estandar').css('opacity', '0.5');
    $('#btn-descuento').css('opacity', '1');
    $('.plan-estandar').css('display', 'none');
    $('.plan-descuento').css('display', 'inline-block');
});



// Funciones Iniciales




$('#id_codigo').attr("placeholder", "Ingresa tu código de descuento");    

