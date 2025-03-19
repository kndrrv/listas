class Persona: # se crea la clase persona con lo solicitado
    def __init__(self, nombre, apellido1, apellido2, edad):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__edad = edad

# getters
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido1(self):
        return self.__apellido1
    
    def get_apellido2(self):
        return self.__apellido2
    
    def get_edad(self):
        return self.__edad
    
    def __str__(self): # método para representar la instancia como una cadena de texto
        return(f"Nombre: {self.__nombre}, Apellido1: {self.__apellido1}, Apellido2: {self.__apellido2}, Edad: {self.__edad}")