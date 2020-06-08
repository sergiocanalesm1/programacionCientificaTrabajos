import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib import style
from PIL import ImageTk, Image
import logica
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

root = Tk()
root.title('Lectura de ECG')
## Frame parametros
Parametros = LabelFrame(root, padx=50, pady=50, bg='snow')
Parametros.grid(row=0, column=0, rowspan=3)
Parametros.place(x=0, y=0)

titulop = Label(Parametros, text='Parámetros', font=('Comic Sans MS', 15, 'bold italic'), bg='snow')
titulop.grid(row=0, column=0, columnspan=2)
frecuencia = Label(Parametros, text='Frecuencia cardíaca', bg='snow')
frecuencia.grid(row=4, column=0)
e_frecuencia = Entry(Parametros, width=25, borderwidth=5)
e_frecuencia.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
e_frecuencia.insert(0, 80)
fc = int(e_frecuencia.get())

latidos = Label(Parametros, text='Número de Latidos', bg='snow')
latidos.grid(row=1, column=0)
e_latidos = Entry(Parametros, width=25, borderwidth=5)
e_latidos.grid(row=1, column=1, columnspan=1, padx=10, pady=10)
e_latidos.insert(0, 10)
lat = int(e_latidos.get())

frecuenciaMuestreo = Label(Parametros, text='Frecuencia Muestreo', bg='snow')
frecuenciaMuestreo.grid(row=2, column=0)
e_frecuenciaM = Entry(Parametros, width=25, borderwidth=5)
e_frecuenciaM.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
e_frecuenciaM.insert(0, 360)
fm = int(e_frecuenciaM.get())

factor = Label(Parametros, text='Factor de Ruido', bg='snow')
factor.grid(row=3, column=0)
e_factor = Entry(Parametros, width=25, borderwidth=5)
e_factor.grid(row=3, column=1, columnspan=1, padx=10, pady=10)

## Frame Metodo de solucion

metodo = LabelFrame(root, padx=80, pady=60, bg='snow')
metodo.grid(row=4, column=0, rowspan=3, columnspan=1)

titulomds = Label(metodo, text='Método de Solución', font=('Comic Sans MS', 15, 'bold italic'), bg='snow')
titulomds.grid(row=0, column=0, pady=10)


def clicekd(value):
    global nombre_metodo
    nombre_metodo = value


r = StringVar()
r.set(NONE)

ead = Radiobutton(metodo, text='Euler Adelante', variable=r, bg='snow', value='Euler Adelante', command=lambda: clicekd(r.get()))
ead.grid(row=1, column=0, pady=6)

eat = Radiobutton(metodo, text='Euler Atrás', variable=r, bg='snow', value='Euler Atras', command=lambda: clicekd(r.get()))
eat.grid(row=2, column=0, pady=6)

em = Radiobutton(metodo, text='Euler Modificado', variable=r, bg='snow', value='Euler Modificado', command=lambda: clicekd(r.get()))
em.grid(row=3, column=0, pady=6)

rk2 = Radiobutton(metodo, text='Runge-Kutta 2', variable=r, bg='snow', value='Runge-Kutta 2', command=lambda: clicekd(r.get()))
rk2.config(state=DISABLED)
rk2.grid(row=4, column=0, pady=6)

rk4 = Radiobutton(metodo, text='Runge-Kutta 4', variable=r, bg='snow', value='Runge-Kutta 4', command=lambda: clicekd(r.get()))
rk4.config(state=DISABLED)
rk4.grid(row=5, column=0, pady=6)


## Parte derecha
frame = LabelFrame(root, padx=80, pady=10, bg='snow')
frame.grid(row=0, column=1, rowspan=7)


def CerrarAplicacion():
    MsgBox = messagebox.askquestion('Cerrar Aplicación', '¿Está seguro que desea cerrar la aplicación?', icon='warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tkinter.messagebox.showinfo('Retornar', 'Será retornado a la aplicación')


Boton2 = Button(frame, text="x", command=CerrarAplicacion, bg='red', font=15)
Boton2.grid(row=0, column=6, padx=10)


def exportar():
    logica.exportar(z, t, fc, lat, fm, '')


exportarDatos = Button(frame, text='Exportar datos', command=exportar, state=DISABLED)
exportarDatos.grid(row=0, column=0, padx=10, pady=0, columnspan=3)


def cargar():
    global nombre_metodo, z, t, fc, lat, fm
    z, t, fc, lat, fm = logica.cargar()
    nombre_metodo = 'Cargar'
    return z, t


ccargarDatos = Button(frame, text='Cargar datos', command=cargar)
ccargarDatos.grid(row=0, column=4, padx=10, pady=10, columnspan=2)
# Titulo señal de ECG

señal = Label(frame, text='Señal de ECG', font=('Comic Sans MS', 20, 'bold italic'), bg='snow')
señal.grid(row=1, column=1, padx=10, columnspan=6)
figure = plt.Figure(figsize=(5, 4), dpi=80)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, frame)
chart_type.get_tk_widget().grid(row=3, column=1, columnspan=6)


