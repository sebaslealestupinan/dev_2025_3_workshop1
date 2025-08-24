class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        return (metros * 3.28084)
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        return (pies / 3.28084)
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        binario =''

        if decimal == 0:
            binario = '0'
        else:
            while decimal > 0:

                divi = decimal//2

                if decimal - divi*2 == 0:
                    binario= '0'+binario
                else:
                    binario='1'+binario

                decimal = divi
        return (binario)
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        
        lista = list(binario)
        lista.reverse()

        Decimal = 0
        multi= 1

        if  lista[0] == "1":
            Decimal=1

        del lista[0]

        for n in lista:
            multi = multi * 2

            if n == "1":
                Decimal= Decimal + multi
        

        return (Decimal)


    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        dicRomanos = [
               (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
                (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
                ]

        romano = ""
    
        for num, letra in dicRomanos:
               while numero >= num:
                numero-= num
                romano+= letra

        return (romano) 
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        dic= {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        f= len(romano)
        decimal= 0
        for i in range(f):
                
                letra_actual= dic[romano[i]]

                if i +1 < f:
                        letra_siguiente = dic[romano[i+1]]

                        if letra_actual < letra_siguiente:
                                decimal-= letra_actual
                                continue
                decimal+=letra_actual
                        
        return (decimal)
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        codeMorse= {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
        "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
        "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
        "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
        "Z": "--..",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}
        TEXTO = texto.upper()

        n = len(TEXTO)

        morse =""

        for x in range(n):
                Traducir = codeMorse[TEXTO[x]]
                if x >= 1:
                    
                    morse += " "+Traducir

                else: 
                     morse += Traducir

        return morse
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """

        decodificacion= ""

        if morse == "":

            decodificacion = ""

        else: 
            codeMorse= {
            ".-" : "A",   "-...": "B",  "-.-.": "C",  "-..": "D",   ".": "E",
            "..-.": "F",  "--.": "G",   "....": "H",  "..": "I",    ".---": "J",
            "-.-": "K",   ".-..": "L",  "--": "M",    "-.": "N",    "---": "O",
            ".--.": "P",  "--.-": "Q",  ".-.": "R",   "...": "S",   "-": "T",
            "..-": "U",   "...-": "V",  ".--": "W",   "-..-": "X",  "-.--": "Y",
            "--..": "Z", "--": " ",

            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}

            morse += " "
            f = len(morse)
            letraMorse = ""

            for i in range(f):
                
                    if morse[i] == " " and morse[i-1] != " ":
                        
                        decodificacion+= codeMorse[letraMorse]

                        letraMorse = ""

                    else: 
                        if morse[i] != " ":
                            letraMorse += morse[i]
        
        return decodificacion