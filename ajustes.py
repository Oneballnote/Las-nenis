from Hoja_de_personalizacion import *
import tkinter
import tkinter.font
import io
 
Nombre_producto = []
Precio_producto = []
Costo_producto = []

def ventana_ajustes():
            
    def save():
        archivo = open('nombre.txt','w')
        archivo.write(Nombre_empresa.get())
        archivo.close()
        
    def Almacenar_productos():
        Nombre_producto.append(Entrada_producto.get())
        Precio_producto.append(Entrada_precio.get())
        Costo_producto.append(Entrada_costo.get())
    
    def Guardar_datos():
        Archivo = open('productos.txt', 'w')
        for i in Nombre_producto: 
            Archivo.write(i + ',')
        Archivo.close()
        costo = open('costo.txt', 'w')
        for i in Costo_producto:
            costo.write(i + ',')
        costo.close()
        precio = open('Precio.txt', 'w') 
        for i in Precio_producto:
            precio.write(i + ',')
        precio.close()
        VentanaDeAjustes.destroy()
        
    VentanaDeAjustes = tkinter.Tk()
    VentanaDeAjustes.title("Ajustes")
    VentanaDeAjustes.geometry('500x600')
    VentanaDeAjustes.configure(bg = Color_de_fondo)

    #Titulo de la ventana
    Nombre_ventana = tkinter.Label(VentanaDeAjustes, 
                                   text = 'Ajustes',
                                   bg = Color_de_fondo,
                                   font = (Fuente_titulos,Tamaño_titulos)).grid(pady = Espacio_botones - 5)
    
    #Primera sección
    Nombre_seccion_cambio = tkinter.Label(VentanaDeAjustes,
                                          text = 'Cambio de nombre',
                                          bg = Color_de_fondo,
                                          font = (Fuente_titulos, Tamaño_titulos - 1)).grid(pady = Espacio_botones - 5)
    Nombre_empresa = tkinter.Entry(VentanaDeAjustes, width = 30)
    Nombre_empresa.grid(pady = Espacio_botones - 5)
    cambio_nombre = tkinter.Label(VentanaDeAjustes, 
                              text = 'Introduzca el nombre',
                              bg = Color_de_fondo,
                              font = (Fuente_titulos, 10)).grid(pady = Espacio_botones - 5)
    guardar = tkinter.Button(VentanaDeAjustes, 
                           text = 'Guardar', 
                           border = Tamaño_bordes,
                           bg = Color_de_botones, 
                           command = save,
                           heigh = altura_botones, 
                           width = ancho_botones,   
                           activebackground = botones_activos,
                           cursor = Figura,
                           font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones - 5)
   
   
    Separacion = tkinter.Label(VentanaDeAjustes, 
                               text = '-'*71,
                               bg = Color_de_fondo).grid(pady = Espacio_botones - 5)
    
    #Segunda sección
    Titulo_precios = tkinter.Label(VentanaDeAjustes,
                                   text = 'Precios',
                                   bg = Color_de_fondo,
                                   font = (Fuente_titulos, Tamaño_titulos - 1)).grid(pady = Espacio_botones - 5)
    Titulo_productos = tkinter.Label(VentanaDeAjustes,
                               text = 'Producto',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(pady = Espacio_botones - 5)
    Entrada_producto = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_producto.grid(pady = Espacio_botones - 5)
    Titulo_precios_entry = tkinter.Label(VentanaDeAjustes,
                               text = 'Precio',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(pady = Espacio_botones - 5)
    Entrada_precio = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_precio.grid(pady = Espacio_botones - 5)
    #Tercera sección
    Titulo_costo = tkinter.Label(VentanaDeAjustes,
                               text = 'Costo',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(pady = Espacio_botones - 5)
    Entrada_costo = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_costo.grid(pady = Espacio_botones - 5)
    #Botones
    Boton_almacenar_datos = tkinter.Button(VentanaDeAjustes,
                                  text = 'Guardar',
                                  border = Tamaño_bordes,
                                  bg = Color_de_botones, 
                                  command = Almacenar_productos, 
                                  heigh = altura_botones, 
                                  width = ancho_botones,   
                                  activebackground = botones_activos,
                                  cursor = Figura,
                                  font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
    boton_salir = tkinter.Button(VentanaDeAjustes, 
                                 text = 'Guardar\ny\nsalir', 
                                 border = Tamaño_bordes,
                                 bg = Color_de_botones, 
                                 command = Guardar_datos, 
                                 heigh = altura_botones + 1, 
                                 width = ancho_botones,   
                                 activebackground = botones_activos,
                                 cursor = Figura,
                                 font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones - 5)
    
    tkinter.mainloop() #Crea un bucle para que no se cierre la ventana