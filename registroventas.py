# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:40:41 2021

@author: Hannia
"""


from datetime import datetime
import pandas as pd

#En BALANCE
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
    rregistrobolis = pd.read_csv("registro_bolis.csv")
    filas = len(rregistrobolis.index)
#agregar registro al historial
    #nuevoregistro = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobolis]
    rregistrobolis.loc[filas] = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobolis]

#modificar los bolis vendidos en el inventario
    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
    renglon["Cantidad"] = renglon["Cantidad"] - cantidad
    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon

#guardar/sobreescribir los dataframes modificados en los archivos  csv
    ralmacen.to_csv("Inventario.csv")
    rregistrobolis.to_csv("registro_bolis.csv")
    
elif tipoproducto=="botanas":
    ralmacen = pd.read_csv("Inventario.csv")
    rregistrobotanas = pd.read_csv("registro_botanas.csv")
    filas2 = len(rregistrobotanas.index)
#agregar registro al historial
    rregistrobotanas.loc[filas] = [fecharegistro.strftime("%x"),"Venta",cantidad,cantidad*preciobotanas]
#modificar las botanas vendidas en el inventario
    renglon = ralmacen[ralmacen["Sabor"]==sabor.capitalize()]
    renglon["Cantidad"] = renglon["Cantidad"] - cantidad
    ralmacen[ralmacen["Sabor"]==sabor.capitalize()] = renglon

#guardar/sobreescribir los dataframes modificados en los archivos  csv
    ralmacen.to_csv("Inventario.csv")
    rregistrobotanas.to_csv("registro_botanas.csv")
    