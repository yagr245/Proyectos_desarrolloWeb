function actual(){
    horaActual = new Date(); 
    mireloj = horaActual.toLocaleTimeString();
    return mireloj; 
}

function actualizar() { 
    document.getElementById("hora").innerHTML = actual(); 
}

setInterval(actualizar,1000); 