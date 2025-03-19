class NodoDoble: # se crea la clase nodo para la lista doblemente enlazada
    def __init__(self, data):
        self.__data = data
        self.__siguiente = None
        self.__previo = None

# setters
    def set_siguiente(self, siguiente_nodo):
        self.__siguiente = siguiente_nodo

    def set_previo(self, nodo_previo):
        self.__previo = nodo_previo

# getters

    def get_siguiente(self):
        return self.__siguiente
    
    def get_previo(self):
        return self.__previo
    
    def get_data(self):
        return self.__data
    
    def __str__(self):
        previo = None
        siguiente = None
        if self.__previo != None:
            previo = self.__previo.get_data()
        if self.__siguiente != None: 
            next = self.__siguiente.get_data()
        return f"Data: {self.__data}, Previo: {previo}, Siguiente: {siguiente}"