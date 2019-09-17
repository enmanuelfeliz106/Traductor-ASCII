

#Traductor ASCII
#Enmanuel Feliz Espinal - 1064591


diccionarioLetras={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e' : 101,
                   'f': 102, 'g': 103, 'h' : 104,'i': 105, 'j': 106, 'k' : 107,
                   'l': 108, 'm': 109, 'n' : 110,'o': 111, 'p': 112, 'q' : 113,
                   'r': 114, 's': 115, 't' : 116,'u': 117, 'v': 118, 'w' : 119,
                   'x': 120, 'y': 121, 'z' : 122,'{': 123, '|': 124, '}' : 125,
                   '~': 126, '@': 64, 'A' : 65,'B': 66, 'C': 67, 'D' : 68, 'E': 69,
                   'F': 70, 'G' : 71, 'H': 72, 'I': 73, 'J' : 74, 'K': 75,
                   'L': 76, 'M' : 77, 'N': 78, 'O': 79, 'P' : 80, 'Q': 81,
                   'R': 82, 'S' : 83, 'T': 84, 'U': 85, 'V' : 86, 'W': 87,
                   'X': 88, 'Y' : 89, 'Z': 90, '[': 91, 'barra invertida (\)' : 92, ']': 93,
                   '^': 94, '_' : 95}

diccionarioNumeros={ 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e',
                   102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k',
                   108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q',
                   114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w',
                   120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}',
                   126: '~', 64 : '@', 65: 'A' , 66: 'B', 67: 'C', 68: 'D', 69: 'E',
                   70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K',
                   76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q',
                   82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W',
                   88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: 'barra invertida (\)' , 93: ']',
                   94: '^', 95: '_'}

def validarDatos(x):
        while (x!=1 or x!=2 or x!=3):
            try:
                x = int(x)
                if (x==1 or x==2 or x==3):
                    return x
                    
                else:
                    print("Entrada invalida. Elija solo de las opciones disponibles\n")
                    x= input("Escriba su opcion y presione enter:")

            except ValueError:
                print("Entrada invalida. Elija solo de las opciones disponibles\n")
                x= input("Escriba su opcion y presione enter:")
                print("\n")

def conversionALetra():
    numero= int(input("Ingrese el numero y presione enter:"))
    aLetra=diccionarioNumeros.get(numero)
    print ("La traduccion es:" , aLetra)

def conversionANumero():
    letra=input("Ingrese la letra y presione enter:")
    aNumero=diccionarioLetras.get(letra)
    print ("La traduccion es:" , aNumero)

def main ():
    print ("--------------------Traductor ASCII-------------------\n")
    print ("Opcion 1: Traducir numeros a letras")
    print ("Opcion 2: Traducir letras a numeros")
    print ("Opcion 3: Salir\n")

    entrada= input("Escriba su opcion y presione enter:")
    print("\n")
    
    opcion=validarDatos(entrada)

    if opcion==1: 
        conversionALetra()
        print("\n")
        main()
        
    elif opcion==2:
        conversionANumero()
        print("\n")
        main()

    elif opcion==3:
        print ("Gracias por utilizar Traductor ASCII")
        


main()


