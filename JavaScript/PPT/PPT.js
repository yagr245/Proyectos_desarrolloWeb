var player = ["Piedra", "Papel", "Tijera"]
var a = '', b = '';


function computadora(player){
    var aleatorio = Math.floor(Math.random() * 3) //numero entre 0 y 2;
    var jugador = player;
    var ganadas = document.getElementById("ganadas").value;
    var perdidas = document.getElementById("perdidas").value;
    var contador = document.getElementById("contador").value;
    
    if(aleatorio == 0){
        var computer = "Piedra";
    }
    else if (aleatorio == 1) {
        var computer = "Papel";
    }
    else{
        var computer = "Tijera";
    }

    console.log(computer);
    document.getElementById("jugador").value = jugador;
    document.getElementById("computer").value = computer;
    var registropc = document.getElementById("computer").value;
    var registrojugador = document.getElementById("jugador").value;

    if(jugador == computer){
        ganadas = parseInt(ganadas) + 0;
        perdidas = parseInt(perdidas) + 0;
        contador = parseInt(contador) + 1; 
        a = a + registrojugador + " - "
        b = b + registropc + " - "    
    } 
    else if(jugador == "Piedra" && computer == "Tijera"){
        victoria();
    } 
    else if(jugador == "Piedra" && computer == "Papel"){
        derrota();
    } 
    else if(jugador == "Papel" && computer == "Piedra"){
        victoria();
    } 
    else if(jugador == "Papel" && computer == "Tijera"){
        derrota();   
    } 
    else if(jugador == "Tijera" && computer == "Papel"){
        victoria();  
    } 
    else if(jugador == "Tijera" && computer == "Piedra"){
        derrota();
    } 

    function victoria(){
        ganadas = parseInt(ganadas) + 1;
        contador = parseInt(contador) + 1;  
        a = a + registrojugador + " - "
        b = b + registropc + " - " 
    }

    function derrota(){
        perdidas = parseInt(perdidas) + 1;
        contador = parseInt(contador) + 1; 
        a = a + registrojugador + " - "
        b = b + registropc + " - " 
    }

    console.log(contador);
    document.getElementById("ganadas").value = ganadas;
    document.getElementById("perdidas").value = perdidas;
    document.getElementById("contador").value = contador;
    document.getElementById("resultado1").value = a;
    document.getElementById("resultado2").value = b;
}