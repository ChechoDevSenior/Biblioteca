# Definimos una lista vacía para almacenar los libros
biblioteca = []

# Función para agregar un libro
def Agregar_libro():
    isbn = input("Ingrese el ISBN del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = input("Ingrese el año de la publicación del libro: ")

    libro = {
        'ISBN:': isbn,
        'TÍtulo:': titulo,
        'Autor:': autor,
        'Año:': anio,
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

# Función para eliminar libro por ISBN
def Eliminar_libro():
    isbn = input("Ingrese el ISBN del libro a eliminar: ")
    for libro in biblioteca:
        if libro['isbn'] == isbn:
            biblioteca.remove(libro)
            print(f"El libro con ISBN '{isbn}' eliminado con éxito de la biblioteca.")
            return
    print(f"El libro con el ISBN '{isbn}' no fue encontrado en la biblioteca.")

# Menú principal
def menu():
    while True:
        print("\nMenú de la Biblioteca:")
        print("1. Agregar libro.")
        print("2. Eliminar libro.")
        print("3. Mostrar biblioteca.")
        print("4. Salir.")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            Agregar_libro()
        elif opcion == '2':
            Eliminar_libro()
        elif opcion == '3':
            print("\nBiblioteca:")
            if not biblioteca:
                print("La biblioteca está vacía.")
            for libro in biblioteca:
                print(libro)
        elif opcion == '4':
            print("Gracias por usar los servicios de la biblioteca.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú
menu()
