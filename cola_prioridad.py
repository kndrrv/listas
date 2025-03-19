from nodo import Nodo
from persona import Persona

class ColaPrioridad:
    def __init__(self):
        self.__inicio = None  
        self.__tamaño = 0     

    def insertar(self, persona): # inserta las personas con prioridad
        nuevo_nodo = Nodo(persona)  

        if self.__inicio is None: # verifica si la cola está vacía
            self.__inicio = nuevo_nodo  
   
        elif persona.get_edad() >= 65: # si la persona es mayor de 65 tiene prioridad mayor
          
            if self.__inicio.get_data().get_edad() < 65:
                nuevo_nodo.set_siguiente(self.__inicio)  
                self.__inicio = nuevo_nodo  

            else:
                
                actual = self.__inicio # busca la última persona mayor a 65
                while actual.get_siguiente() and actual.get_siguiente().get_data().get_edad() >= 65:
                    actual = actual.get_siguiente()  # avanza al siguiente nodo

               
                nuevo_nodo.set_siguiente(actual.get_siguiente())  
                actual.set_siguiente(nuevo_nodo)  
  
        else: # en caso de que la persona se menor a 65 
            actual = self.__inicio
            while actual.get_siguiente():  # avanza hasta el último nodo
                actual = actual.get_siguiente()

            actual.set_siguiente(nuevo_nodo)  

        self.__tamaño += 1  # incrementa el tamaño de la cola

    def remover(self): # remueve el primer elemento de la cola
        if self.__inicio is None: 
            return None

        persona = self.__inicio.get_data()  # obtiene la persona del primer nodo
        self.__inicio = self.__inicio.get_siguiente() 
        self.__tamaño -= 1  # disminuye el tamaño de la cola

        return persona  # retorna la persona removida

    def imprimir(self): # imprime todas las personas de la cola
        if self.__inicio is None:  # verifica si la cola está vacía
            print("La cola está vacía")
            return

        print(f"Total de personas en la cola: {self.__tamaño}")
        actual = self.__inicio 
        posicion = 1

        while actual:
            print(f"{posicion}. {actual.get_data()}")  # imprime los datos del nodo actual
            actual = actual.get_siguiente()  # avanza al siguiente nodo
            posicion += 1
    
    def buscar_por_edad(self, edad): # busca por edad
        if self.__inicio is None: # verifica si la cola está vacía
            return []
        
        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if actual.get_data().get_edad() == edad: # si la edad es igual
                resultados.append((posicion, actual.get_data())) # añade a los resultados
            actual = actual.get_siguiente() # avanza al siguiente nodo
            posicion += 1
        
        return resultados
    
    def buscar_por_nombre(self, nombre): # buscar por aproximación del nombre
        if self.__inicio is None: # verifica si la cola está vacía
            return []
        
        resultados = []
        actual = self.__inicio
        posicion = 1

        while actual:
            if nombre.lower() in actual.get_data().get_nombre().lower(): # si el nombre coincide
                resultados.append((posicion, actual.get_data())) # añade a los resultados
            actual = actual.get_siguiente() # avanza al siguiente nodo
            posicion += 1

        return resultados
    
    def buscar_por_apellido(self, apellido): # busca por aproximación de apellidos
        if self.__inicio is None:  # verifica si la cola está vacía
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
        if self.__inicio is None:  # verifica si la cola está vacía
            return False

        if posicion < 1 or posicion > self.__tamaño: # Valida que la posición sea válida
            return False

        if posicion == 1:
            self.__inicio = self.__inicio.get_siguiente()  # la cabeza ahora es el siguiente nodo
            self.__tamaño -= 1  # disminuye el tamaño de la cola
            return True

        actual = self.__inicio # borra el nodo en otra posición
        indice = 1

        while indice < posicion - 1:  # avanza hasta el nodo anterior al que se quiere borrar
            actual = actual.get_siguiente()
            indice += 1

        actual.set_siguiente(actual.get_siguiente().get_siguiente())  # el nodo anterior apunta al siguiente del que se borra
        self.__tamaño -= 1  # disminuye el tamaño de la cola
        return True
    
    def get_tamaño(self):
        return self.__tamaño