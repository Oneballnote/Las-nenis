import tkinter.font
from Hoja_de_personalizacion import *
from datetime import datetime
import pandas as pd
import io

#Trabajo con archivos
Archivo_productos = open('productos.txt', 'r')
Tipo_productos = Archivo_productos.readline()
Archivo_productos.close()

Archivo_costos = open('costo.txt', 'r')
costos_productos = Archivo_costos.readline()
Archivo_costos.close()

Archivo_Precio = open('Precio.txt', 'r')
Precio_productos = Archivo_Precio.readline()
Archivo_Precio.close()

#Trabajo con listas
Tipo_productos = Tipo_productos.split(',')
Tipo_productos.remove('')
costos_productos = costos_productos.split(',')
costos_productos.remove('')
Precio_productos = Precio_productos.split(',')
Precio_productos.remove('')
#Convierte las cadenas de la lista a enteros
for m in range(len(Tipo_productos)):
    Tipo_productos[m] = Tipo_productos[m].lower()
for i in range(len(costos_productos)):
    costos_productos[i] = int(costos_productos[i])
    
for j in range(len(Precio_productos)):
    Precio_productos[j] = int(Precio_productos[j])

#asignación de precios
if Tipo_productos[0] == 'bolis':
    preciobolis = Precio_productos[0]
    costobolis = Precio_productos[1]*(-1)
    preciobotana = costos_productos[0]
    costobotana = costos_productos[1]*(-1)
    
elif Tipo_productos[0] == 'botana':
    preciobolis = Precio_productos[1]
    costobolis = Precio_productos[0]*(-1)
    preciobotana = costos_productos[1]
    costobotana = costos_productos[0]*(-1)
    
