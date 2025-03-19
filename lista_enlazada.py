from nodo import Nodo
from persona import Persona

class Lista_enlazada:
    def __init__(self):
        self.__inicio = None
        self.__tamaño = 0

    def insertar(self, persona): # insertar por edad de menor a mayor
        nuevo_nodo = Nodo(persona)

        if self.__inicio is None or persona.get_edad() < self.__inicio.persona.get_edad(): # verifica si la lista está vacía o el nuevo nodo debe ir al principio
            nuevo_nodo.get_siguiente = self.__inicio
            self.__inicio = nuevo_nodo

        else:
            actual = self.__inicio
            while actual.get_siguiente() and actual.get_siguiente.persona.get_edad() <= persona.get_edad(): # busca la posición correcta para insertar
                actual = actual.get_siguiente() # avanza al siguiente nodo

            nuevo_nodo.set_siguiente = actual.get_siguiente # el nuevo nodo apunta el nuevo nodo
            actual.set_siguiente = nuevo_nodo
        
        self.__tamaño += 1 # incrementa el tamaño de la lista

    def imprimir(self): # imprime todas las personas de la lista
        if self.__inicio is None: # verifica si la lista está vacía
            print("La lista está vacía")
            return
        
        print(f"Total de personas en la lista: {self.__tamaño}") # imprime el total de las personas
        actual = self.__inicio
        posicion += 1

        while actual:
            print(f"{posicion}, {actual.get_data()}") # imprime los datos del nodo actual
            actual = actual.get_siguiente # avanza al siguiente nodo
            posicion +=1

    def buscar_por_edad(self, edad): # busca por edad
        if self.__inicio is None: # verifica si la lista está vacía
            print("La lista está vacía")
            return
        
        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if actual.persona.get_edad() == edad: # si la edad es igual
                resultados.append((posicion, actual.persona)) # añade a los resultados
            actual = actual.get_siguiente # avanza al siguiente nodo
            posicion += 1
        
        return resultados
    
    def buscar_por_nombre(self, nombre): # buscar por aproxiamación del nombre
        if self.__inicio is None: # verifica si a lista está vacía
            print("La lista está vacía")
            return 
        
        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if nombre.lower() in actual.persona.get_nombre().lower(): # si el nombre coincide
                resultados.append(posicion, actual.persona) # añade a los resultados
                actual = actual.get_siguiente() # avanza al siguiente nodo
                posicion += 1

        return resultados
    
    def buscar_por_apellido(self, apellido): # busca por aproximación de apellidos
        if self.__inicio is None:  # verifica si la lista está vacía
            return []

        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if (apellido.lower() in actual.get_data().get_apellido1().lower() or
                apellido.lower() in actual.get_data().get_apellido2().lower()):  # si el apellido coincide
                resultados.append((posicion, actual.get_data()))  # añade a los resultados
            actual = actual.get_siguiente()  # avanza al siguiente nodo
            posicion += 1

        return resultados
    
    def borrar_por_posicion(self, posicion):
        if self.__inicio is None:  # verifica si la lista está vacía
            return False

        if posicion < 1 or posicion > self.__tamaño: # Valida que la posición sea válida
            return False

        if posicion == 1:
            self.__inicio = self.__inicio.get_siguiente()  # la cabeza ahora es el siguiente nodo
            self.__tamaño -= 1  # disminuye el tamaño de la lista
            return True

        actual = self.__inicio # borra el nodo en otra posición
        indice = 1

        while indice < posicion - 1:  # avanza hasta el nodo anterior al que se quiere borrar
            actual = actual.get_siguiente()
            indice += 1

        actual.set_siguiente(actual.get_siguiente().get_siguiente())  # el nodo anterior apunta al siguiente del que se borra
        self.__tamaño -= 1  # disminuye el tamaño de la lista
        return True