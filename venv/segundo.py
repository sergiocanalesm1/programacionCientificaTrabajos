def decimal_a_binario():
    print("Ingrese un numero decimal para convertirlo a binario")
    entero = int(input())
    enteroGlobal = entero #para guardar el valor y llamarlo más adelante, el entero normalito se modifica
    print("Ingrese el número de bits con los que quiere representar {}".format(entero))
    bits = int(input())
    bitsGlobal = bits #para guardar el valor y llamarlo más adelante, bits normalito se modifica
    binario = ""
    suficientesBits = True
    if entero < 0 :
        print("no se pueden números negativos")
        return #se sale de la FUNCION
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
        print(binario)
        print(enteroGlobal == binario_a_decimal(binario))#para verificar
    else:
        print("{} bits no son suficientes para expresar el entero {}".format(bitsGlobal, enteroGlobal))

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
    losQueLlevo = 0
    while True:
        if i < 0 and bits > len(binario):
            binario = 1 + binario # toca hacerlo así porque va ser un string más grande
            return binario
        if binario[i] + 1 == 2:#si era uno
            binario[i] =  0
        elif binario[i] +1 == 1:
                binario[i] = 1
                return binario
        else:
            return binario#si no es 2 ya acabó
        i -= 1