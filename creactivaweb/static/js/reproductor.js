setTimeout(function () {
    // MENSAJE A CONSOLA
    console.log("muestra el tiempo");

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
        // BOTÓN PAUSA
        btnMasInfoCap = document.querySelector("#mas-info-cap")
        videoElem = document.getElementsByTagName("video")[0]
        btnMasInfoCap?.addEventListener("click", () => {
            videoElem.pause();
        });
        console.log("llegó hasta acá")
    });
    // CÓDIGO DEL ALERT
    $(document).ready(function () {
        $('#transicion').css('opacity', '0');
    });
    // TIEMPO DE ESPERA = 5 segundos
},500);


// ------ CÓDIGO SIN USAR QUE NO QUIERO BORRAR TODAVÍA ---------

        // if (e.target.value !== "") {
        //     window.addEventListener("beforeunload", beforeUnloadHandler);
        //     console.log("Añadido el event listener");
        // } else {
        //     window.removeEventListener("beforeunload", beforeUnloadHandler);
        //     console.log("Quitado el event listener");
        // }
// document.onreadystatechange = function() {
//     if (document.readyState === "complete") {
//         console.log(document.getElementsByTagName("button"))
//       console.log("Page is loaded completely!");
//       screenControl = document.querySelector("button.video-click-to-play.ui.play-button-overlay-glyph");
//       console.log(screenControl);
//     }
//   };

// document.addEventListener("DOMContentLoaded", function(e) {
//     const screenControl = document.querySelector("button.video-click-to-play.ui.play-button-overlay-glyph")
//     console.log(screenControl)
//     screenControl?.addEventListener("click", () => {
//         console.log("Llega acá")
//         document.getElementById("btn-capitulo-out").style.visibility = "hidden"
//         // if (e.target.value !== "") {
//         //     window.addEventListener("beforeunload", beforeUnloadHandler);
//         //     console.log("Añadido el event listener");
//         // } else {
//         //     window.removeEventListener("beforeunload", beforeUnloadHandler);
//         //     console.log("Quitado el event listener");
//         // }
//     });
//     console.log("Sí llegó")
//   });

// $( document ).ready(function() {
//     console.log("script loaded")
//   });

// ---------- FUNCIÓN QUE MANEJA DATA RELEVANTE DEL REPRODUCTOR -------------------
// función que se dispara cuando termina de ver el video:
    // discusión: - ¿le ponemos un botón "desea salir del reproductor"? eso facilitaría el envío de info
    //              al servidor
// El evento beforeunload en window se activa cuando el usuario quiere salir de la página. 
// Si cancelamos el evento, el navegador pregunta si el usuario realmente quiere irse (por ejemplo, 
// tenemos cambios sin guardar).


// atributo del elemento que recoge el segundo de reproducción:
// let segReproduccion = document.getElementsByClassName("progress-scrubbar-track")[0].ariaValueNow;

// cómo recupero este dato desde el backend? hasta ahora solo lo tengo aislado en el navegador
// MÉTODO GET


// Estructura función asíncrona que realiza el post, capaz que hasta me sirva para hacer cualquier
// otra solicitud, como un get
// async function post(req){
//     try{
//         const response = await fetch(req);
//         const result = await response.json();
//         console.log("Success:", result)
//     } catch(err){
//         console.error("Error:", err)
//     }
// }
// Lógica: Entonces, debería configurar una URL que sirva el html y otra url que reciba las
// peticiones ?? 
// No, la misma URL del capítulo permite:
//      1. GET: Envía el html con render y en el context envía toda la data del cap + la data
//              de la última reproducción (si es que existe)
//      2. POST: Del lado del front-end, permite "salir/finalizar el reproductor", y desde
//              el backend permite recuperar la última reproducción y mandarla en el body
//              de una solicitud POST. El backend la recibe y la almacena.


// Configuración de la solicitud POST con objeto Request
// const req = new Request(
//     "http://localhost:8000/capitulo", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//             min_video: segReproduccion
//         })
//     }
// );

// Aquí recién hago el llamado a la ejecución de la solicitud POST
// opciones: botón, apretar cerrar? hay algún evento del navegador que sea salir de la página?


// const beforeUnloadHandler = (e) => {
//     // Recomendado
//     e.preventDefault();
//     // Esto es para soporte legacy como Chrome < 119
//     e.returnValue = true;
//     // y aquí iría este código??
    
//     post(req);
// };

// la estructura sería:
// manejador del evento (el código que quiero que se ejecute)

// llamado al elemento del DOM que gatilla el beforeUnload. O sea, si aprieta "ese" elemento, entonces
// pide confirmación antes de salir. Yo creo que para nosotros será el botón Comenzar.

// console.log(btnReproduccion, btnMasInfo)
// el event listener para el evento
    // por ejemplo, la persona reproduce el video (onclick botón play)
    // si cierra la ventana, escribe otra dirección o vuelve a la página anterior, antes de que salga,
    // el navegador pregunta confirmación. 
    // entonces, llama al manejador del beforeUnload, que recupera la data del elemento del dom
    // especificado



// DEBUG: no está agregando el event listener
// DEBUG: hay problemas serios de carga de la página en google chrome normal
// window.onbeforeunload = function() {
//     console.log("Sí")
//     return "Hay cambios sin guardar. ¿Salir ahora?";
//   };

// window.addEventListener("beforeunload", (event) => {
// // funciona, lo mismo que si devolviera desde window.onbeforeunload
// event.returnValue = "Hsy cambios sin grabar. ¿Abandonar ahora?";
// });
