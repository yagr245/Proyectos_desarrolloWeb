#Inicializa la clase
class Todo:
    
    #1. define la funcion self que contiene las listas de objetos
    def __init__(self):
        self.lista_incompleta = []
        self.lista_completa = []
    
    #2. guarda los datos introducidos en la lista de tareas pendientes
    def guardar(self):
        tarea = input("Nueva tarea\n")
        to_do = { "tarea":tarea}
        self.lista_incompleta.append(to_do)
        input("Desea volver al menu principal?")
    
    #3. visualiza la lista de tareas pendientes 
    def ver(self):
        print("Esta es tu lista de tareas Pendientes: ")
        #3.1. variable de control para enumerar las tareas
        i = 1
        #3.2. crea, abre, escribe y cierra el archivo donde se tendra la lista de tareas pendientes
        archivo = open("to_do.txt", "a")
        archivo.write("Esta es tu lista de tareas Pendiente: \n")
        archivo.close()
        #3.3. ciclo para recorrer la lista donde se encuentran guardadas las tareas pendientes
        for to_do in self.lista_incompleta:
            #3.3.1. imprime y enumera cada una de las tareas pendientes
            print(str(i) + ". " + to_do["tarea"])
            #3.3.2. en cada ciclo se escribe cada una de las tareas en el archivo de tareas pendientes
            archivo = open("to_do.txt", "a")
            archivo.write(str(i) + ". " + to_do["tarea"] + "\n\n")
            archivo.close()
            #3.3.3. se suma +1 a la variable de control para enumerar las tareas pendientes
            i = i + 1
        #3.4. variable y condicion para eliminar una tarea pendiente de la lista, y agregarla a
        #la lista de tareas completadas, en caso de no querer quitar alguna se selecciona 0 para 
        #volver al menu principal
        tarea_seleccionada = input("Seleccione la tarea que fue completada, sino seleccione 0: ")
        if tarea_seleccionada == "0":
            input("Desea volver al menu principal?")
        else:
            tarea_completada = self.lista_incompleta[int(tarea_seleccionada)-1]
            self.lista_completa.append(tarea_completada)
            self.lista_incompleta.pop(int(tarea_seleccionada)-1)
            input("Desea volver al menu principal?")
    
    #4. visualiza la lista de tareas completadas
    def vercompleta(self):
        print("Esta es tu lista de tareas Completadas: ")
        j = 1
        #4.1. se escribe sobre el archivo existente para agregar la lista de tareas completadas
        archivo = open("to_do.txt", "a")
        archivo.write("Esta es tu lista de tareas Completadas: \n\n")
        archivo.close()
        #4.2. mismo procedimiento que el punto 3.3 para ver la lista de tareas completadas
        for tarea_completada in self.lista_completa:
            print(str(j) + ". " + tarea_completada["tarea"])
            archivo = open("to_do.txt", "a")
            archivo.write(str(j) + ". " + tarea_completada["tarea"] + "\n\n")
            archivo.close()
            j = j + 1
        input("Desea volver al menu principal?")
    
    #5. Muestra el menu principal
    def opciones(self):
        print("Bienvenido a tu lista de tareas, selecciona que desea hacer: ")
        print("1. Guardar nueva tarea")
        print("2. Ver lista de tareas Pendientes")
        print("3. Ver lista de tareas Completadas")
        print("4. Terminar programa")

    #6. Limpia la terminal
    def clearConsole(self):
        import os
        os.system ("cls")
    
    #7. Limpia las listas, y elimina el archivo existente para inicializar nuevamente el programa
    def borrar(self):
        self.lista_completa.clear()
        self.lista_incompleta.clear()
        import os
        if os.path.exists("to_do.txt"):
            os.remove("to_do.txt")
        else:
            print("El archivo no existe")