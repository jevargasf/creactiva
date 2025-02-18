
window.addEventListener('load', function () {
    $('#transicion').css('opacity', '0');
    $('#transicion')
      .delay(2000)
      .queue( function(next){ 
        $(this).hide(); 
        next(); 
      });
      $('body').css('overflow-y', 'auto');
      document.querySelector('#btn-spotlight1').classList.add('collapsed');
      document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
      document.querySelector('#add-favoritos').classList.add('collapsed');
  })


// Botones

$(document).ready(function(){   
    $(".categoria1").click(function(){
        if ( $(this).attr('class') == 'categoria1') {
            $(this).removeClass('categoria1');
            $(this).addClass('categoria2');
        } else {
            $(this).removeClass('categoria2');
            $(this).addClass('categoria1');
        }
    });
});

$("#btn-menu").click(function(){
    document.querySelector('#menudesplegabe').classList.toggle('collapsed');
    document.querySelector('#btn-menu').classList.toggle('collapsed');
});

// BTN COMPARTIR

$(document).ready(function () {
    btnCompartir = document.getElementById("btn-compartir")
    btnCerrar = document.getElementById("modal-close")
    btnClipboard = document.getElementById("btn-clipboard")
    modalCompartir = document.getElementById("modal-compartir")
    btnCompartir.addEventListener("click", function(){
            modalCompartir.classList.toggle("modal-compartir-open")
    })
    btnCerrar.addEventListener("click", function(){
        modalCompartir.classList.toggle("modal-compartir-open")
})
    btnClipboard.addEventListener("click", function(){
        link = document.getElementById("share-link")
        link.select()
        link.setSelectionRange(0,99999)
        navigator.clipboard.writeText(link.value)
        alert("Texto copiado al portapapeles." + link.value)
    })
});

// BOTON CERRAR ALERTA
$("#cerrar-compartir").click(function(){
    document.querySelector('#modal-compartir').classList.toggle('modal-compartir-open');
});


// BOTON CERRAR ALERTA
$("#cerrarAlerta").click(function(){
    document.querySelector('#alerta').classList.add('collapsed');
});

// BOTONES DE LA LISTA DESPLEGABLE EN CURSOS


    $(".boton-ra1").click(function(){
        document.querySelector('.boton-ra1').classList.toggle('collapsed');
        document.querySelector('.boton-ra2').classList.remove('collapsed');
        document.querySelector('.boton-ra3').classList.remove('collapsed');
        document.querySelector('.boton-ra4').classList.remove('collapsed');
        document.querySelector('.boton-ra5').classList.remove('collapsed');
        document.querySelector('.lista-ra1').classList.toggle('collapsed');
        document.querySelector('.lista-ra2').classList.remove('collapsed');
        document.querySelector('.lista-ra3').classList.remove('collapsed');
        document.querySelector('.lista-ra4').classList.remove('collapsed');
        document.querySelector('.lista-ra5').classList.remove('collapsed');
    });
    
    $(".boton-ra2").click(function(){
        document.querySelector('.boton-ra1').classList.remove('collapsed');
        document.querySelector('.boton-ra2').classList.toggle('collapsed');
        document.querySelector('.boton-ra3').classList.remove('collapsed');
        document.querySelector('.boton-ra4').classList.remove('collapsed');
        document.querySelector('.boton-ra5').classList.remove('collapsed');
        document.querySelector('.lista-ra1').classList.remove('collapsed');
        document.querySelector('.lista-ra2').classList.toggle('collapsed');
        document.querySelector('.lista-ra3').classList.remove('collapsed');
        document.querySelector('.lista-ra4').classList.remove('collapsed');
        document.querySelector('.lista-ra5').classList.remove('collapsed');
    });
            
    $(".boton-ra3").click(function(){
        document.querySelector('.boton-ra1').classList.remove('collapsed');
        document.querySelector('.boton-ra2').classList.remove('collapsed');
        document.querySelector('.boton-ra3').classList.toggle('collapsed');
        document.querySelector('.boton-ra4').classList.remove('collapsed');
        document.querySelector('.boton-ra5').classList.remove('collapsed');
        document.querySelector('.lista-ra1').classList.remove('collapsed');
        document.querySelector('.lista-ra2').classList.remove('collapsed');
        document.querySelector('.lista-ra3').classList.toggle('collapsed');
        document.querySelector('.lista-ra4').classList.remove('collapsed');
        document.querySelector('.lista-ra5').classList.remove('collapsed');
    });

    $(".boton-ra4").click(function(){
        document.querySelector('.boton-ra1').classList.remove('collapsed');
        document.querySelector('.boton-ra2').classList.remove('collapsed');
        document.querySelector('.boton-ra3').classList.remove('collapsed');
        document.querySelector('.boton-ra4').classList.toggle('collapsed');
        document.querySelector('.boton-ra5').classList.remove('collapsed');
        document.querySelector('.lista-ra1').classList.remove('collapsed');
        document.querySelector('.lista-ra2').classList.remove('collapsed');
        document.querySelector('.lista-ra3').classList.remove('collapsed');
        document.querySelector('.lista-ra4').classList.toggle('collapsed');
        document.querySelector('.lista-ra5').classList.remove('collapsed');
    });

    $(".boton-ra5").click(function(){
        document.querySelector('.boton-ra1').classList.remove('collapsed');
        document.querySelector('.boton-ra2').classList.remove('collapsed');
        document.querySelector('.boton-ra3').classList.remove('collapsed');
        document.querySelector('.boton-ra4').classList.remove('collapsed');
        document.querySelector('.boton-ra5').classList.toggle('collapsed');
        document.querySelector('.lista-ra1').classList.remove('collapsed');
        document.querySelector('.lista-ra2').classList.remove('collapsed');
        document.querySelector('.lista-ra3').classList.remove('collapsed');
        document.querySelector('.lista-ra4').classList.remove('collapsed');
        document.querySelector('.lista-ra5').classList.toggle('collapsed');
    });




$(document).ready(function(){   
    $("#add-favoritos").click(function(){
        if ( $(this).attr('class') == 'collapsed') {
            $(this).removeClass('collapsed');
            $("#add-favoritos img").attr("src", "/static/icon/fav-on.svg");
            $("#add-favoritos h1").text("FAVORITO");
        } else {
            $(this).addClass('collapsed');
            $("#add-favoritos img").attr("src", "/static/icon/fav-off.svg");
            $("#add-favoritos h1").text("AÑADIR A FAVORITOS");
        }
    });
});



// Botones scroll

$("#mas-info").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cur-info").offset().top},
        'slow');
});


$("#btn-curso1").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cur-info").offset().top},
        'slow');
});


$("#mas-info-cap").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-info").offset().top},
        'slow');
});

$("#btn-capitulo-out").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-info").offset().top},
        'slow');
});


$("#cap-reproducir").click(function() {
    $('html,body').animate({
        scrollTop: $("html").offset().top},
        'slow');
});




// Animación Título Principal con scroll



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
