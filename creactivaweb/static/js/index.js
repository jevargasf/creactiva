
window.addEventListener('load', function () {
    $('#transicion').css('opacity', '0');
    $('#transicion')
      .delay(2000)
      .queue( function(next){ 
        $(this).hide(); 
        next(); 
      });
      $('body').css('overflow-y', 'auto');

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

// $("#busqueda").click(function(){
//     document.querySelector('#spotlight').classList.add('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.add('collapsed');
//     document.querySelector('#buscador').classList.add('collapsed');
//     document.querySelector('#fila').classList.add('collapsed');
//     document.querySelector('#slider-fila').classList.add('collapsed');
// });


// 
// $("#fila").click(function(){
//     document.querySelector('#spotlight').classList.add('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.add('collapsed');
//     document.querySelector('#buscador').classList.add('collapsed');
//     document.querySelector('#fila').classList.add('collapsed');
//     document.querySelector('#slider-fila').classList.add('collapsed');
// });
// 
// $("#btn-busqueda").click(function(){
//     document.querySelector('#spotlight').classList.add('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.add('collapsed');
//     document.querySelector('#buscador').classList.add('collapsed');
//     document.querySelector('#fila').classList.add('collapsed');
//     document.querySelector('#slider-fila').classList.add('collapsed');
// });
// 
// 
// $("#categorias").click(function(){
//     document.querySelector('#spotlight').classList.add('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.add('collapsed');
//     document.querySelector('#buscador').classList.add('collapsed');
//     document.querySelector('#fila').classList.add('collapsed');
//     document.querySelector('#slider-fila').classList.add('collapsed');
// });
// // 
// 
// $("#spotlight").click(function(){
//     document.querySelector('#spotlight').classList.remove('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.remove('collapsed');
//     document.querySelector('#buscador').classList.remove('collapsed');
//     document.querySelector('#fila').classList.remove('collapsed');
//     document.querySelector('#slider-fila').classList.remove('collapsed');
// 
// });
// 
// 
// $("#logo").click(function(){
//     document.querySelector('#spotlight').classList.remove('collapsed');
//     document.querySelector('#slider-inicial-nav').classList.remove('collapsed');
//     document.querySelector('#buscador').classList.remove('collapsed');
//     document.querySelector('#fila').classList.remove('collapsed');
// });
// 

// BOTON CERRAR ALERTA
$("#cerrarAlerta").click(function(){
    document.querySelector('#alerta').classList.add('collapsed');
});

// BOTON + INFO CURSO
//$("#mas-info").click(function(){
//    document.querySelector('#contenido-curso1').classList.add('collapsed');
//    document.querySelector('#curso-info1').classList.add('collapsed');
//    document.querySelector('#mas-info').classList.add('collapsed');
//    document.querySelector('#info-cap-full').classList.add('collapsed');
//});

// BOTON VOLVER CURSO INFO
//$("#img-curso-cont").click(function(){
//    document.querySelector('#contenido-curso1').classList.remove('collapsed');
//    document.querySelector('#curso-info1').classList.remove('collapsed');
//    document.querySelector('#info-cap-full').classList.remove('collapsed');
//    document.querySelector('#mas-info').classList.remove('collapsed');
//});

// BOTON + INFO CAP
//$("#mas-info-cap").click(function(){
//    document.querySelector('#tscVideoContent').classList.add('collapsed');
//    document.querySelector('#mas-info-cap').classList.add('collapsed');
//    document.querySelector('.play-button-overlay-glyph').classList.add('collapsed');
//    document.querySelector('#btn-capitulo-out').classList.add('collapsed');
//    document.querySelector('#logo_abajo').classList.add('collapsed');
//    document.querySelector('#cap-banner-top').classList.add('collapsed');
//    document.querySelector('#info-cap-player').classList.add('collapsed');
//    document.querySelector('#logo_capitulo').classList.add('collapsed2');
//    document.querySelector('#info-cap-full').classList.add('collapsed');
//});

// BOTON MAS INFO CAP SOBRE VIDEO
//$("#btn-capitulo-out").click(function(){
//    document.querySelector('#tscVideoContent').classList.add('collapsed');
//    document.querySelector('#mas-info-cap').classList.add('collapsed');
//    document.querySelector('.play-button-overlay-glyph').classList.add('collapsed');
//    document.querySelector('#btn-capitulo-out').classList.add('collapsed');
//    document.querySelector('#logo_abajo').classList.add('collapsed');
//    document.querySelector('#cap-banner-top').classList.add('collapsed');
//    document.querySelector('#info-cap-player').classList.add('collapsed');
//    document.querySelector('#logo_capitulo').classList.add('collapsed2');
//    document.querySelector('#info-cap-full').classList.add('collapsed');
//});

//// BOTON REGRESO AL CAP DESDE INFOFULL
//$("#tscVideoContent").click(function(){
//    document.querySelector('#tscVideoContent').classList.remove('collapsed');
//    document.querySelector('#mas-info-cap').classList.remove('collapsed');
//    document.querySelector('#btn-capitulo-out').classList.remove('collapsed');
//    document.querySelector('#logo_abajo').classList.remove('collapsed');
//    document.querySelector('#cap-banner-top').classList.remove('collapsed');
//    document.querySelector('#info-cap-player').classList.remove('collapsed');
//    document.querySelector('#logo_capitulo').classList.remove('collapsed2');
//    document.querySelector('#info-cap-full').classList.remove('collapsed');
//});
//
//// BOTON REPRODUCIR DE LA INFO DEL CAP
//$("#cap-reproducir").click(function(){
//    document.querySelector('#tscVideoContent').classList.remove('collapsed');
//    document.querySelector('#mas-info-cap').classList.remove('collapsed');
//    document.querySelector('#btn-capitulo-out').classList.remove('collapsed');
//    document.querySelector('#logo_abajo').classList.remove('collapsed');
//    document.querySelector('#cap-banner-top').classList.remove('collapsed');
//    document.querySelector('#info-cap-player').classList.remove('collapsed');
//    document.querySelector('#logo_capitulo').classList.remove('collapsed2');
//    document.querySelector('#info-cap-full').classList.remove('collapsed');
//});
//
//// BOTONES CURSO MAS INFO
//$("#btn-curso1").click(function(){
//    document.querySelector('#contenido-curso1').classList.add('collapsed');
//    document.querySelector('#curso-info1').classList.add('collapsed');
//    document.querySelector('#mas-info').classList.add('collapsed');
//    document.querySelector('#info-cap-full').classList.add('collapsed');
//});
//
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

// Funciones Iniciales

$(document).ready(function () {
    document.querySelector('#btn-spotlight1').classList.add('collapsed');
    document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
    document.querySelector('#add-favoritos').classList.add('collapsed');


});

// Botones scroll

$("#mas-info").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-full").offset().top},
        'slow');
});


$("#btn-curso1").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-full").offset().top},
        'slow');
});


$("#mas-info-cap").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-full").offset().top},
        'slow');
});

$("#btn-capitulo-out").click(function() {
    $('html,body').animate({
        scrollTop: $("#info-cap-full").offset().top},
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

$('#id_codigo').attr("placeholder", "Ingresa tu código de descuento");    
