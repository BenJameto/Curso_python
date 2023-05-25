from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('425x600')
ventana.resizable(False,False)
ventana.configure(background='gray')

#Display de los resultados
pantalla = Entry(ventana, font=('arial',20,'bold'), borderwidth=2)
pantalla.grid(row = 0, column = 0, columnspan = 3, pady= 10, padx=5)

##BOTONES###

#Boton AC
bootom_ac = Button(ventana, text='AC', width= 8, height=2, borderwidth=2, command= lambda:borrar())
bootom_ac.grid(row=0, column=3, pady=10, padx=5, columnspan=1)

#diseño de boton
ancho = 8
alto = 3

#Botones primera fila
boton1=Button(ventana, text='1',width=ancho, height=alto, command=lambda:click(1))
boton1.grid(row=1, column=0, padx=5, pady=5)

boton2=Button(ventana, text='2',width=ancho, height=alto, command=lambda:click(2))
boton2.grid(row=1, column=1, padx=5, pady=5)

boton3=Button(ventana, text='3',width=ancho, height=alto, command=lambda:click(3))
boton3.grid(row=1, column=2, padx=5, pady=5)

boton4=Button(ventana, text='4',width=ancho, height=alto, command=lambda:click(4))
boton4.grid(row=1, column=3, padx=5, pady=5)

#Botones 2 fila

boton5=Button(ventana, text='5',width=ancho, height=alto, command=lambda:click(5))
boton5.grid(row=2, column=0, padx=5, pady=5)

boton6=Button(ventana, text='6',width=ancho, height=alto, command=lambda:click(6))
boton6.grid(row=2, column=1, padx=5, pady=5)

boton7=Button(ventana, text='7',width=ancho, height=alto, command=lambda:click(7))
boton7.grid(row=2, column=2, padx=5, pady=5)

boton8=Button(ventana, text='8',width=ancho, height=alto, command=lambda:click(8))
boton8.grid(row=2, column=3, padx=5, pady=5)

#Botones fila 3

boton9=Button(ventana, text='9',width=ancho, height=alto, command=lambda:click(9))
boton9.grid(row=3, column=0, padx=5, pady=5)

boton0=Button(ventana, text='0',width=ancho, height=alto, command=lambda:click(0))
boton0.grid(row=3, column=1, padx=5, pady=5)

boton_punto=Button(ventana, text='.',width=ancho, height=alto, command=lambda:click('.'))
boton_punto.grid(row=3, column=2, padx=5, pady=5)

boton_suma=Button(ventana, text='+',width=ancho, height=alto, command=lambda:click('+'))
boton_suma.grid(row=3, column=3, padx=5, pady=5)

#Botones fila 4

boton_resta=Button(ventana, text='-',width=ancho, height=alto, command=lambda:click('-'))
boton_resta.grid(row=4, column=0, padx=5, pady=5)

boton_producto=Button(ventana, text='*',width=ancho, height=alto, command=lambda:click('*'))
boton_producto.grid(row=4, column=1, padx=5, pady=5)

boton_division=Button(ventana, text='/',width=ancho, height=alto, command=lambda:click('/'))
boton_division.grid(row=4, column=2, padx=5, pady=5)

boton_resultado=Button(ventana, text='=',width=ancho, height=alto, command = lambda:evaluar())
boton_resultado.grid(row=4, column=3, padx=5, pady=5)


#Funciones
operacion = ""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)

def click(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0, operacion)

def evaluar():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = "Error"
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0,resultado)


ventana.mainloop()