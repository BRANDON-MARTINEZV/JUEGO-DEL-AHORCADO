class Login:
    def __init__(self):
        # Usuarios predefinidos
        self.usuarios = {"brandon": "1234", "admin": "admin"}

    def iniciar_sesion(self):
        print("\n--- Login ---")
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        if usuario in self.usuarios and self.usuarios[usuario] == password:
            print("Inicio de sesión exitoso.\n")
            return usuario
        else:
            print("Usuario o contraseña incorrectos.\n")
            return None
