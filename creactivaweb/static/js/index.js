
window.addEventListener('load', function () {
      $('body').css('overflow-y', 'auto');
      document.querySelector('#btn-spotlight1').classList.add('collapsed');
      document.querySelector('#slider-inicial-descripcion-1').classList.add('collapsed');
    //   document.querySelector('#add-favoritos').classList.add('collapsed');
  })

// LOCAL STORAGE
// flag = localStorage.getItem("alert")
// if (localStorage.flag === "true"){
//   console.log("no hago nada")
// } else if (flag === null){
//   document.querySelector("#publicidad").innerHTML += 
//   `<div id="alerta" class="alert" role="alert">
//   <div>
//   <strong>USTED HA INGRESADO POR PRIMERA VEZ</strong>
//   <p>haz click para continuar</p>
//   <button id="cerrarAlerta"  type="button"><img src="" alt=""></button>
//   </div>
//   </div>`
//   localStorage.setItem("flag", "true")
// }