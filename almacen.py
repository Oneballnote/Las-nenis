from tkinter import *
import tkinter
from Hoja_de_personalizacion import *
from datetime import datetime
import pandas as pd
dt = datetime.now()

def Almacen():
    
    #Personalización de la ventana
    main_window = tkinter.Tk()
    main_window.geometry('600x500')
    main_window.configure(bg = Color_de_fondo)
    main_window.title('Almacen')
    
    #Textos
    nombre = tkinter.Label(main_window, 
                           text = 'Almacen',
                           bg = Color_de_fondo,
                           font = (Fuente_titulos, Tamaño_titulos)).grid(row = 1, column = 2, padx = 50, pady = 10)


    almacen = pd.read_csv("Inventario.csv")
    producto_tipo = tkinter.Label(main_window, 
                             text = almacen,
                             bg = Color_de_fondo,
                             font = (Fuente_titulos, Tamaño_subtitulos + 2)).grid(row = 2,column = 2, padx = 50, pady =10)
    volver = tkinter.Button(main_window, 
                            text = 'volver',
                            border = Tamaño_bordes,
                            bg = Color_de_botones, 
                            command = main_window.destroy,
                            heigh = altura_botones, 
                            width = ancho_botones,
                            activebackground = botones_activos,
                            cursor = Figura,
                            relief = Tipo_borde,
                            font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 5, column = 2, padx = 55, pady = Espacio_botones + 5)
    
    tkinter.mainloop()