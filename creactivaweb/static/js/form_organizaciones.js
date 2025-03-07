// BOTONES FORM ORGANIZACIONES
selectPais = document.getElementById("pais")
selectRegion = document.getElementById("region")
selectComuna = document.getElementById("comuna")
divSelectRegion = document.getElementById("div-region")
divSelectComuna = document.getElementById("div-comuna")
selectPais.addEventListener("change", ()=>{
    value = selectPais.options[selectPais.selectedIndex].value
    if (value == 'CL'){
        divSelectRegion.classList.remove("form-hide")
    } else if (value != 'CL') {
        divSelectRegion.classList.add("form-hide")
        divSelectComuna.classList.add("form-hide")
    }
})
selectRegion.addEventListener("change", ()=>{
    divSelectComuna.classList.remove("form-hide")
    region = selectRegion.options[selectRegion.selectedIndex].value
    for (i=0; i<selectComuna.options.length; i++) {
        if (selectComuna.options[i].value.slice(0,2) == region){
            selectComuna.options[i].style.display = 'block'
        } else {
            selectComuna.options[i].style.display = 'none'
        }
    }
})