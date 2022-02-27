
#coding: utf-8

'''
Created on 26 feb 2022

@author: Sergio
'''

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Holiday_SGV.DDBB import DDBB

class Grafico():
    
    def __init__(self):
        
        db = DDBB()
        
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", ]
    
        miFigura = Figure(figsize=(12, 5), facecolor='white') 
    
        ejes = miFigura.add_subplot(111)
    
        ejes.set_xlim(0, 11) #meses
        #ejes.set_ylim(0, 31) #dias
    
        e0, = ejes.plot(meses, db.getNumFechasEmpleadoPorMes("admin"), color='green')
        e1, = ejes.plot(meses, db.getNumFechasEmpleadoPorMes("MarioSantos"), color='blue')
        e2, = ejes.plot(meses, db.getNumFechasEmpleadoPorMes("Sergio"), color='yellow')
        e3, = ejes.plot(meses, db.getNumFechasEmpleadoPorMes("Pizarroso"), color='red')
        e4, = ejes.plot(meses, db.getNumFechasEmpleadoPorMes("Jorge"), color='green')
        
        #leyenda
        miFigura.legend((e0,e1,e2,e3,e4), ("admin", "MarioSantos", "Sergio", "Pizarroso", "Jorge"), "upper right")
    
        ejes.set_xlabel("Meses")
        ejes.set_ylabel("Dias libres mensuales")
        
        ejes.grid(linestyle='-')
        
        miGrafico = tk.Toplevel()
        
        canvas = FigureCanvasTkAgg(miFigura,master=miGrafico)
        canvas._tkcanvas.pack(sid=tk.TOP, fill=tk.BOTH, expand=1)
        
        
        
        