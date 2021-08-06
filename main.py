# Programa que calcule la derivada y la integral de una función
from sympy import *
import sympy
from sympy.parsing.sympy_parser import parse_expr # Leer función introducida
from tkinter import *

from sympy.plotting import plot3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from sympy.printing.tree import tree

def verificar_variables(variable):
    x = false
    y = false
    z = false
    if variable == '':
        print('sin variable especificada')
        return false
    print('verificando')
    if 'x' in variable:
        x =true
    if 'y' in variable:
        y = true
    if 'z'in variable:
        z = true
    
    ar=[]
    if x:
        if y:
            ###
            #if z:
            #    ar.append(7)
            #    ar.append('x')
            #    ar.append('y')
            #    ar.append('z')
            ###
            ar.append(4)
            ar.append('x')
            ar.append('y')
        elif z:
            ar.append(5)
            ar.append('x')
            ar.append('z')
        ar.append(1)
        ar.append('x')
    elif y:
        if z:
            ar.append(6)
            ar.append('y')
            ar.append('z')
        ar.append(2)
        ar.append('y')
    else:
        ar.append(3)
        ar.append('z')
    print('verificacion hecha')
    return ar

        
def derivada():
    try:

        #x = symbols('x') #Declarar variable independiente
        #y = symbols('y')
        #z = symbols('z')

        condicion = variables.get()
        re = verificar_variables(condicion)

        if re == false:
            anuncio3.configure(text="variable no especificada X", fg="red")
        else:
            anuncio3.configure(text="variable especificada ✔", fg="green")

        fun_escrita = funcion.get()

        if fun_escrita == '':
            anuncio4.configure(text="funcion no especificada X", fg="red")
        else:
            anuncio4.configure(text="funcion especificada ✔", fg="green")

        f = parse_expr(fun_escrita)
        a=symbols('x')
        if re[0] <=3:
            if re[1] == 'x':
                a=symbols('x')
            elif re[1] == 'y':
                a=symbols('y')
            else:
                a=symbols('z')
            print('derivada lista')
            derivada = diff(f,a)
            etiqueta.configure(text=derivada)
        else:
            if re[1] == 'x':
                if re[2]=='y':
                    a=symbols('x')
                    b=symbols('y')
                else:
                    a=symbols('x')
                    b=symbols('z')
            elif re[1] == 'y':
                a = symbols('y')
                b = symbols('z')
            derivada1 = diff(f,a)
            derivada2 = diff(f,b)
            derivada3 = diff(f,a,a)
            derivada4 = diff(f,b,b)
            derivada5 = diff(f,a,b)
            derivada6 = diff(f,b,a)
            print('derivadas listas')
            etiqueta2.configure(text=derivada1)
            etiqueta3.configure(text=derivada2)
            etiqueta4.configure(text=derivada3)
            etiqueta5.configure(text=derivada4)
            etiqueta6.configure(text=derivada5)
            etiqueta7.configure(text=derivada6)
    except:
        etiqueta.configure(text="Error: Introduce las variables o función correctamente")
        



'''
def integral():
    try:
        x = symbols('x') #Declarar variable independiente
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
'''
def graficar():
    x = symbols('x') #Declarar variable independiente
    y = symbols('y')
    z = symbols('z')
    fun_escrita = funcion.get()
    if fun_escrita == '':
        anuncio5.configure(text="funcion no especificada X", fg="red")
    else:
        anuncio5.configure(text="funcion especificada ✔", fg="green")
    f = parse_expr(fun_escrita)
    plot3d(f, (x, -100,100), (y, -100,100), (z, -100,100))

ventana = Tk()
ventana.geometry('902x526')

bg = PhotoImage(file = 'E:/PYTHON DATE/Prueba_calculadora/Fondo.png')
label1 = Label(ventana, image=bg)
label1.place(x=0, y=0)

ventana.title("Proyecto Final - Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una F():", font=("Arial", 15), fg="blue")
anuncio.pack()

variables = Entry(ventana, font=("Arial", 15))
variables.pack()

anuncio3 = Label(ventana, text="Antecedentes:", font=("Arial", 15), fg="blue")
anuncio3.pack()

anuncio1 = Label(ventana, text="Introduce una función:", font=("Arial", 15), fg="blue")
anuncio1.pack()
funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()

anuncio4 = Label(ventana, text="Antecedentes:", font=("Arial", 15), fg="blue")
anuncio4.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

etiqueta2 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta2.pack()
etiqueta3 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta3.pack()
etiqueta4 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta4.pack()
etiqueta5 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta5.pack()
etiqueta6 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta6.pack()
etiqueta7 = Label(ventana, text="Resultados", font=("Arial", 15), fg="red")
etiqueta7.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=derivada)
boton1.pack()

boton4 = Button(ventana, text="Gráfico de la función", font=("Arial", 15), command=graficar, width=22)
boton4.pack(pady=(5,0))
anuncio5 = Label(ventana, text="Antecedentes del grafico:", font=("Arial", 15), fg="blue")
anuncio5.pack()

#boton2 = Button(ventana, text="Integrar Función", font=("Arial", 15), command=integral)
#boton2.pack()

def _quit(): #Función salir
    ventana.quit()     # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria
                    

button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button3.pack()

ventana.mainloop()