function alerta(){
    alertaIntermitente = "Hola!!";
    return alertaIntermitente;
}

function actualizar() { 
    if(document.getElementById("alerta").innerHTML){
        document.getElementById("alerta").innerHTML = ""; 
    } else{
        document.getElementById("alerta").innerHTML = alerta(); 
    }
}

setInterval(actualizar,1000); 