# Crear un programa el cual te permita guardar nombres y correos, ver esos nombres y
# correos en un archivo. SIN EMBARGO, los correos y nombres deben ser correctamente
# validados, un nombre no puede contener numeros ni caracteres extra;os y debe
# al menos tener 2 caracteres y un maximo de 30 (ORIENTADO A OBJETOS, Investigar
# expresiones regulares en python para hacer esto)

from Expresiones_regulares_logica import nombres
names = nombres()

def Nuevo():
    names.clearConsole()
    ejecutar = 1
    #ciclo para mantener ejecutando el programa hasta que se le solicite detenerse
    while ejecutar == 1:
        #Llama a la funcion para ver el menu principal
        names.opciones()
        opcion = input("Selecciona la opcion que quieres realizar: ")
        #limpia la consola
        names.clearConsole()
        if opcion == "1":
            #Nuevo registro
            names.registro()
            Nuevo()
        if opcion == "2":
            #Ver registros
            names.ver()
            Nuevo()
        if opcion == "3":
            #Reiniciar el programa
            names.borrar()
            ejecutar = 0
Nuevo()