# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 08:09:01 2025

@author: ingmi
"""

# Super clase - Clase padre

class Vehiculo:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def descripcion(self):
        print(f"Marca: {self.marca}, \nModelo: {self.modelo},\nEn Marcha: {self.enmarcha}, \nAcelera: {self.acelera}, \nFrena: {self.frena}")
        
# Subclase - Clase hija
class Moto(Vehiculo):
    acrobacias = ''
    
    def acrobacia(self):
        self.acrobacias = 'Endo'
        
    def descripcion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nEn Marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena}\nself.acrobacias")


# subclase - Clase hija
class Furgoneta(Vehiculo):
    def carga(self, carga):
        self.cargado = carga
        
        if(self.cargado):
            return 'La furgo está cargada'
        else:
            return 'La furgo No está cargada'

class V_electrico(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 600
        
    def carcaEnergía(self):
        self.cargado = True
        
class BicicletaElectrica:
    def __init__(self):
        self.autonomia = 60
        
    def carcaEnergia(self):
        self.cargado = True
        
## Herencia Multiple
class Bici_Electrica(V_electrico,Vehiculo):
    pass


bici_Felipe = Bici_Electrica("BMW", "Thomson 2024")
bici_Felipe.arrancar()
bici_Felipe.carcaEnergía()
bici_Felipe.descripcion()




moto_Roger = Moto('Yamaha', '2026 - fz')
moto_Roger.arrancar()
moto_Roger.acelerar()
moto_Roger.descripcion()

furgo_will = Furgoneta("Polo", "2018")
furgo_will.descripcion()

# Funcion Super()
