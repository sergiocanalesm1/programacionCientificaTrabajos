import numpy as np
import struct as st

f = open("averagebin1.bin","rb")
archivo = f.read()
paquete = st.unpack("f"*int(len(archivo)/4),archivo)
media = np.mean(paquete)

print(" {} {} {} ".format(paquete[2], paquete[21],paquete[43]))

