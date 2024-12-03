document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
// SLIDER NOTICIAS
$(document).ready(function(){
    $('#slider-noticias').slick({
        arrows: false,
        easing: true,
        pauseOnHover:true,
        infinte: true,
        autoplay: true,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 5,
        responsive: [
        {
            breakpoint: 1460,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 900,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
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

$("#flecha-izquierda-slider-noticias").click(function(){
    $('#slider-noticias').slick('slickPrev');
});

$("#flecha-derecha-slider-noticias").click(function(){
    $('#slider-noticias').slick('slickNext');
});


// SLIDER INICIAL
$(document).ready(function(){
$('#slider-inicial').slick({
arrows: false,
easing: true,
autoplay: true,
infinte: true,
speed: 300,
fade:true,
pauseOnFocus:false,
pauseOnHover:true,
autoplaySpeed: 2500,
});
});

$('#slider-inicial').on('beforeChange', function(event, slick, currentSlide, nextSlide){
if(currentSlide === 0){
document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
}


if(nextSlide === 0){
document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
}

if(nextSlide === 1){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
}

if(nextSlide === 2){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
}

if(nextSlide === 3){
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.add('collapsed');
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
});

$("#slider-inicial-descripcion-2").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(1));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
});

$("#slider-inicial-descripcion-3").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(2));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.add('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.remove('collapsed');
});

$("#slider-inicial-descripcion-4").click(function(e){
e.preventDefault();
$('#slider-inicial').slick('slickGoTo', parseInt(3));
document.querySelector('#slider-inicial-descripcion-1').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-2').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-3').classList.remove('collapsed');
document.querySelector('#slider-inicial-descripcion-4').classList.add('collapsed');
});
