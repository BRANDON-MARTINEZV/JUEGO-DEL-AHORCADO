import random
from login import Login

class Ahorcado:
    def __init__(self):
        # Lista de palabras
        self.palabras = ['gato', 'perro', 'elefante', 'jirafa', 'rinoceronte', 'leon']
        self.intentos = 0
        self.max_intentos = 6
        self.palabra_secreta = ""
        self.palabra_oculta = ""
        self.letras_adivinadas = []
        self.dibujos = [
             """
               ------
               |    |
               |    
               |    
               |    
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |    
               |    
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               |    
            ========
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |    
            ========
            """
        ]

    def elegir_palabra(self):
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_oculta = "_" * len(self.palabra_secreta)

    def mostrar_estado(self):
        print("\nPalabra:", self.palabra_oculta)
        print(self.dibujos[self.intentos])
        print("Letras incorrectas:", ", ".join(self.letras_adivinadas))

    def verificar_letra(self, letra):
        if letra in self.palabra_secreta:
            for i in range(len(self.palabra_secreta)):
                if self.palabra_secreta[i] == letra:
                    self.palabra_oculta = self.palabra_oculta[:i] + letra + self.palabra_oculta[i+1:]
            print("¡Bien hecho!")
        else:
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)
                self.intentos += 1
                print(f"Letra incorrecta. Te quedan {self.max_intentos - self.intentos} intentos.")

    def iniciar_juego(self):
        self.elegir_palabra()
        while self.intentos < self.max_intentos:
            self.mostrar_estado()
            letra = input("Ingresa una letra: ").lower()

            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, ingresa solo una letra.")
                continue

            if letra in self.palabra_oculta or letra in self.letras_adivinadas:
                print("Ya intentaste esa letra, ¡intenta otra!")
                continue

            self.verificar_letra(letra)

            if "_" not in self.palabra_oculta:
                print(f"¡Felicidades! Adivinaste la palabra: {self.palabra_secreta}")
                break

        if self.intentos == self.max_intentos:
            print(f"Lo siento, perdiste. La palabra era: {self.palabra_secreta}")

def main():
    print("¡Bienvenido al juego de Ahorcado!")

    # Realizar login
    login = Login()
    usuario = login.iniciar_sesion()

    if usuario:
        print(f"¡Hola, {usuario}! Prepárate para jugar.\n")
        juego = Ahorcado()
        juego.iniciar_juego()
    else:
        print("No se pudo iniciar sesión. Saliendo del programa.")

if __name__ == "__main__":
    main()
