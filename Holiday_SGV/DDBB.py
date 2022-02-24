
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
        
        #Si quieres probar la base de datos y atacarla puedes 'descomentar' la funcion de debajo una vez
        #self.cargarDatos()

    def getNumeroUsuarios(self):
        self.cursor.execute("SELECT COUNT(usuarios.Usuario) FROM usuarios")
        return int(self.cursor.fetchall()[0][0])
    
    def hacerQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def usuarioExiste(self,u):
        existe:bool = False
        
        global txtUsuario
        
        for i in range(self.getNumeroUsuarios()):
            userActual = self.hacerQuery("SELECT Usuario FROM usuarios")[i][0]
            if userActual == u:
                existe = True
                
        return existe
    
    def cambiarContrasenna(self, usuario, contrasenna):      
        self.cursor.execute("UPDATE usuarios SET usuarios.Contraseña = '" + contrasenna + "' WHERE (usuarios.Usuario = '" + usuario + "');")    
        self.conexion.commit()
        
    def getDiasTotalesVacacionesDisponiblesDeEmpleado(self, empleado):
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + empleado + "'")
        numDias = self.cursor.fetchall()[0][0]
        return numDias

    def getNumDiasQueLeQuedan(self, empleado):
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE fechas.Usuario = '" + empleado + "' AND fechas.Fecha > NOW()")
        numDias = self.cursor.fetchall()[0][0]
        return numDias
    
    def getDiasQueLeQuedan(self, empleado):
        self.cursor.execute("SELECT fechas.Fecha FROM fechas WHERE fechas.Usuario = '" + empleado + "' AND fechas.Fecha > NOW()")
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
        Fecha DATE NOT NULL,
        Usuario VARCHAR(30) NOT NULL,
        FOREIGN KEY (Usuario) REFERENCES usuarios(Usuario)
        
        )ENGINE=InnoDB;
        ''')
        
        #Inserto datos
        
        self.cursor.execute('''INSERT INTO usuarios VALUES ('admin','admin','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('MarioSantos','123abc','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Sergio','123abc','administrador');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Pizarroso','vegano','empleado');''')
        self.cursor.execute('''INSERT INTO usuarios VALUES ('Jorge','chispas','empleado');''')
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-22','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-02-23','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-24','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-04-25','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-26','Jorge');''')
        
        
        self.conexion.commit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    