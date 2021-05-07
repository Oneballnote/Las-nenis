import tkinter
import tkinter.font
from Hoja_de_personalizacion import *
from datetime import datetime
import pandas as pd

dt = datetime.now()

Articulos_vendidos = []
Tipo_vendido = []
Cantidad_vendida = []

Articulos_comprados = []
Tipo_comprado = []
cantidad_comprada = []

def ventana_balance():
    VentanadeBalance = tkinter.Tk()
    VentanadeBalance.geometry('670x340')
    VentanadeBalance.configure(bg = Color_de_fondo)
    VentanadeBalance.title('Registro')
    
    
    def Registro_de_Ventas():
        a = entrada_articulo_venta.get()
        b = entrada_tipo_venta.get()
        c = entrada_cantidad_venta.get()
        Articulos_vendidos.append(a)
        Tipo_vendido.append(b)
        Cantidad_vendida.append(c)
        #REGISTRAR VENTA 
        fechadia = datetime.now()
        fecharegistro =fechadia.date()

        preciobolis=14
        preciobotanas=30

        #Ingreso de la venta por parte del usuario
        tipoproducto =  input("Tipo de producto vendido (botanas/bolis): ").lower()
        sabor = input("Sabor del producto vendido: ").lower()
        cantidad = int(input("Cantidad de unidades vendidas: "))


    #lectura de df's de historial e inventario
        if tipoproducto=="bolis":
            ralmacen = pd.read_csv("Inventario.csv")
            print(ralmacen)
            rregistrobolis = pd.read_csv("registro_bolis.csv")
            print(rregistrobolis)
            filas = len(rregistrobolis.index)
    #agregar registro al historial
            rregistrobolis.loc[filas] = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobolis]
            print(rregistrobolis)
    #modificar los bolis vendidos en el inventario
            renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
            renglon["Cantidad"] = renglon["Cantidad"] - cantidad
            ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
            print(ralmacen)
    #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.to_csv("Inventario.csv")
            rregistrobolis.to_csv("registro_bolis.csv")
    
        elif tipoproducto=="botanas":
            ralmacen = pd.read_csv("Inventario.csv")
            print(ralmacen)
            rregistrobotanas = pd.read_csv("registro_botanas.csv")
            print(rregistrobotanas)
            filas = len(rregistrobotanas.index)
    #agregar registro al historial
            rregistrobotanas.loc[filas] = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobotanas]
            print(rregistrobotanas)
    #modificar las botanas vendidas en el inventario
            renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
            renglon["Cantidad"] = renglon["Cantidad"] - cantidad
            ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
            print(ralmacen)
    #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.to_csv("Inventario.csv")
            rregistrobotanas.to_csv("registro_botanas.csv")
        
    def Registro_de_Compras():
        a = entrada_articulo_compra.get()
        b = entrada_tipo_compra.get()
        c = entrada_cantidad_compra.get()
        Articulos_comprados.append(a)
        Tipo_comprado.append(b)
        cantidad_comprada.append(c)
        #En BALANCE
        #REGISTRAR COMPRA/CARGA
        fechadia = datetime.now()
        fecharegistro =fechadia.date()

        costobolis=-9
        costobotanas=-19

        #Ingreso de la venta por parte del usuario
        tipoproducto =  input("Tipo de producto cargado (botanas/bolis): ").lower()
        sabor = input("Sabor del producto cargado: ").lower()
        cantidad = int(input("Cantidad de unidades cargadas: "))


        #lectura de df's de historial e inventario
        if tipoproducto=="bolis":
            ralmacen = pd.read_csv("Inventario.csv")
            print(ralmacen)
            rregistrobolis = pd.read_csv("registro_bolis.csv")
            print(rregistrobolis)
            filas = len(rregistrobolis.index)
        #agregar registro al historial
            #nuevoregistro = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobolis]
            rregistrobolis.loc[filas] = [fecharegistro.strftime("%d/%m/%Y"),"Carga",cantidad,cantidad*costobolis]
            print(rregistrobolis)
        #modificar los bolis vendidos en el inventario
            filas2 = len(ralmacen.index)
        #buscamos fila por fila si el sabor que compramos ya estába en el inventario
            for i in range(filas2):
                if ralmacen.at[i,"Sabor"]==sabor.capitalize():        
        #Si el sabor ya estaba entonces al renglón de ese sabor le modificamos la cantidad
                    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
                    renglon["Cantidad"] = renglon["Cantidad"] + cantidad
                    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
                    print(ralmacen)
        #Si en ningún renglón encontramos el sabor entonces...
                else:
                    renglon=0
        #Si no se encontró el sabor en el inventario significa que cargamos uno nuevo, por lo que agregamos un nuevo campo
            if renglon==0:
                ralmacen.loc[filas2] = [tipoproducto.capitalize(),sabor.capitalize(),cantidad]        
        #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.index = ralmacen["Tipo"]
            ralmacen.to_csv("Inventario.csv")
            rregistrobolis.index = rregistrobolis["Tipo"]
            rregistrobolis.to_csv("registro_bolis.csv")

        elif tipoproducto=="botanas":
            ralmacen = pd.read_csv("Inventario.csv")
            print(ralmacen)
            rregistrobotanas = pd.read_csv("registro_botanas.csv")
            print(rregistrobotanas)
            filas = len(rregistrobotanas.index)
        #agregar registro al historial
            rregistrobotanas.loc[filas] = [fecharegistro.strftime("%d/m/%Y"),"Carga",cantidad,cantidad*costobotanas]
            print(rregistrobotanas)
        #modificar las botanas vendidas en el inventario
            filas2 = len(ralmacen.index)
            for i in range(filas2):
                if ralmacen.at[i,"Sabor"]==sabor.capitalize():
                    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
                    renglon["Cantidad"] = renglon["Cantidad"] + cantidad
                    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon
                    print(ralmacen)
                else:
                    renglon=0
            if renglon==0:
                ralmacen.loc[filas2] = [tipoproducto.capitalize(),sabor.capitalize(),cantidad]
        #guardar/sobreescribir los dataframes modificados en los archivos  csv
            ralmacen.index = ralmacen["Tipo"]
            ralmacen.to_csv("Inventario.csv")
            rregistrobotanas.index = rregistrobotanas["Fecha"]
            rregistrobotanas.to_csv("registro_botanas.csv")

    #Título
    balance = tkinter.Label(VentanadeBalance, 
                            text = 'Registros', 
                            bg = Color_de_fondo, 
                            font = (Fuente_titulos, Tamaño_titulos)).grid(row = 1, column = 3, padx = 5, pady = 15)
    
    #Sección de ventas
    Ventas = tkinter.Label(VentanadeBalance, 
                            text = 'Ventas', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos + 2)).grid(row = 2, column = 1, padx = 10 , pady = 5)
    Articuloventa = tkinter.Label(VentanadeBalance, 
                            text = 'Artículo', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 3, column = 1, pady = 5)
    Tipoventa = tkinter.Label(VentanadeBalance, 
                            text = 'Tipo', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 4, column = 1, pady = 5)
    Cantidadventa = tkinter.Label(VentanadeBalance, 
                            text = 'Cantidad', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 5, column = 1, pady = 5)
    Gananciaventa = tkinter.Label(VentanadeBalance, 
                            text = 'Ganancia', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 6, column = 1, pady = 5)
    #Entrada de datos para las ventas
    entrada_articulo_venta = tkinter.Entry(VentanadeBalance)
    entrada_articulo_venta.grid(row = 3, column = 2) 
    entrada_tipo_venta = tkinter.Entry(VentanadeBalance)
    entrada_tipo_venta.grid(row = 4, column = 2) 
    entrada_cantidad_venta = tkinter.Entry(VentanadeBalance)
    entrada_cantidad_venta.grid(row = 5, column = 2)  
    #Boton de guardado ventas
    Guardar_venta = tkinter.Button(VentanadeBalance,
                                text = 'Guardar artículo',
                               border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = Registro_de_Ventas,
                               heigh = altura_botones, 
                               width = ancho_botones + 4,   
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 7, column = 2, pady = 10)
    
    #Sección de compras
    Compras = tkinter.Label(VentanadeBalance, 
                            text = 'Compras', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos + 2)).grid(row = 2, column = 4,padx = 10, pady = 5)
    ArticuloCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Articulo', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 3, column = 4, pady = 5)
    TipoCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Tipo', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos )).grid(row = 4, column = 4, pady = 5)
    CantidadCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Cantidad', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 5, column = 4, pady = 5)
    GananciaCompra = tkinter.Label(VentanadeBalance, 
                            text = 'Ganancia', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 6, column = 4, pady = 5)
    GananciaCompraEscrita = tkinter.Label(VentanadeBalance, 
                            text = 'Ganancia', 
                            bg = Color_de_fondo, 
                            font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 6, column = 4, pady = 5)
    
    #Entradas de datos para las compras      
    entrada_articulo_compra = tkinter.Entry(VentanadeBalance)
    entrada_articulo_compra.grid(row = 3, column = 5) 
    entrada_tipo_compra = tkinter.Entry(VentanadeBalance)
    entrada_tipo_compra.grid(row = 4, column = 5) 
    entrada_cantidad_compra = tkinter.Entry(VentanadeBalance)
    entrada_cantidad_compra.grid(row = 5, column = 5)  
    
    #Botones de compras
    Guardar_compra = tkinter.Button(VentanadeBalance,
                                text = 'Guardar artículo',
                                border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = Registro_de_Compras,
                               heigh = altura_botones, 
                               width = ancho_botones + 4,   
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 7, column = 5, pady = 10)
    #
    Boton_salir = tkinter.Button(VentanadeBalance,
                                text = 'Guardar y salir',
                                border = Tamaño_bordes,
                               bg = Color_de_botones, 
                               command = VentanadeBalance.destroy,
                               heigh = altura_botones, 
                               width = ancho_botones + 4,   
                               activebackground = botones_activos,
                               cursor = Figura,
                               relief = Tipo_borde,
                               font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 8, column = 5)
    
   
    tkinter.mainloop()    
