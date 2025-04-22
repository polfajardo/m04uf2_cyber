#!/usr/bin/python3

def show_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Álbumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Géneros")
        print("0. Salir")

        opcion = input("Elige una opción (0-4): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 4:
                return opcion
            else:
                print("buff: Introduce un número entre 0 y 4.")
        else:
            print("buff: Error: introduce un número válido.")

def show_menu_songs():
    while True:
        print("\n--- Menú Canciones ---")
        print("1. Listar todas las canciones")
        print("2. Buscar canción por título")
        print("0. Volver")

        opcion = input("Elige una opción (0-2): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("buff: Introduce un número entre 0 y 2.")
        else:
            print("buff: Error: introduce un número válido.")

def show_menu_albums():
    while True:
        print("\n--- Menú Álbumes ---")
        print("1. Listar todos los álbumes")
        print("2. Buscar álbum por título")
        print("0. Volver")

        opcion = input("Elige una opción (0-2): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("buff: Introduce un número entre 0 y 2.")
        else:
            print("buff: Error: introduce un número válido.")

def show_menu_artists():
    while True:
        print("\n--- Menú Artistas ---")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")

        opcion = input("Elige una opción (0-2): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("buff: Introduce un número entre 0 y 2.")
        else:
            print("buff: Error: introduce un número válido.")

def show_menu_genres():
    while True:
        print("\n--- Menú Géneros ---")
        print("1. Listar todos los géneros")
        print("2. Buscar género por nombre")
        print("0. Volver")

        opcion = input("Elige una opción (0-2): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("buff: Introduce un número entre 0 y 2.")
        else:
            print("buff: Error: introduce un número válido.")

# --- Inicio del programa ---
version = 0.5
app_title = "Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))

# Menú principal
while True:
    opcion_elegida = show_menu()

    if opcion_elegida == 1:
        show_menu_albums()
    elif opcion_elegida == 2:
        show_menu_artists()
    elif opcion_elegida == 3:
        show_menu_songs()
    elif opcion_elegida == 4:
        show_menu_genres()
    elif opcion_elegida == 0:
        print("Chao pescao!")
        break
