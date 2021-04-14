#Importación de librerías y otros archivos
from datetime import datetime
from almacen import Almacen
from balance import ventana_balance
from Historial import Ventana_Historial
from Datos import Ventana_datos
from ajustes import ventana_ajustes
import tkinter

#Asígnamos el módulo datetime a dt para escribir menos xd 
dt = datetime.now()





#Crear ventana principal
main_window = tkinter.Tk()
main_window.geometry('600x500')
main_window.configure(bg = '#6990D8')



#Sección de textos sin interacción
Fecha = tkinter.Label(main_window, text = '{}/{}/{}'.format(dt.day, dt.month, dt.year), bg = '#6990D8').grid(row = 0, column = 3)
vacio = tkinter.Label(main_window,bg = '#6990D8').grid(row = 2, column = 2)
label2 = tkinter.Label(main_window, text = 'Las nenis', bg = '#6990D8').grid(row = 3,column = 2)
spacer = tkinter.Label(main_window, text = '     ',bg = '#6990D8').grid(row = 3,column = 1)

#Sección de botones
boton_almacen = tkinter.Button(main_window, text = ' Almacén ',border = 0,bg = '#89AAE6', command = Almacen).grid(row = 4,column = 2)
boton_balance = tkinter.Button(main_window, text = ' Balance ',border = 0,bg = '#89AAE6', command =ventana_balance ).grid(row = 5,column = 2)
boton_historial = tkinter.Button(main_window, text = 'Historial',border = 0,bg = '#89AAE6', command = Ventana_Historial).grid(row = 6,column = 2)
boton_datos = tkinter.Button(main_window, text = '  Datos  ',border = 0,bg = '#89AAE6', command = Ventana_datos).grid(row = 7,column = 2)
boton_ajustes = tkinter.Button(main_window, text = ' Ajustes ',bg = '#89AAE6',border = 0, command = ventana_ajustes ).grid(row = 8,column = 2)
boton_salir = tkinter.Button(main_window, text = '  Salir  ', bg = '#89AAE6',border = 0,command = main_window.destroy).grid(row = 9,column = 2)

#Empaquetamos cada uno de loswidgets anteriores para que se puedan usar


#Lo hacemos un bucle infinito para que no se cierre
tkinter.mainloop()


 
