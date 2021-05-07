import tkinter
import tkinter.font
from Hoja_de_personalizacion import *
from datetime import datetime

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
        
    def Registro_de_Compras():
        a = entrada_articulo_compra.get()
        b = entrada_tipo_compra.get()
        c = entrada_cantidad_compra.get()
        Articulos_comprados.append(a)
        Tipo_comprado.append(b)
        cantidad_comprada.append(c)
        
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
