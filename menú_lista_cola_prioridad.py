from cola_prioridad import ColaPrioridad
from persona import Persona

def menu_principal():
    print("\n   MENÚ PRINCIPAL COLA DE PRIORIDAD")
    print("1. Agregar persona a la cola")
    print("2. Listar personas")
    print("3. Borrar personas")
    print("4. Buscar personas")
    print("5. Salir")
    return input("Seleccione una opción: ")

def menu_busqueda():
    print("\n OPCIONES DE BÚSQUEDA")
    print("1. Buscar por edad")
    print("2. Buscar por nombre")
    print("3. Buscar por apellido")
    print("4. Volver al menú principal")
    return input("Seleccione una opción: ")

def agregar_persona(cola):
    print("\n AGREGAR PERSONA ")
    nombre = input("Nombre: ")
    apellido1 = input("Primer apellido: ")
    apellido2 = input("Segundo apellido: ")
    
    while True: # valida que sea un número
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Error: La edad debe ser un número entero.")
    
    persona = Persona(nombre, apellido1, apellido2, edad) # crea la persona y la agrega a la cola
    cola.insertar(persona)
    print(f"\n Persona agregada: {persona}")
    if edad >= 65:
        print("La persona tiene prioridad por ser mayor de 65 años.")
    else:
        print("La persona ha sido agregada al final de la cola.")

def listar_personas(cola):
    print("\n LISTA DE PERSONAS ")
    print("Las personas mayores de 65 años tienen prioridad y se muestran primero.")
    cola.imprimir()

def borrar_persona(cola):
    print("\n  BORRAR PERSONA ")
    
    listar_personas(cola) # muestra la lista primero
    
    if cola.get_tamaño() == 0:
        return
    
    while True: # solicita la posición
        try:
            posicion = int(input(f"\n Ingrese el # de item a borrar (1-{cola.get_tamaño()}): "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero.")
    
    if cola.borrar_por_posicion(posicion):
        print(f"Persona en la posición {posicion} borrada exitosamente.")
    else:
        print(f"No se pudo borrar. La cola tiene {cola.get_tamaño()} elementos.")

def buscar_por_edad(cola):
    print("\n  BUSCAR POR EDAD ")
    
    while True: # pide la edad
        try:
            edad = int(input("Ingrese la edad a buscar: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero.")
    
    # Realizar la búsqueda
    resultados = cola.buscar_por_edad(edad)
    
    if not resultados:
        print(f"No se encontraron personas con {edad} años.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con {edad} años:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def buscar_por_nombre(cola):
    print("\n BUSCAR POR NOMBRE ")
    
    nombre = input("Ingrese parte del nombre a buscar: ")
    
    # Realizar la búsqueda
    resultados = cola.buscar_por_nombre(nombre)
    
    if not resultados:
        print(f"No se encontraron personas con '{nombre}' en su nombre.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con '{nombre}' en su nombre:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def buscar_por_apellido(cola):
    print("\n BUSCAR POR APELLIDO ")
    
    apellido = input("Ingrese parte del apellido a buscar: ")
    
    # Realizar la búsqueda
    resultados = cola.buscar_por_apellido(apellido)
    
    if not resultados:
        print(f"No se encontraron personas con '{apellido}' en sus apellidos.")
    else:
        print(f"Se encontraron {len(resultados)} persona(s) con '{apellido}' en sus apellidos:")
        for posicion, persona in resultados:
            print(f"{posicion}. {persona}")

def main():
    cola = ColaPrioridad()
    
    # datos de ejemplo
    cola.insertar(Persona("Kendra", "Vega", "Gutiérrez", 20))
    cola.insertar(Persona("Amanda", "Quesada", "Porras", 20))  
    cola.insertar(Persona("Alvaro", "Vega", "Zuñiga", 68))
    cola.insertar(Persona("Zelmira", "Ordoñez", "Quirós", 66))  
    
    print("Bienvenido al programa de gestión de personas con Cola de Prioridad")
    print("Las personas mayores de 65 años tienen prioridad y se colocan primero")
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            agregar_persona(cola)
        elif opcion == "2":
            listar_personas(cola)
        elif opcion == "3":
            borrar_persona(cola)
        elif opcion == "4":
            while True:
                opcion_busqueda = menu_busqueda()
                
                if opcion_busqueda == "1":
                    buscar_por_edad(cola)
                elif opcion_busqueda == "2":
                    buscar_por_nombre(cola)
                elif opcion_busqueda == "3":
                    buscar_por_apellido(cola)
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