def ventana_balance():
    
    
    VentanadeBalance = tkinter.Tk() #Crea una ventana y la asigna a VentanadeBalance
    VentanadeBalance.geometry('670x340') #Especifica las medidas de la ventana 
    VentanadeBalance.configure(bg = Color_de_fondo) #Especifica el color de fondo de la ventana
    VentanadeBalance.title('Registro') #Especifica el titulo de la ventana
    
    def Registro_de_Ventas():
        
        a = entrada_articulo_venta.get().lower()
        sabor = entrada_tipo_venta.get().lower()
        cantidad = entrada_cantidad_venta.get()
        cantidad = int(cantidad)
        
        #REGISTRAR VENTA 
        fechadia = datetime.now()
        fecharegistro = fechadia.date()

    #lectura de df's de historial e inventario
        if a == "bolis":
            ralmacen = pd.read_csv("Inventario.csv")
            rregistrobolis = pd.read_csv("lolo.csv")
            filas = len(rregistrobolis.index)
            
    #agregar registro al historial
            rregistrobolis.loc[filas] = [fecharegistro.strftime("%d/%m/%Y"),"Venta",cantidad,cantidad*preciobolis]
            
    #modificar los bolis vendidos en el inventario
            renglon = ralmacen[ralmacen["Sabor"] == sabor.capitalize()]
            renglon["Cantidad"] = renglon["Cantidad"] - cantidad
            ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
            
    #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.index = ralmacen['Tipo']
            ralmacen.drop('Tipo', axis = 1, inplace = True)
            ralmacen.to_csv("Inventario.csv")
            rregistrobolis.index = rregistrobolis['Fecha']
            rregistrobolis.drop('Fecha', axis = 1, inplace = True)
            rregistrobolis.to_csv("lolo.csv")
    
        elif a == "botanas":
            ralmacen = pd.read_csv("Inventario.csv")
            rregistrobotanas = pd.read_csv("registro botanas.csv")
            filas = len(rregistrobotanas.index)
    #agregar registro al historial
            rregistrobotanas.loc[filas] = [fecharegistro.strftime("%d/%m/%Y"),"Venta",cantidad,cantidad*preciobotanas]
    #modificar las botanas vendidas en el inventario
            renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
            renglon["Cantidad"] = renglon["Cantidad"] - cantidad
            ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
    #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.index = ralmacen['Tipo']
            ralmacen.drop('Tipo', axis = 1, inplace = True)
            ralmacen.to_csv("Inventario.csv")
            rregistrobotanas.index = rregistrobotanas['Fecha']
            rregistrobotanas.drop('Fecha', axis = 1, inplace = True)
            rregistrobotanas.to_csv("registro botanas.csv")
       
    def Registro_de_Compras():
        a = entrada_articulo_compra.get().lower()
        sabor = entrada_tipo_compra.get().lower()
        cantidad = entrada_cantidad_compra.get()
        cantidad = int(cantidad)
        
        #En BALANCE
        #REGISTRAR COMPRA/CARGA
        fechadia = datetime.now()
        fecharegistro =fechadia.date()

        #lectura de df's de historial e inventario
        if a == "bolis":
            ralmacen = pd.read_csv("Inventario.csv")
            rregistrobolis = pd.read_csv("lolo.csv")
            filas = len(rregistrobolis.index)
        #agregar registro al historial
            #nuevoregistro = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobolis]
            rregistrobolis.loc[filas] = [fecharegistro.strftime("%d/%m/%Y"),"Carga",cantidad,cantidad*costobolis]
        #modificar los bolis vendidos en el inventario
            filas2 = len(ralmacen.index)
        #buscamos fila por fila si el sabor que compramos ya estába en el inventario
            for i in range(filas2):
                if ralmacen.at[i,"Sabor"]==sabor.capitalize():        
        #Si el sabor ya estaba entonces al renglón de ese sabor le modificamos la cantidad
                    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
                    renglon["Cantidad"] = renglon["Cantidad"] + cantidad
                    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
                    renglon = 1
                    break
        #Si en ningún renglón encontramos el sabor entonces...
                else:
                    renglon=0
        #Si no se encontró el sabor en el inventario significa que cargamos uno nuevo, por lo que agregamos un nuevo campo
            if renglon==0:
                ralmacen.loc[filas2] = [a.capitalize(),sabor.capitalize(),cantidad]        
        #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.index = ralmacen["Tipo"]
            ralmacen.drop('Tipo', axis = 1, inplace = True)
            ralmacen.to_csv("Inventario.csv")
            rregistrobolis.index = rregistrobolis["Fecha"]
            rregistrobolis.drop("Fecha", axis = 1, inplace = True)
            rregistrobolis.to_csv("lolo.csv")

        elif a == "botanas":
            ralmacen = pd.read_csv("Inventario.csv")
            rregistrobotanas = pd.read_csv("registro botanas.csv")
            filas = len(rregistrobotanas.index)
        #agregar registro al historial
            rregistrobotanas.loc[filas] = [fecharegistro.strftime("%x"),"Carga",cantidad,cantidad*costobotanas]
        #modificar las botanas vendidas en el inventario
            filas2 = len(ralmacen.index)
            for i in range(filas2):
                if ralmacen.at[i,"Sabor"]==sabor.capitalize():
                    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
                    renglon["Cantidad"] = renglon["Cantidad"] + cantidad
                    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
                    renglon = 1
                    break
                    
                else:
                    renglon = 0
                    
            if renglon == 0:
                ralmacen.loc[filas2] = [a.capitalize(),sabor.capitalize(),cantidad]
                #guardar/sobreescribir los dataframes modificados en los archivos  csv
            
            ralmacen.index = ralmacen['Tipo']
            ralmacen.drop('Tipo', axis = 1, inplace = True)
            ralmacen.to_csv("Inventario.csv")
            rregistrobotanas.index = rregistrobotanas["Fecha"]
            ralmacen.drop("Fecha", axis = 1, inplace = True)
            rregistrobotanas.to_csv("registro botanas.csv")
    #Título
    balance = tkinter.Label(VentanadeBalance, 
                            text = 'Registros', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_titulos, Tamaño_titulos)).grid(row = 1, column = 3, padx = 5, pady = 15) #Imprime en la ventana el título Registro
    
    #Sección de ventas
    Ventas = tkinter.Label(VentanadeBalance, 
                            text = 'Ventas', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos + 2)).grid(row = 2, column = 1, padx = 10 , pady = 5)
    Articuloventa = tkinter.Label(VentanadeBalance, 
                            text = 'Artículo', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 3, column = 1, pady = 5)
    Tipoventa = tkinter.Label(VentanadeBalance, 
                            text = 'Tipo', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 4, column = 1, pady = 5)
    Cantidadventa = tkinter.Label(VentanadeBalance, 
                            text = 'Cantidad', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 5, column = 1, pady = 5)
    #Entrada de datos para las ventas
    entrada_articulo_venta = tkinter.Entry(VentanadeBalance)
    entrada_articulo_venta.grid(row = 3, column = 2) 
    entrada_tipo_venta = tkinter.Entry(VentanadeBalance)
    entrada_tipo_venta.grid(row = 4, column = 2) 
    entrada_cantidad_venta = tkinter.Entry(VentanadeBalance)
    entrada_cantidad_venta.grid(row = 5, column = 2)  
    #Boton de guardado ventas
    Guardar_venta = tkinter.Button(VentanadeBalance,
                                text = 'Guardar artículo',#Este el texto que se va a imprimir 
                               border = Tamaño_bordes,
                               bg = Color_de_botones, #Tendrá este color
                               command = Registro_de_Ventas,
                               heigh = altura_botones, #Indica el tamaño del boton
                               width = ancho_botones + 4,   
                               activebackground = botones_activos, #Tendrá este color cuando el cursor este encima
                               cursor = Figura,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 7, column = 2, pady = 10)
    
    #Sección de compras
    Compras = tkinter.Label(VentanadeBalance, 
                            text = 'Compras', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos + 2)).grid(row = 2, column = 4,padx = 10, pady = 5)
    ArticuloCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Articulo', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 3, column = 4, pady = 5)
    TipoCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Tipo', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos )).grid(row = 4, column = 4, pady = 5)
    CantidadCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Cantidad', #Este el texto que se va a imprimir 
                            bg = Color_de_fondo, #Tendrá este color
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 5, column = 4, pady = 5)
    
    
    #Entradas de datos para las compras      
    entrada_articulo_compra = tkinter.Entry(VentanadeBalance)
    entrada_articulo_compra.grid(row = 3, column = 5) 
    entrada_tipo_compra = tkinter.Entry(VentanadeBalance)
    entrada_tipo_compra.grid(row = 4, column = 5) 
    entrada_cantidad_compra = tkinter.Entry(VentanadeBalance)
    entrada_cantidad_compra.grid(row = 5, column = 5)  
    
    #Botones de compras
    Guardar_compra = tkinter.Button(VentanadeBalance,
                                text = 'Guardar artículo', #Este el texto que se va a imprimir 
                                border = Tamaño_bordes,
                               bg = Color_de_botones, #Tendrá este color
                               command = Registro_de_Compras,
                               heigh = altura_botones, #Indica el tamaño del boton
                               width = ancho_botones + 4,   
                               activebackground = botones_activos,#Tendrá este color cuando el cursor este encima
                               cursor = Figura,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 7, column = 5, pady = 10)
    
    Boton_salir = tkinter.Button(VentanadeBalance,
                                text = 'Salir', #Este el texto que se va a imprimir 
                                border = Tamaño_bordes,
                               bg = Color_de_botones, #Tendrá este color
                               command = VentanadeBalance.destroy,
                               heigh = altura_botones,  #Indica el tamaño del boton
                               width = ancho_botones + 4,   
                               activebackground = botones_activos, #Tendrá este color cuando el cursor este encima
                               cursor = Figura,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 8, column = 5)
    
   
    tkinter.mainloop()    