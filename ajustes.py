from Hoja_de_personalizacion import *
import tkinter
import tkinter.font
import io
 
    
def ventana_ajustes():
            
    
    def save():
        archivo = open('nombre.txt','w')
    
        archivo.write(e.get())
        archivo.close()
        VentanaNombre.destroy()
        
    VentanaDeAjustes = tkinter.Tk()
    VentanaDeAjustes.title("Ajustes")
    VentanaDeAjustes.geometry('500x700')
    VentanaDeAjustes.configure(bg = Color_de_fondo)

    #Titulo de la ventana
    Nombre_ventana = tkinter.Label(VentanaDeAjustes, 
                                   text = 'Ajustes',
                                   bg = Color_de_fondo,
                                   font = (Fuente_titulos,Tamaño_titulos)).grid(row = 1, column = 1)
    
    #Primera sección
    Nombre_seccion_cambio = tkinter.Label(VentanaDeAjustes,
                                          text = 'Cambio de nombre',
                                          bg = Color_de_fondo,
                                          font = (Fuente_titulos, Tamaño_titulos - 1)).grid(row = 2,column = 1, pady = 10)
    Nombre_empresa = tkinter.Entry(VentanaDeAjustes, width = 30)
    Nombre_empresa.grid(row = 4, column = 1)
    cambio_nombre = tkinter.Label(VentanaDeAjustes, 
                              text = 'Introduzca el nombre',
                              bg = Color_de_fondo,
                              font = (Fuente_titulos, 10)).grid(row = 3, column = 1, pady = 10)
    guardar = tkinter.Button(VentanaDeAjustes, 
                           text = 'Guardar\ny\nsalir ', 
                           border = Tamaño_bordes,
                           bg = Color_de_botones, 
                           command = save,
                           heigh = altura_botones + 1, 
                           width = ancho_botones,   
                           activebackground = botones_activos,
                           cursor = Figura,
                           relief = Tipo_borde,
                           font = (Fuente_botones, Tamaño_fuente_botones)).grid(row = 5, column = 1, pady = 10)
    '''
    #Segunda sección
    Titulo_precios = tkinter.Label(VentanaDeAjustes,
                                   text = 'Precios',
                                   bg = Color_de_fondo,
                                   font = (Fuente_titulos, Tamaño_titulos - 1)).grid(pady = 10)
    Titulo_productos = tkinter.Label(VentanaDeAjustes,
                               text = 'Producto',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 7,column = 1, pady = 10)
    Entrada_producto = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_producto.grid(row = 7,column = 1)
    Titulo_precios_entry = tkinter.Label(VentanaDeAjustes,
                               text = 'Precio',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid(row = 8,column = 1)
    Entrada_precio = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_precio.grid(row = 8,column = 1)
    Boton_precio = tkinter.Button(VentanaDeAjustes,
                                  text = 'Precios',
                                   border = Tamaño_bordes,
                                   bg = Color_de_botones, 
                                   command = VentanaDeAjustes.destroy, 
                                   heigh = altura_botones, 
                                   width = ancho_botones,   
                                   activebackground = botones_activos,
                                   cursor = Figura,
                                   relief = Tipo_borde,
                                   font = (Fuente_botones, Tamaño_fuente_botones)).grid(column = 1,pady = Espacio_botones)
    #Tercera sección
    
    Titulo_costos = tkinter.Label(VentanaDeAjustes,
                               text = 'Costos',
                               bg = Color_de_fondo,
                               font = (Fuente_titulos, Tamaño_titulos - 1)).grid()
    Titulo_producto = tkinter.Label(VentanaDeAjustes,
                               text = 'Producto',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid()
    EntradaProducto = tkinter.Entry(VentanaDeAjustes, width = 30)
    EntradaProducto.grid()
    Titulo_costo = tkinter.Label(VentanaDeAjustes,
                               text = 'Costo',
                               bg = Color_de_fondo,
                               font = (Fuente_subtitulos, Tamaño_subtitulos)).grid()
    Entrada_costo = tkinter.Entry(VentanaDeAjustes, width = 30)
    Entrada_costo.grid()
    #Botones
    Boton_costos = tkinter.Button(VentanaDeAjustes,
                                  text = 'Costos',
                                  border = Tamaño_bordes,
                                  bg = Color_de_botones, 
                                  command = VentanaDeAjustes.destroy, 
                                  heigh = altura_botones, 
                                  width = ancho_botones,   
                                  activebackground = botones_activos,
                                  cursor = Figura,
                                  relief = Tipo_borde,
                                  font = (Fuente_botones, Tamaño_fuente_botones)).grid()
    boton_salir = tkinter.Button(VentanaDeAjustes, 
                                 text = 'Volver', 
                                 border = Tamaño_bordes,
                                 bg = Color_de_botones, 
                                 command = VentanaDeAjustes.destroy, 
                                 heigh = altura_botones, 
                                 width = ancho_botones,   
                                 activebackground = botones_activos,
                                 cursor = Figura,
                                 relief = Tipo_borde,
                                 font = (Fuente_botones, Tamaño_fuente_botones)).grid(pady = Espacio_botones)
    '''
    tkinter.mainloop()

ventana_ajustes()