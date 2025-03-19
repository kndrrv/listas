from nodo_doble import NodoDoble
from persona import Persona

class ListaDoble: # se crea la clase 
    def __init__(self):
        self.__inicio = None  
        self.__cola = None    
        self.__tamaño = 0     

    def insertar(self, persona): # inserta ordenado por edad
        nuevo_nodo = NodoDoble(persona)  # crea un nuevo nodo con la persona

        if self.__inicio is None: # si la lista está vacía
            self.__inicio = nuevo_nodo  # el nuevo nodo es la cabeza
            self.__cola = nuevo_nodo   

        elif persona.get_edad() < self.__inicio.get_data().get_edad(): # inserta al principio si la persona es más joven que la cabeza
            nuevo_nodo.set_siguiente(self.__inicio)  
            self.__inicio.set_previo(nuevo_nodo)      
            self.__inicio = nuevo_nodo                

        elif persona.get_edad() >= self.__cola.get_data().get_edad(): # inserta al final de la cola si la personas es mayor a igual
            nuevo_nodo.set_previo(self.__cola)  
            self.__cola.set_siguiente(nuevo_nodo)  
            self.__cola = nuevo_nodo               

        else: # si hay que insertar en el medio
            actual = self.__inicio
            
            while actual and actual.get_data().get_edad() <= persona.get_edad():# avanza hasta encontrar la posición correcta
                actual = actual.get_siguiente()

            nuevo_nodo.set_siguiente(actual) 
            nuevo_nodo.set_previo(actual.get_previo())  
            actual.get_previo().set_siguiente(nuevo_nodo)  
            actual.set_previo(nuevo_nodo)  

        self.__tamaño += 1  # incrementa el tamaño de la lista

    def imprimir(self): # imprime todas las personas de la lista
        if self.__inicio is None:  # verifica si la lista está vacía
            print("La lista está vacía")
            return

        print(f"Total de personas en la lista: {self.__tamaño}")
        actual = self.__inicio  # empezamos desde la cabeza
        posicion = 1

        while actual:
            print(f"{posicion}. {actual.get_data()}")  # imprime los datos del nodo actual
            actual = actual.get_siguiente()  # avanza al siguiente nodo
            posicion += 1

    def buscar_por_edad(self, edad): # buscar por edad
        if self.__inicio is None:  # verifica si la lista está vacía
            print("La lista está vacía")
            return 

        resultados = []

        dif_inicio = abs(self.__inicio.get_data().get_edad() - edad) # determina si es mejor empezar desde el inicio o desde la cola
        dif_cola = abs(self.__cola.get_data().get_edad() - edad)   

        if dif_inicio <= dif_cola:
            actual = self.__inicio
            posicion = 1

            while actual:
                if actual.get_data().get_edad() == edad:  # si la edad coincide
                    resultados.append((posicion, actual.get_data()))  # añade a los resultados
                actual = actual.get_siguiente()  # avanza al siguiente nodo
                posicion += 1
        else:
            actual = self.__cola
            posicion = self.__tamaño

            while actual:
                if actual.get_data().get_edad() == edad:  # si la edad coincide
                    resultados.append((posicion, actual.get_data()))  # añade a los resultados
                actual = actual.get_previo()  # retrocede al nodo anterior
                posicion -= 1

            resultados.sort(key=lambda x: x[0]) # odena los resultados por posición

        return resultados

    def buscar_por_nombre(self, nombre): # buscar por aproximación de nombre
        if self.__inicio is None:  # verifica si la lista está vacía
            print("La lista está vacía")
            return 

        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if nombre.lower() in actual.get_data().get_nombre().lower():  # si el nombre coincide
                resultados.append((posicion, actual.get_data()))  # añade a los resultados
            actual = actual.get_siguiente()  # avanza al siguiente nodo
            posicion += 1

        return resultados

    def buscar_por_apellido(self, apellido): # buscar por aproximación de apellido
        if self.__inicio is None:  # verifica si la lista está vacía
            print("La lista está vacía")
            return

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

    def borrar_por_posicion(self, posicion): # borrar por posición
        if self.__inicio is None:  # verifica si la lista está vacía
            print("La lista está vacía")
            return
        
        if posicion < 1 or posicion > self.__tamaño: # valida que la posición sea correcta
            return False

        if self.__tamaño == 1: # en caso de qe haya solo un elemento
            self.__inicio = None
            self.__cola = None
            self.__tamaño = 0
            return True

        if posicion == 1: # borra el inicio
            self.__inicio = self.__inicio.get_siguiente()  
            self.__inicio.set_previo(None)  
            self.__tamaño -= 1
            return True

        if posicion == self.__tamaño: # borra la cola
            self.__cola = self.__cola.get_previo()  
            self.__cola.set_siguiente(None)  
            self.__tamaño -= 1
            return True

        if posicion <= self.__tamaño // 2: # verifica si es mejor empezar desde el inicio o desde la cola
            actual = self.__inicio
            indice = 1

            while indice < posicion:
                actual = actual.get_siguiente()
                indice += 1
        else:
            actual = self.__cola
            indice = self.__tamaño

            while indice > posicion:
                actual = actual.get_previo()
                indice -= 1

        actual.get_previo().set_siguiente(actual.get_siguiente())  
        actual.get_siguiente().set_previo(actual.get_previo())    
        self.__tamaño -= 1
        return True