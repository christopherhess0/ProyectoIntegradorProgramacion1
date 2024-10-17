import hashlib
import os

# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    # Usamos hashlib con SHA-256
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Encriptamos la contraseña
    contraseña_encriptada = encriptar_contraseña(contraseña)
    
    # Verificamos si el usuario ya existe
    if verificar_usuario_existe(usuario):
        print("El usuario ya existe. Intente con otro nombre de usuario.")
    else:
        # Guardamos usuario y contraseña en el archivo
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{usuario},{contraseña_encriptada}\n")
        print("Usuario registrado con éxito.")

# Función para verificar si un usuario ya existe
def verificar_usuario_existe(usuario):
    if not os.path.exists("usuarios.txt"):
        return False
    
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            usuario_guardado, _ = linea.strip().split(',')
            if usuario_guardado == usuario:
                return True
    return False

# Función para iniciar sesión
def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Encriptamos la contraseña ingresada
    contraseña_encriptada = encriptar_contraseña(contraseña)
    
    # Buscamos al usuario en el archivo
    if not os.path.exists("usuarios.txt"):
        print("No hay usuarios registrados.")
        return
    
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            usuario_guardado, contraseña_guardada = linea.strip().split(',')
            if usuario == usuario_guardado and contraseña_encriptada == contraseña_guardada:
                print("Inicio de sesión exitoso.")
                return
    print("Usuario o contraseña incorrectos.")

# Función principal del programa
def menuLogin():
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú principal
menuLogin()
