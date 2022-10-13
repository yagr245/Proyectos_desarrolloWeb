import re

#Inicializa la clase
class nombres:
    
    #1. define la funcion self que contiene la lista de registros
    def __init__(self):
        self.datos = []
    
    #2. guarda los datos introducidos en la lista de registros
    def registro(self):
        #2.1. Introducir los datos solicitados (nombre, apellido y correo)
        nombre = input("Introduce tu nombre, debe empezar con mayúscula y tener de 2 a 30 caracteres: ")
        apellido = input("Introduce tu apellido, debe empezar con mayúscula y tener de 2 a 30 caracteres: ")
        email = input("Introduce tu email, ejemplo: email@dominio.com: ")
        #2.2. Condicional donde se determina a traves de expresiones regulares que los datos
        # solicitados cumplan con los parametros requeridos
        # Nombre: Comienza con letra mayuscula, el resto en minuscula, entre 2 y 30 caracteres
        # Apellido: Comienza con letra mayuscula, el resto en minuscula, entre 2 y 30 caracteres
        # Email: Cualquier caracter alfanumerico incluidos los caracteres (._%+-) para el nombre
        # del correo + el simbolo (@) + cualquier caracter alfanumerico incluidos los 
        # caracteres (._-) + (.) + cualquier caracter alfanumerico para el nombre del dominio 
        if re.fullmatch(r'[A-Z][a-z]{2,30}', nombre) and re.fullmatch(r'[A-Z][a-z]{2,30}', apellido) and re.fullmatch(r'^[\w._%+-]+[@][\w._-]+[.][\w]{2,3}$', email):
            #2.2.1. Si se cumple la condicion se registran los datos en el objeto registro_datos
            registro_datos = { "nombre":nombre, "apellido":apellido, "email":email}
            #2.2.2. Se agrega a la lista datos el objeto
            self.datos.append(registro_datos)
            print(registro_datos["nombre"], registro_datos["apellido"], registro_datos["email"])
            input("Presiona enter para volver al menu principal")
        else:
            #2.2.3. Si no se cumple con alguna de las condiciones, es necesario realizar el 
            # registro nuevamente siguiendo los parametros indicados
            print("Uno de los datos es incorrecto, por favor ingresa nuevamente e introduce los datos de forma correcta")
            input("Presiona enter para volver al menu principal")
            
    #3. visualiza la lista de registros 
    def ver(self):
        print("Esta es la cantidad de registros: ")
        #3.1. variable de control para enumerar los registros
        i = 1
        #3.2. crea, abre, escribe y cierra el archivo donde se tendra la lista de registros
        archivo = open("regulares.txt", "a")
        archivo.write("Esta es la cantidad de registros: \n\n")
        archivo.close()
        #3.3. ciclo para recorrer la lista donde se encuentran guardados los registros
        for registro_datos in self.datos:
            #3.3.1. imprime y enumera cada uno de los registros
            print(str(i) + ". " + registro_datos["nombre"] + " " + registro_datos["apellido"] + ", " + registro_datos["email"])
            #3.3.2. en cada ciclo se escribe cada uno de los registros en el archivo
            archivo = open("regulares.txt", "a")
            archivo.write(str(i) + ". " + registro_datos["nombre"] + " " + registro_datos["apellido"] + ", " + registro_datos["email"] + "\n")
            archivo.close()
            #3.3.3. se suma +1 a la variable de control para enumerar los registros
            i += 1     
        input("Presiona enter para volver al menu principal")
    
    #4. Muestra el menu principal
    def opciones(self):
        print("Bienvenido, registra tu nombre y correo: ")
        print("1. Registrar Nombre y Correo")
        print("2. Generar archivo con la informacion")
        print("3. Reiniciar el programa")

    #5. Limpia la terminal
    def clearConsole(self):
        import os
        os.system ("cls")
    
    #6. Limpia las listas, y elimina el archivo existente para inicializar nuevamente el programa
    def borrar(self):
        self.datos.clear()
        import os
        if os.path.exists("regulares.txt"):
            os.remove("regulares.txt")
        else:
            print("El archivo no existe")