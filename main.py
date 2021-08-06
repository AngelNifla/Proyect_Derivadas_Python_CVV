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
            etiqueta2.configure(text=derivada)
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
        etiqueta2.configure(text="Error: Introduce las variables o función correctamente")
        



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
ventana.geometry('1200x600')

bg = PhotoImage(file = 'E:/PYTHON DATE/Nueva carpeta/Fondo.png')
label1 = Label(ventana, image=bg)
label1.place(x=0, y=0)

ventana.title("Proyecto Final - Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una F():", font=("Corbel", 15), fg="black", width=23)
anuncio.place(x=50, y=30)

variables = Entry(ventana, font=("Corbel", 15), width=23)
variables.place(x=320, y=30)

anuncio3 = Label(ventana, text="Antecedentes:", font=("Corbel", 15), fg="blue", width=23)
anuncio3.place(x=190, y=70)



anuncio1 = Label(ventana, text="Introduce una función:", font=("Corbel", 15), fg="black", width=22)
anuncio1.place(x=600, y=30)
funcion = Entry(ventana, font=("Corbel", 15), width=22)
funcion.place(x=870, y=30)
anuncio4 = Label(ventana, text="Antecedentes:", font=("Corbel", 15), fg="blue", width=22)
anuncio4.place(x=740, y=70)
'''
etiqueta = Label(ventana, text="Resultado", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta.place(x=70, y=190)
'''
etiqueta0_2 = Label(ventana, text="Derivada DF/Da :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_2.place(x=70, y=200)
etiqueta2 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta2.place(x=100, y=240)
etiqueta0_4 = Label(ventana, text="Derivada DF/Daa :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_4.place(x=70, y=300)
etiqueta4 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta4.place(x=100, y=340)
etiqueta0_5 = Label(ventana, text="Derivada DF/Dab :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_5.place(x=70, y=400)
etiqueta6 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta6.place(x=100, y=440)


etiqueta0_3 = Label(ventana, text="Derivada DF/Db :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_3.place(x=770, y=200)
etiqueta3 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta3.place(x=800, y=240)
etiqueta0_5 = Label(ventana, text="Derivada DF/Dbb :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_5.place(x=770, y=300)
etiqueta5 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta5.place(x=800, y=340)
etiqueta0_5 = Label(ventana, text="Derivada DF/Dba :", font=("Corbel", 15), fg="red", bg='white')
etiqueta0_5.place(x=770, y=400)
etiqueta7 = Label(ventana, text="Resultados", font=("Corbel", 15), fg="white", bg='#000000')
etiqueta7.place(x=800, y=440)

boton1 = Button(ventana, text="Derivar Función", font=("Corbel", 15), command=derivada, width=22, background="CadetBlue")
boton1.place(x=30, y=520)

boton4 = Button(ventana, text="Gráfico de la función", font=("Corbel", 15), command=graficar, width=22, background="CadetBlue")
boton4.place(x=470,y=490)
anuncio5 = Label(ventana, text="Antecedentes del grafico:", font=("Corbel", 15), fg="blue", width=22)
anuncio5.place(x=472,y=535)

#boton2 = Button(ventana, text="Integrar Función", font=("Corbel", 15), command=integral)
#boton2.pack()

def _quit(): #Función salir
    ventana.quit()     # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria
                    

button3 = Button(master=ventana, text="Salir", font=("Corbel", 15), command=_quit, width=22, background="CadetBlue")
button3.place(x=910, y=520)

ventana.mainloop()