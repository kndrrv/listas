class Nodo: # se crea la clase nodo para una lista enlazada
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_siguiente(self, next_node): # setter para el nodo siguiente
        self.__next = next_node

    def get_siguiente(self): # getter
        return self.__next
    
    def get_data(self):
        return self.__data
    
    def __str__(self):
        return f"Data: {self.__data}"