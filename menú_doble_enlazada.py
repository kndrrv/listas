from lista_doble import ListaDoble
from persona import Persona

def menu_principal():
    print("\n MENÚ PRINCIPAL LISTA DOBLEMENTE ENLAZADA")
    print("1. Agregar persona a la lista")
    print("2. Listar personas")
    print("3. Borrar personas")
    print("4. Buscar personas")
    print("5. Salir")
    return input("Seleccione una opción: ")

def menu_busqueda():
    print("\n OPCIONES DE BÚSQUEDA ")
    print("1. Buscar por edad")
    print("2. Buscar por nombre")
    print("3. Buscar por apellido")
    print("4. Volver al menú principal")
    return input("Seleccione una opción: ")

def agregar_persona(lista):
    print("\n AGREGAR PERSONA ")
    nombre = input("Nombre: ")
    apellido1 = input("Primer apellido: ")
    apellido2 = input("Segundo apellido: ")
    

    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Error: La edad debe ser un número entero.")
    

    persona = Persona(nombre, apellido1, apellido2, edad)
    lista.insertar(persona)
    print(f"\nPersona agregada: {persona}")

def listar_personas(lista):
    print("\n LISTA DE PERSONAS ")
    lista.imprimir()

def borrar_persona(lista):
    print("\n BORRAR PERSONA ")
    

    listar_personas(lista)
    
    if lista._ListaDoble__tamaño == 0:
        return
    
   
    while True:
        try:
            posicion = int(input(f"\nIngrese el # de item a borrar (1-{lista._ListaDoble__tamaño}): "))
            if posicion < 1 or posicion > lista._ListaDoble__tamaño:
                print(f"Error: El número debe estar entre 1 y {lista._ListaDoble__tamaño}.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero.")
    
  
    if lista.borrar_por_posicion(posicion):
        print(f"Persona en la posición {posicion} borrada exitosamente.")
    else:
        print(f"No se pudo borrar. La lista tiene {lista._ListaDoble__tamaño} elementos.")

def buscar_por_edad(lista):
    print("\n BUSCAR POR EDAD ")
    
 
    while True:
        try:
            edad = int(input("Ingrese la edad a buscar: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero.")
    
 
    resultados = lista.buscar_por_edad(edad)
    
    if not resultados:
        print(f"No se encontraron personas con {edad} años.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con {edad} años:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def buscar_por_nombre(lista):
    print("\n BUSCAR POR NOMBRE ")
    
    nombre_parcial = input("Ingrese parte del nombre a buscar: ")
    
    resultados = lista.buscar_por_nombre(nombre_parcial)
    
    if not resultados:
        print(f"No se encontraron personas con '{nombre_parcial}' en su nombre.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con '{nombre_parcial}' en su nombre:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def buscar_por_apellido(lista):
    print("\n  BUSCAR POR APELLIDO")
    
    apellido_parcial = input("Ingrese parte del apellido a buscar: ")
   
    resultados = lista.buscar_por_apellido(apellido_parcial)
    
    if not resultados:
        print(f"No se encontraron personas con '{apellido_parcial}' en sus apellidos.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con '{apellido_parcial}' en sus apellidos:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def main():
    lista = ListaDoble()
    
    # datos de ejemplo
    lista.insertar(Persona("Kendra", "Vega", "Gutiérrez", 20))
    lista.insertar(Persona("Amanda", "Quesada", "Porras", 20))  
    lista.insertar(Persona("Alvaro", "Vega", "Zuñiga", 68))
    lista.insertar(Persona("Zelmira", "Ordoñez", "Quirós", 66)) 
    
    print("Bienvenido al programa de gestión de personas con Lista Doblemente Enlazada")
    print("La lista está ordenada por edad de menor a mayor")
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            agregar_persona(lista)
        elif opcion == "2":
            listar_personas(lista)
        elif opcion == "3":
            borrar_persona(lista)
        elif opcion == "4":
            while True:
                opcion_busqueda = menu_busqueda()
                
                if opcion_busqueda == "1":
                    buscar_por_edad(lista)
                elif opcion_busqueda == "2":
                    buscar_por_nombre(lista)
                elif opcion_busqueda == "3":
                    buscar_por_apellido(lista)
                elif opcion_busqueda == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
        elif opcion == "5":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()