#Desarrollar una TO-DO List en python que te permita guardar tareas, saber si estan
#completadas o no, ademas las tareas tienen que ser guardadas en un archivo
#puedes marcar o desmarcar cada tarea como completada (ORIENTADO A OBJETOS)


#importa la clase del archivo donde se encuentra la logica del programa
from TO_DO_LIST_LOGICA import Todo
#se guarda la clase en una variable para ser usada en la funcion List()
to_do = Todo()

#Funcion donde se ejecutan las diferentes acciones en funcion del numero seleccionado
def List():
    to_do.clearConsole()
    ejecutar = 1
    #ciclo para mantener ejecutando el programa hasta que se le solicite detenerse
    while ejecutar == 1:
        #Llama a la funcion para ver el menu principal
        to_do.opciones()
        opcion = input("Selecciona la opcion que quieres realizar: ")
        #limpia la consola
        to_do.clearConsole()
        if opcion == "1":
            #Registro de nueva tarea pendiente
            to_do.guardar()
            List()
        if opcion == "2":
            #Ver tareas pendientes
            to_do.ver()
            List()
        if opcion == "3":
            #Ver tareas completadas
            to_do.vercompleta()
            List()
        if opcion == "4":
            #Reiniciar el programa
            to_do.borrar()
            ejecutar = 0
List()