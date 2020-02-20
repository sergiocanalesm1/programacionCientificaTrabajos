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

print("ingrese un número decimal para mostrar su representación en binario con 32 bits")
decimal = float(input())
binario = "0"
#1) primer bit para ver si es negativo o positivo
if decimal < 0:
    binario = "1"
#2) los siguientes 8 bits representan el exponenete
bits = 8


##
def decimal_a_binario(entero,bits):
    enteroGlobal = entero #para guardar el valor y llamarlo más adelante, el entero normalito se modifica
    bitsGlobal = bits #para guardar el valor y llamarlo más adelante, bits normalito se modifica
    binario = ""
    suficientesBits = True
    while bits >= 0:
        if bits == 0 and entero > 0:
            suficientesBits = False
            break
        if entero == 0:
            binario = str("0")*bits+binario #como binario es un string, simplemente toca multiplicar por 0s para rellenar
            break
        binario += str(entero % 2) #como binario es un string, los nuevos caracteres se agregan a la izquierda
        bits-=1
        entero = entero // 2
    if suficientesBits:
        return binario
        #print(enteroGlobal == binario_a_decimal(binario))#para verificar
    else:
        print("{} bits no son suficientes para expresar el entero {}".format(bitsGlobal, enteroGlobal))
        return None

def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)-1,-1,-1):
        posBin = int(binario[i])
        exp = len(binario)-i-1
        decimal += posBin*2**exp
    return(decimal)
def entero_a_complemento2():
    print("ingrese un entero para representarlo binariamente en complemente a 2")
    entero = int(input())
    print("ingrese el número de bits con los que quiere representar {}".format(entero))
    bits = int(input())
    if entero > 0:
        print(sumar1bit(decimal_a_binario(entero,bits)))

def sumar1bit(binario,bits):
    tocaSumar = True #booleano para verificar si ya puede parar de sumar
    i = len(binario)-1
    listaBinarios = list(binario)#se pasa a una lista para poder asignar
    while True:
        if i < 0 and bits > len(binario):
            listaBinarios.insert(0,"1") # toca hacerlo así porque va ser un string más grande
            break
        if int(binario[i]) + 1 == 2:#si era uno
            listaBinarios[i] =  "0" #sigue haciendo el while
            i -= 1
        else:#si es cero
                listaBinarios[i] = "1"
                break
    return "".join(listaBinarios)#devuelve un string
##
import math


x = math.pi
decimalGlobal = (x/2**1)-1
mantissa = ""


def bin_a_flotante(binario):
    listBin = [int(x) for x in binario]
    listBin.reverse()
    dec = 0.0
    exponente = 1
    for bit in listBin:
        dec += bit*(2**-exponente)
        exponente += 1
    return dec

decimal = decimalGlobal
for i in range(1,53):
    #print("---")

    if decimal >= 2**(-i):
        mantissa = "1" + mantissa
        decimal = decimal - 2**(-i)
    else:
        mantissa = "0" + mantissa
    #print("decimal entrante: {} decimal que sale:{} a potencia de 2: {} mantissa: {}".format(y,decimal,2**-i,mantissa[-i]))
    #print("aaaaaa")

print(decimalGlobal)
print(bin_a_flotante(mantissa) == decimalGlobal)