##
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

##
print("Ingrese un numero para convertirlo a complemento a 2")
entrada = input()
if "," not in entrada or "." not in entrada:
    enteroGlobal = int(entrada)
    entero = enteroGlobal #para guardar el valor y llamarlo más adelante, el entero normalito se modifica
    print("Ingrese el número de bits con los que quiere representar {}".format(entero))
    bits = int(input())
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
        binario = str(entero % 2) + binario #como binario es un string, los nuevos caracteres se agregan a la izquierda
        bits-=1
        entero = entero // 2
    if suficientesBits:
        print("el número {} en binario es: {}".format(enteroGlobal,binario))
        ##toca invertirlo
        ##sumarle 1
        #print(enteroGlobal == binario_a_decimal(binario))#para verificar
    else:
        print("{} bits no son suficientes para expresar el entero {}".format(bitsGlobal, enteroGlobal))
else:
    print("el número no es entero")
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

