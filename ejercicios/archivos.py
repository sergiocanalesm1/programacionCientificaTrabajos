import numpy as np
import struct as st #para empaquetar y desempaquetar información binaria
import matplotlib.pyplot as p
'''
f = open("detexto.txt","w")
f.write("primera \nsegunda \ntercera ")
f.close()
f2=open("binario.txt","r")
linea = f2.readline()
while linea != "":
    print(linea)
    linea = f2.readline()
f2.close()
'''


arreglo = np.random.rand(100)*10
print(arreglo)
f = open("binario.bin","wb")
arreglo_binario = st.pack("d"*int(len(arreglo)),*arreglo) #https://docs.python.org/3/library/struct.html
f.write(arreglo_binario)
f.close()
r = open("binario.bin","rb")
archivo = r.read()
arreglo_leido = st.unpack("d"*int(len(archivo)/8),archivo)
print(arreglo_leido)
p.figure()
p.plot(arreglo_leido)
p.show()