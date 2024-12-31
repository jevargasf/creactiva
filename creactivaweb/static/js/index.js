

document.querySelector('#btn-menu').addEventListener('click', function() {
    document.querySelector('#menudesplegabe').classList.toggle('collapsed');
    document.querySelector('#btn-menu').classList.toggle('collapsed');
});





// SLIDER NOTICIAS
$(document).ready(function(){
    $('#slider-fila').slick({
        arrows: false,
        easing: true,
        pauseOnHover:true,
        infinte: true,
        autoplay: false,
        speed: 500,
        slidesToShow: 7,
        slidesToScroll: 3,
        responsive: [
        {
            breakpoint: 1460,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 5,
            }
        },
        {
            breakpoint: 900,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 760,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                centerMode: true,
                centerPadding: '60px',
            }
        },
        {
            breakpoint: 480,
            settings: {
                centerMode: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '60px',
            }
        }
        ]
    });
});

$("#flecha-izquierda-slider-fila").click(function(){
    $('#slider-fila').slick('slickPrev');
});

$("#flecha-derecha-slider-fila").click(function(){
    $('#slider-fila').slick('slickNext');
});



// SLIDER NOTICIAS
$(document).ready(function(){
    $('#slider-fila-curso').slick({
        arrows: false,
        easing: true,
        pauseOnHover:true,
        infinte: true,
        autoplay: false,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 3,
        responsive: [
        {
            breakpoint: 1460,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 5,
            }
        },
        {
            breakpoint: 900,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 760,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                centerMode: true,
                centerPadding: '60px',
            }
        },
        {
            breakpoint: 480,
            settings: {
                centerMode: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '60px',
            }
        }
        ]
    });
});

$("#flecha-izquierda-slider-fila").click(function(){
    $('#slider-fila').slick('slickPrev');
});

$("#flecha-derecha-slider-fila").click(function(){
    $('#slider-fila').slick('slickNext');
});

// SLIDER INICIAL
$(document).ready(function(){
$('#slider-inicial').slick({
arrows: false,
easing: true,
autoplay: true,
infinte: true,
speed: 500,
fade:true,
pauseOnFocus:false,
pauseOnHover:true,
autoplaySpeed: 5000,
});
});

$('#slider-inicial').on('beforeChange', function(event, slick, currentSlide, nextSlide){
if(currentSlide === 0){
document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
document.querySelector('#btn-spotlight1').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
}


if(nextSlide === 0){
document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.add('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
}

if(nextSlide === 1){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.add('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
}

if(nextSlide === 2){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.add('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
}

if(nextSlide === 3){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.add('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.add('collapsed');
}
});

$("#flecha-izquierda-slider-inicial").click(function(){
$('#slider-inicial').slick('slickPrev');
});

$("#flecha-derecha-slider-inicial").click(function(){
$('#slider-inicial').slick('slickNext');
});

$("#slider-inicial-descripcion-1").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(0));
document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.add('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
});

$("#slider-inicial-descripcion-2").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(1));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.add('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
});

$("#slider-inicial-descripcion-3").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(2));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.add('collapsed');
document.querySelector('#btn-spotlight4').classList.remove('collapsed');
});

$("#slider-inicial-descripcion-4").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(3));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.add('collapsed');
document.querySelector('#btn-spotlight1').classList.remove('collapsed');
document.querySelector('#btn-spotlight2').classList.remove('collapsed');
document.querySelector('#btn-spotlight3').classList.remove('collapsed');
document.querySelector('#btn-spotlight4').classList.add('collapsed');
});





// Botones

document.querySelector('#cerrar-alerta').addEventListener('click', function() {
    document.querySelector('#alerta').classList.add('collapsed');
});
