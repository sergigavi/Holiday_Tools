
#coding: utf-8

'''
Created on 17 feb 2022

@author: Sergio
'''


import mysql.connector as conn
import tkinter
from tkinter import ttk, messagebox

class DDBB():
    
    def __init__(self):
        self.conexion = conn.connect(host="127.0.0.1", user="root", password="123abc")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS HolydayToolsDDBB")
        self.cursor.execute("USE HolydayToolsDDBB")
        #self.cargarDatos()

    def getNumeroUsuarios(self):
        self.cursor.execute("SELECT COUNT(usuarios.Usuario) FROM usuarios")
        return int(self.cursor.fetchall()[0][0])
    
    def hacerQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def cargarDatos(self):
        
        #Creo las tablas
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
        Usuario VARCHAR(30) NOT NULL PRIMARY KEY,
        Contraseña VARCHAR(30) NOT NULL,
        Tipo VARCHAR(13)
        
        )ENGINE=InnoDB;
        ''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fechas(
        Fecha CHAR(10) NOT NULL,
        Usuario VARCHAR(30) NOT NULL,
        FOREIGN KEY (Usuario) REFERENCES usuarios(Usuario)
        
        )ENGINE=InnoDB;
        ''')
        
        #Inserto datos
        
        self.cursor.execute('''INSERT INTO usuarios VALUES ('admin','admin','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('MarioSantos','123abc','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Sergio','123abc','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Pizarroso','vegano','empleado');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Jorge','admin','empleado');''')
        
        
        self.conexion.commit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    