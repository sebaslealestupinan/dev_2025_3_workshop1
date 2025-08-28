class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        J1= jugador1.lower()
        J2= jugador2.lower()

        element= ["piedra", "tijera", "papel"]

        if J1 not in element or J2 not in element:    
                                 
                return "invalid"
        
        else:

            if J1 == J2:
                    
                return "empate"
                
            if (
            (J1 == "piedra" and J2 == "tijera") or
            (J1 == "tijera" and J2 == "papel") or
            (J1 == "papel" and J2 == "piedra")
                ):
                return "jugador1"
            
            else:

                return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if numero_secreto == intento:

            return "correcto"
        if numero_secreto < intento:

            return "muy alto"
        if numero_secreto > intento:

            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        for fila in tablero:
            if all(c == "X" for c in fila):

                return "X"
            
            if all(c == "O" for c in fila):

                return "O"

    
        for colum in range(3):
            if tablero[0][colum] == tablero[1][colum] == tablero[2][colum] != " ":

                return tablero[0][colum]

  
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":

            return tablero[0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":

            return tablero[0][2]

    
        for fila in tablero:
            for cel in fila:
                if cel == " ":
                    return "continua"

        return "empate"
         
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if 0 <= hasta_col <= 8 and 0 <= hasta_fila <= 8:
        
            if desde_col == hasta_col and desde_fila == hasta_fila: 

                return False
            
            elif desde_col == hasta_col and desde_fila != hasta_fila:
                
                return True
            
            elif desde_col != hasta_col and desde_fila == hasta_fila:

                return True
            
            elif desde_col != hasta_fila and desde_col != hasta_col:

                return False
            
            else: 

                return False

        else: 
            return False