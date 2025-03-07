    // SLIDER FILA 3 (VISTA DETALLE CURSO)
    $(document).ready(function(){
        $('#slider-fila-3').slick({
            arrows: false,
            easing: true,
            pauseOnHover:true,
            infinte: true,
            autoplay: true,
            autoplaySpeed: 5000,
            speed: 500,
            slidesToShow: 4,
            slidesToScroll: 2,
            centerPadding: '62px',
            centerMode: true,
            responsive: [
            {
                breakpoint: 1460,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 2,
                    centerPadding: '62px',
                    centerMode: true,

                }
            },
            {
                breakpoint: 900,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    centerMode: true,
                    centerPadding: '60px',
                }
            },
            {
                breakpoint: 760,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    centerMode: true,
                    centerPadding: '60px',
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    centerMode: true,
                    centerPadding: '25px',
                }
            }
            ]
        });
    });
    
    $("#flecha-izquierda-slider-fila-3").click(function(){
        $('#slider-fila-3').slick('slickPrev');
    });
    
    $("#flecha-derecha-slider-fila-3").click(function(){
        $('#slider-fila-3').slick('slickNext');
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


