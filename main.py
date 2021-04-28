#Importación de librerías y otros archivos
from datetime import datetime
from almacen import *
from balance import *
from Historial import *
from Datos import *
from ajustes import *
from Hoja_de_personalizacion import *
from tkinter import *

#Asígnamos el módulo datetime a dt para escribir menos xd 
dt = datetime.now()

#Crear ventana principal
main_window = tkinter.Tk()
main_window.geometry('900x700')
main_window.configure(bg = Color_de_fondo)
main_window.title('Inicio')

#Sección de textos sin interacción
Fecha = tkinter.Label(main_window, 
                      text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), 
                      bg = Color_de_fondo,
                      font = (Fuente_titulos, 10)).grid(column = 2)
label2 = tkinter.Label(main_window, text = 'Las nenis',
                       bg = Color_de_fondo, 
                       font = (Fuente_titulos, Tamaño_titulos)).grid(padx = espacio_lateral, pady = espacio_superior)

#Sección de botones
boton_almacen = tkinter.Button(main_window, 
                               text = ' Almacén ',
                               border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = Almacen, 
                               heigh = Altura_botones, 
                               width = Ancho_botones,
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_balance = tkinter.Button(main_window, text = ' Balance ',
                               border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command =ventana_balance,
                               heigh = Altura_botones, 
                               width = Ancho_botones,
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_historial = tkinter.Button(main_window, text = 'Historial',
                                 border = Tamaño_bordes, 
                                 bg = Color_de_botones, 
                                 command = Ventana_Historial, 
                                 heigh = Altura_botones, 
                                 width = Ancho_botones,
                                 activebackground = botones_activos,
                                 cursor = Figura,
                                 relief = Tipo_borde,
                                 font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_datos = tkinter.Button(main_window, text = '  Datos  ',
                             border = Tamaño_bordes,
                             bg = Color_de_botones, 
                             command = Ventana_datos, 
                             heigh = Altura_botones, 
                             width = Ancho_botones,
                             activebackground = botones_activos,
                             cursor = Figura,
                             relief = Tipo_borde,
                             font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_ajustes = tkinter.Button(main_window, text = ' Ajustes ',
                               bg = Color_de_botones,
                               border = Tamaño_bordes, 
                               command = ventana_ajustes , 
                               heigh = Altura_botones, 
                               width = Ancho_botones,
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
boton_salir = tkinter.Button(main_window, text = '  Salir  ', 
                             bg = Color_de_botones,
                             border = Tamaño_bordes,
                             command = main_window.destroy, 
                             heigh = Altura_botones, 
                             width = Ancho_botones,
                             activebackground = botones_activos,
                             cursor = Figura,
                             relief = Tipo_borde,
                             font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)


#Lo hacemos un bucle infinito para que no se cierre
tkinter.mainloop()