// --------- INYECCIÓN DE ESTILOS QUE NO SE PUEDEN MANEJAR CON CSS -----------
// Ante cualquier cambio, subir este código al hosting
// básicamente, esto debe ser una función dependiente de DOMContentLoaded
$.getScript( "https://cdn.cloud.techsmith.com/smartplayer/5/latest/techsmith-smart-player.min.js" )
  .done(function( script, textStatus ) {
    console.log( textStatus );
    boton_play = document.getElementsByClassName("video-click-to-play ui play-button-overlay-glyph")
    console.log(boton_play[0])
    boton_play[0].innerHTML = 'Comenzar'
  })
  .fail(function( jqxhr, settings, exception ) {
    //script fail warning if you want it
    console.log("Algo falló")
});

// ---------- FUNCIÓN QUE MANEJA DATA RELEVANTE DEL REPRODUCTOR -------------------
// función que se dispara cuando termina de ver el video:
    // discusión: - ¿le ponemos un botón "desea salir del reproductor"? eso facilitaría el envío de info
    //              al servidor
// El evento beforeunload en window se activa cuando el usuario quiere salir de la página. 
// Si cancelamos el evento, el navegador pregunta si el usuario realmente quiere irse (por ejemplo, 
// tenemos cambios sin guardar).


// atributo del elemento que recoge el segundo de reproducción:
let segReproduccion = document.getElementsByClassName("progress-scrubbar-track")[0].ariaValueNow;

// cómo recupero este dato desde el backend? hasta ahora solo lo tengo aislado en el navegador
// MÉTODO GET


// Estructura función asíncrona que realiza el post, capaz que hasta me sirva para hacer cualquier
// otra solicitud, como un get
async function post(req){
    try{
        const response = await fetch(req);
        const result = await response.json();
        console.log("Success:", result)
    } catch(err){
        console.error("Error:", err)
    }
}
// Lógica: Entonces, debería configurar una URL que sirva el html y otra url que reciba las
// peticiones ?? 
// No, la misma URL del capítulo permite:
//      1. GET: Envía el html con render y en el context envía toda la data del cap + la data
//              de la última reproducción (si es que existe)
//      2. POST: Del lado del front-end, permite "salir/finalizar el reproductor", y desde
//              el backend permite recuperar la última reproducción y mandarla en el body
//              de una solicitud POST. El backend la recibe y la almacena.


// Configuración de la solicitud POST con objeto Request
const req = new Request(
    "http://localhost:8000/capitulo", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            min_video: segReproduccion
        })
    }
);

// Aquí recién hago el llamado a la ejecución de la solicitud POST
// opciones: botón, apretar cerrar? hay algún evento del navegador que sea salir de la página?


const beforeUnloadHandler = (e) => {
    // Recomendado
    e.preventDefault();
    // Esto es para soporte legacy como Chrome < 119
    e.returnValue = true;
    // y aquí iría este código??
    post(req);
};

// la estructura sería:
// manejador del evento (el código que quiero que se ejecute)

// llamado al elemento del DOM que gatilla el beforeUnload. O sea, si aprieta "ese" elemento, entonces
// pide confirmación antes de salir. Yo creo que para nosotros será el botón Comenzar.
const btnReproduccion = document.getElementsByClassName("ui control-button tertiary-button play-control")[0]
// el event listener para el evento
    // por ejemplo, la persona reproduce el video (onclick botón play)
    // si cierra la ventana, escribe otra dirección o vuelve a la página anterior, antes de que salga,
    // el navegador pregunta confirmación. 
    // entonces, llama al manejador del beforeUnload, que recupera la data del elemento del dom
    // especificado

btnReproduccion.addEventListener("click", (e) => {
    if (e.target.value !== "") {
        window.addEventListener("beforeunload", beforeUnloadHandler);
        console.log("Añadido el event listener");
    } else {
        window.removeEventListener("beforeunload", beforeUnloadHandler);
    }
});

// DEBUG: no está agregando el event listener
// DEBUG: hay problemas serios de carga de la página en google chrome normal