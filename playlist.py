import os
from bs4 import BeautifulSoup

def load_artists():
    print("\n--- Listado de Artistas ---")
    artists_directory = 'artists'
    artist_files = [f for f in os.listdir(artists_directory) if f.endswith('.xml')]

    for artist_file in artist_files:
        artist_path = os.path.join(artists_directory, artist_file)

        with open(artist_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')
            artist_name = soup.find('name')
            if artist_name:
                print(f"- {artist_name.text}")

def load_albums():
    print("\n--- Listado de Álbumes ---")
    albums_directory = 'albums'
    album_files = [f for f in os.listdir(albums_directory) if f.endswith('.xml')]

    for album_file in album_files:
        album_path = os.path.join(albums_directory, album_file)

        with open(album_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')
            album_title = soup.find('title')
            if album_title:
                print(f"- {album_title.text}")

def load_songs():
    print("\n--- Listado de Canciones ---")
    songs_directory = 'songs'
    song_files = [f for f in os.listdir(songs_directory) if f.endswith('.xml')]

    for song_file in song_files:
        song_path = os.path.join(songs_directory, song_file)

        with open(song_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')
            song_title = soup.find('title')
            if song_title:
                print(f"- {song_title.text}")

def load_genres():
    print("\n--- Listado de Géneros ---")
    genres_directory = 'genres'
    genre_files = [f for f in os.listdir(genres_directory) if f.endswith('.xml')]

    for genre_file in genre_files:
        genre_path = os.path.join(genres_directory, genre_file)

        with open(genre_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')
            genre_name = soup.find('name')
            if genre_name:
                print(f"- {genre_name.text}")

def show_menu_songs():
    while True:
        print("\n--- Menú de Canciones ---")
        print("1. Listar todas las canciones")
        print("0. Volver")
        
        option = input("Elige una opción (0-1): ")

        if option == '1':
            load_songs()
        elif option == '0':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 1.")

def show_menu_albums():
    while True:
        print("\n--- Menú de Álbumes ---")
        print("1. Listar todos los álbumes")
        print("0. Volver")
        
        option = input("Elige una opción (0-1): ")

        if option == '1':
            load_albums()
        elif option == '0':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 1.")

def show_menu_artists():
    while True:
        print("\n--- Menú de Artistas ---")
        print("1. Listar todos los artistas")
        print("0. Volver")
        
        option = input("Elige una opción (0-1): ")

        if option == '1':
            load_artists()
        elif option == '0':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 1.")

def show_menu_genres():
    while True:
        print("\n--- Menú de Géneros ---")
        print("1. Listar todos los géneros")
        print("0. Volver")
        
        option = input("Elige una opción (0-1): ")

        if option == '1':
            load_genres()
        elif option == '0':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 1.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Álbumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Géneros")
        print("0. Salir")
        
        option = input("Elige una opción (0-4): ")

        if option == '1':
            show_menu_albums()
        elif option == '2':
            show_menu_artists()
        elif option == '3':
            show_menu_songs()
        elif option == '4':
            show_menu_genres()
        elif option == '0':
            print("¡CHAO PESCAO!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 4.")

if __name__ == "__main__":
    main()
