import numpy as np
import matplotlib.pyplot as p
import struct as st

def nueve():
    arreglo = np.random.randint(-10,10,1000)
    print(arreglo)
    name = "FileBinInt16.bin"
    format = "h"
    f = open(name,"wb")
    paquete = st.pack(format*len(arreglo),*arreglo)
    f.write(paquete)
    inversaArchivo(name,format,2)

def inversaArchivo(name,format,divide):
    f = open(name,"rb")
    file = f.read()
    paquete = st.unpack(format*int(len(file)/divide),file)
    print(paquete)

def trece():
    f = open("File-214.bin","rb")
    file = f.read()
    arreglo_leido = st.unpack("I" * int(len(file) / 4),file)
    print(np.mean(arreglo_leido))


