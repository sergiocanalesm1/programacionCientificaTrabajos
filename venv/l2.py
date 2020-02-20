## Punto 1
print("Ingrese un numero decimal entero para convertirlo a binario")
entero = int(input())
binario = ""
if entero == int(entero):
    if entero > 0:
        #cumple requisitos
        while entero > 0:
            binario = str(entero % 2) + binario #funciona porque binario es un string y se añade el residuo como un caracter
            entero = entero // 2
        print(binario)
    else:
        print("ingrese un número positivo")
else:
    print("ingrese un número entero")

## Punto 2

print("Ingrese un numero para representarlo en complemento a 2")
entrada = input()
if "," not in entrada or "." not in entrada:
    # es entero
    enteroGlobal = int(entrada)
    entero = enteroGlobal  # el entero normalito se modifica
    print("Ingrese el número de bits con los que quiere representar {}".format(entero))
    bits = int(input())
    bitsGlobal = bits  # para guardar el valor y llamarlo más adelante, bits normalito se modifica
    binario = ""
    suficientesBits = True
    negativo = False
    if entero < 0:
        entero = abs(entero)
        negativo = True
    while bits >= 0:
        if bits == 0 and entero > 0:
            suficientesBits = False
            break
        if entero == 0:
            binario = str(
                "0") * bits + binario  # como binario es un string, simplemente toca multiplicar por 0s para rellenar
            break
        binario = str(
            entero % 2) + binario  # como binario es un string, los nuevos caracteres se agregan a la izquierda
        bits -= 1
        entero = entero // 2
    if suficientesBits:
        if negativo:
            # toca invertirlo
            complementoA1 = [abs(int(bit) - 1) for bit in binario]  # se crea una nueva lista invirtiendo cada bit
            stringComplementoA1 = [str(x) for x in complementoA1]  # para poder mostrarlo en consola
            print("el complemento a 1 es: {}".format("".join(stringComplementoA1)))
            # sumarle 1
            i = len(binario) - 1
            while True:
                if i < 0 and bitsGlobal > len(complementoA1):
                    complementoA1.insert(0, "1")  # toca hacerlo así porque va ser un string más grande
                    break
                if int(complementoA1[i]) + 1 == 2:  # si era uno
                    complementoA1[i] = "0"  # sigue haciendo el while
                    i -= 1
                else:  # si es cero
                    complementoA1[i] = "1"
                    break
            complementoA2Lista = [str(bit) for bit in complementoA1]
            complementoA2 = "".join(complementoA2Lista)

            print(
                "el complemento a 2 del entero {} con {} bits, es: {}".format(enteroGlobal, bitsGlobal, complementoA2))
        else:
            if binario[0] == "1" and binario[1:] == str("0") * (bitsGlobal - 1):  # para el más grande
                print(
                    "{} bits no son suficientes para expresar el entero {} en offset".format(bitsGlobal, enteroGlobal))
            else:
                print("el número {} en binario es: {}".format(enteroGlobal, binario))
    else:
        print("{} bits no son suficientes para expresar el entero {} en complemento a dos".format(bitsGlobal,
                                                                                                  enteroGlobal))
else:
    print("el número no es entero")



