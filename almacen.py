#Importación de librerías y archivos
from tkinter import *
import tkinter
from Hoja_de_personalizacion import *
from datetime import datetime
import pandas as pd

almacen = pd.read_csv("Inventario.csv") #Extraemos el inventario del archivo indicado y lo asignamos a almacen

def Almacen():
    
    #Personalización de la ventana
    VentanadeAlmacen = tkinter.Tk() #Crea una ventana y la asigna a VentanadeAlamacén
    VentanadeAlmacen.geometry('600x500') #Especifica el tamaño de la ventana
    VentanadeAlmacen.configure(bg = Color_de_fondo) #Especifica el color de fondo
    VentanadeAlmacen.title('Almacen') #Indica el nombre de la ventana, el cual aparece en la barra superior
    
    
    #Textos
    nombre = tkinter.Label(VentanadeAlmacen, 
                           text = 'Almacen',
                           bg = Color_de_fondo,
                           font = (Fuente_titulos, Tamaño_titulos)).grid(row = 1, column = 2, padx = 50, pady = 10)
    producto_tipo = tkinter.Label(VentanadeAlmacen, 
                             text = almacen,
                             bg = Color_de_fondo,
                             font = (Fuente_titulos, Tamaño_subtitulos + 2)).grid(row = 2,column = 2, padx = 50, pady =10) #imprime la variable almacén
    
    #Botones
    volver = tkinter.Button(VentanadeAlmacen, 
                            text = 'volver',
                            border = Tamaño_bordes,
                            bg = Color_de_botones, 
                            command = VentanadeAlmacen.destroy,
                            heigh = altura_botones, 
                            width = ancho_botones,
                            activebackground = botones_activos,
                            cursor = Figura,
                            font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 5, column = 2, padx = 55, pady = Espacio_botones + 5) #Crea un botón que cierra esta ventana
    
    tkinter.mainloop() #Crea un bucle para que no se cierre la ventana
    