def hallarR():
    e_hallar.delete(0, END)
    hr = logica.hallarHR(ecg=z, fs=fm)
    e_hallar.insert(0, hr)


hallar = Button(frame, text='Hallar HR', state=DISABLED, command=hallarR)
hallar.grid(row=4, column=1, padx=1, pady=10, columnspan=3)

e_hallar = Entry(frame, width=15, borderwidth=5)
e_hallar.grid(row=4, column=4, columnspan=3, padx=1, pady=10)


inputs = Label(frame, text='     P    Q    R     S    T ', font=('Comic Sans MS', 20, 'bold italic'), bg='magenta')
inputs.grid(row=5, column=0, columnspan=6)

ai = Label(frame, text='Ai', font=('Comic Sans MS', 15, 'bold italic'), bg='snow')
ai.grid(row=6, column=0)

bi = Label(frame, text='Bi', font=('Comic Sans MS', 15, 'bold italic'), bg='snow')
bi.grid(row=7, column=0)

e_1 = Entry(frame, width=5, borderwidth=5)
e_1.grid(row=6, column=1, padx=1)
e_1.insert(0, 1.2)
aiP = float(e_1.get())


e_2 = Entry(frame, width=5, borderwidth=5)
e_2.grid(row=6, column=2, padx=1)
e_2.insert(0, -5)
aiQ = float(e_2.get())

e_3 = Entry(frame, width=5, borderwidth=5)
e_3.grid(row=6, column=3, padx=1)
e_3.insert(0, 30)
aiR = float(e_3.get())

e_4 = Entry(frame, width=5, borderwidth=5)
e_4.grid(row=6, column=4, padx=1)
e_4.insert(0, -7.5)
aiS = float(e_4.get())

e_5 = Entry(frame, width=5, borderwidth=5)
e_5.grid(row=6, column=5, padx=1)
e_5.insert(0, 0.75)
aiT = float(e_5.get())

e_6 = Entry(frame, width=5, borderwidth=5)
e_6.grid(row=7, column=1, padx=1)
e_6.insert(0, 0.25)
biP = float(e_6.get())

e_7 = Entry(frame, width=5, borderwidth=5)
e_7.grid(row=7, column=2, padx=1)
e_7.insert(0, 0.1)
biQ = float(e_7.get())

e_8 = Entry(frame, width=5, borderwidth=5)
e_8.grid(row=7, column=3, padx=1)
e_8.insert(0, 0.1)
biR = float(e_8.get())

e_9 = Entry(frame, width=5, borderwidth=5)
e_9.grid(row=7, column=4, padx=1)
e_9.insert(0, 0.1)
biS = float(e_9.get())

e_10 = Entry(frame, width=5, borderwidth=5)
e_10.grid(row=7, column=5, padx=1)
e_10.insert(0, 0.4)
biT = float(e_10.get())

a = [aiP, aiQ, aiR, aiS, aiT]
b = [biP, biQ, biR, biS, biT]


def actualizar(fc, lat, fm, a, b, nombre_metodo):
    global z, t
    z = 0
    t = []
    if nombre_metodo == 'Euler Adelante':
        z, t = logica.eulerForward(FC=fc, Tf=lat, fs=fm, a=a, b=b)
        hallar.config(state='normal')
        exportarDatos.config(state='normal')
    elif nombre_metodo == 'Euler Atras':
        z, t = logica.eulerBack(FC=fc, Tf=lat, fs=fm, a=a, b=b)
        hallar.config(state='normal')
        exportarDatos.config(state='normal')
    elif nombre_metodo == 'Euler Modificado':
        z, t = logica.eulerMod(FC=fc, Tf=lat, fs=fm, a=a, b=b)
        hallar.config(state='normal')
        exportarDatos.config(state='normal')
    elif nombre_metodo == 'Cargar':
        z, t = cargar()
        z = np.array(z)
        hallar.configure(state="normal")
        e_hallar.delete(0, END)
        r.set(None)
        exportarDatos.config(state='normal')
    figure = Figure(figsize=(5, 4), dpi=80)
    g = figure.add_subplot(111)
    g.plot(t, z)
    g.set_xlabel("Latidos", fontsize=14)
    canvas = FigureCanvasTkAgg(figure, frame)
    canvas.get_tk_widget().grid(row=3, column=1, columnspan=6)
    e_hallar.delete(0, END)


boton_act = Button(frame, text='Actualizar Gráfica', command = lambda: actualizar(fc, lat, fm, a, b, nombre_metodo))
boton_act.grid(row=9, column=1, columnspan=7, pady=20)


root.mainloop()