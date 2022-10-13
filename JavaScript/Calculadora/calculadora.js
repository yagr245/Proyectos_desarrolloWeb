var numero1 = 0;
var numero2 = 0;
var operacion = 0;
var simbolo = 0;
var resultado = 0;

function calculadora(dato){
    if(document.getElementById("valor2").innerHTML != 0){
        document.getElementById("valor2").innerHTML = document.getElementById("valor2").innerHTML + dato;
        numero2 = parseFloat(dato) 
    } else{
        numero1 += parseFloat(dato);
        document.getElementById("valor2").innerHTML = numero1;
    }
}

function operador(signo){
    if(signo == '+' && resultado == 0){
        operacion = numero1;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 1;
    }  else if(signo == '+' && resultado != 0){
        operacion = resultado;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 1;
    }
    if(signo == '-' && resultado == 0){
        operacion = numero1;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 2;
    } else if(signo == '-' && resultado != 0){
        operacion = resultado;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 2;
    }
    if(signo == '*' && resultado == 0){
        operacion = numero1;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 3;
    } else if(signo == '*' && resultado != 0){
        operacion = resultado;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 3;
    }
    if(signo == '/' && resultado == 0){
        operacion = numero1;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 4;
    } else if(signo == '/' && resultado != 0){
        operacion = resultado;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 4;
    }
    if(signo == '%' && resultado == 0){
        operacion = numero1;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 5;
    } else if(signo == '%' && resultado != 0){
        operacion = resultado;
        document.getElementById("valor2").innerHTML += signo;
        simbolo = 5;
    }
}

function equal(igual){
    if(igual == '=' && simbolo == 1){
        resultado = parseFloat(operacion) + parseFloat(numero2);
        document.getElementById("valor2").innerHTML = resultado;
    } else if(igual == '=' && simbolo == 2){
        resultado = parseFloat(operacion) - parseFloat(numero2);
        document.getElementById("valor2").innerHTML = resultado;
    } else if(igual == '=' && simbolo == 3){
        resultado = parseFloat(operacion) * parseFloat(numero2);
        document.getElementById("valor2").innerHTML = resultado;
    } else if(igual == '=' && simbolo == 4){
        resultado = parseFloat(operacion) / parseFloat(numero2);
        document.getElementById("valor2").innerHTML = resultado;
    } else if(igual == '=' && simbolo == 5){
        resultado = (parseFloat(operacion) * parseFloat(numero2)) / 100;
        document.getElementById("valor2").innerHTML = resultado;
    }
}

function eraser(){
    document.getElementById("valor2").innerHTML = 0;
    numero1 = 0;
    numero2 = 0;
    operacion = 0;
    simbolo = 0;
    resultado = 0;
}