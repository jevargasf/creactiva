// Ante cualquier cambio, subir este código al hosting
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