## punto 3
print("Ingrese un numero para representarlo a offset binario")
entrada = input()
if "," not in entrada or "." not in entrada:
    # es entero
    enteroGlobal = int(entrada)
    entero = enteroGlobal #el entero normalito se modifica
    print("Ingrese el número de bits con los que quiere representar {}".format(entero))
    bits = int(input())
    bitsGlobal = bits #para guardar el valor y llamarlo más adelante, bits normalito se modifica
    binario = ""
    suficientesBits = True
    negativo = False
    if entero < 0:
        entero = abs(entero)
        negativo = True
    while bits >= 0:
        if bits == 0 and entero > 0:
            suficientesBits = False
            break
        if entero == 0:
            binario = str("0")*bits+binario #como binario es un string, simplemente toca multiplicar por 0s para rellenar
            break
        binario = str(entero % 2) + binario #como binario es un string, los nuevos caracteres se agregan a la izquierda
        bits-=1
        entero = entero // 2
    if suficientesBits:
        if negativo:
            #toca invertirlo
            complementoA1 = [abs(int(bit)-1) for bit in binario]# se crea una nueva lista invirtiendo cada bit
            #sumarle 1 al complemento a 1 para convertirlo a complemento a 2
            i = len(binario) - 1
            while True:
                if i < 0 :
                    if bitsGlobal > len(complementoA1):
                        complementoA1.insert(0, "1")  # toca hacerlo así porque va ser un string más grande
                        break
                if int(complementoA1[i]) + 1 == 2:  # si era uno
                    complementoA1[i] = "0"  # sigue haciendo el while
                    i -= 1
                else:  # si es cero
                    complementoA1[i] = "1"
                    break

            complementoA1[0] = str(abs(int(complementoA1[0]) - 1))  # se guarda como string pero se necesita invertir el último bit
            offset = "".join(complementoA1)  # para mostrarlo como un string


            print("el offset del entero {} con {} bits, es: {}".format(enteroGlobal,bitsGlobal,offset))
        else:
            if binario[0] == "1" and binario[1:] == str("0")*(bitsGlobal-1):#para el más grande
                print("{} bits no son suficientes para expresar el entero {} en offset".format(bitsGlobal, enteroGlobal))
            else:
                offsetList = [bit for bit in binario] #se convierte a una lista para poder cambiarle el primer número
                offsetList[0] = str(abs(int(binario[0]) -1))#se guarda como string pero se necesita invertir el último bit
                offset = "".join(offsetList)#para mostrarlo como un string
                print("el número {} en binario es: {}".format(enteroGlobal, offset))
    else:
        print("{} bits no son suficientes para expresar el entero {} en offset".format(bitsGlobal, enteroGlobal))
else:
    print("el número no es entero")
##punto 4 decimal con 32 bits
#1) primer bit para ver si es negativo o positivo
#2) los siguientes 8 bits representan el exponenete
#3) la matissa (23 bits) (dec/2^exp)-1
import math
print("ingrese un número decimal para mostrar su representación en punto flotante con 32 bits")
decimalG = float(input())
decimal = abs(decimalG)
bitsExponente = 8
bitsMantissa = 23
rango = 127
if -rango <= decimalG <= rango + 1:
    # 1) primer bit para ver si es negativo o positivo
    signo = "0"
    if decimalG < 0:
        signo = "1"
    # 2) los siguientes 8 bits representan el exponenete
    exponente = int(math.log(decimal,2)) # el ultimo exponente de 2 que divide al numero decimal
    offset = 127 + exponente
    #pasarlo a binario
    offsetBinario = ""

    while offset >= 1:
        offsetBinario += str(offset % 2)
        offset = offset // 2
        bitsExponente -= 1
    # 3) la matissa (23 bits) (dec/2^exp)-1
    decimal = -1 + decimal/(2**exponente)
    mantissa = ''
    for i in range(1,bitsMantissa + 1):
        if decimal >= 2 ** (-i):
            mantissa += "1"
            decimal = decimal - 2 ** (-i)
        else:
            mantissa += "0"
    print('en 32 bits, el decimal {} se representa como {} {} {} '.format(decimalG, signo,offsetBinario,mantissa))
else:
    print('el numero {} no puede ser representado con 32 bits'.format(decimal))


##punto 5 decimal con 64 bits
#1) primer bit para ver si es negativo o positivo
#2) los siguientes 11 bits representan el exponenete
#3) la mantissa (52 bits) (dec/2^exp)-1
import math
print("ingrese un número decimal para mostrar su representación en punto flotante con 32 bits")
decimalG = float(input())
decimal = abs(decimalG)
bitsExponente = 11
bitsMantissa = 52
rango = 127
if -rango <= decimalG <= rango + 1:
    # 1) primer bit para ver si es negativo o positivo
    signo = "0"
    if decimalG < 0:
        signo = "1"
    # 2) los siguientes bits representan el exponenete
    exponente = int(math.log(decimal,2)) # el ultimo exponente de 2 que divide al numero decimal
    offset = 127 + exponente
    #pasarlo a binario
    offsetBinario = ""

    while offset >= 1:
        offsetBinario += str(offset % 2)
        offset = offset // 2
        bitsExponente -= 1
    # 3) la matissa (23 bits) (dec/2^exp)-1
    decimal = -1 + decimal/(2**exponente)
    mantissa = ''
    for i in range(1,bitsMantissa + 1):
        if decimal >= 2 ** (-i):
            mantissa += "1"
            decimal = decimal - 2 ** (-i)
        else:
            mantissa += "0"
    print('en 32 bits, el decimal {} se representa como {} {} {} '.format(decimalG, signo,offsetBinario,mantissa))
else:
    print('el numero {} no puede ser representado con 32 bits'.format(decimal))


