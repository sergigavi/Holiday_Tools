
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
        
        #Si quieres probar la base de datos y atacarla puedes 'descomentar' la funcion de debajo una vez (luego tienes que comentarla y volver a ejecutar)
        #self.cargarDatos()

    def getNumeroUsuarios(self):
        self.cursor.execute("SELECT COUNT(usuarios.Usuario) FROM usuarios")
        return int(self.cursor.fetchall()[0][0])
    
    def getUsuarios(self):
        self.cursor.execute("SELECT usuarios.Usuario FROM usuarios")
        return self.cursor.fetchall()
    
    def getFechas(self):
        self.cursor.execute("SELECT * FROM fechas")
        return self.cursor.fetchall()
    
    #devuelvo una lista de 12 posiciones con el total de fechas de ese empleado en cada mes del año
    def getNumFechasEmpleadoPorMes(self, emple):
        lista = []
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 1")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 2")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 3")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 4")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 5")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 6")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 7")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 8")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 9")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 10")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 11")
        lista.append(self.cursor.fetchall()[0][0])
        
        self.cursor.execute("SELECT COUNT(*) FROM fechas WHERE Usuario = '" + emple +"' AND MONTH(Fecha) = 12")
        lista.append(self.cursor.fetchall()[0][0])
        
        #print("lista de dias libres por mes de " + emple)
        #print(lista)
        return lista
    
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
    
    def eliminarDiaUsuario(self, user, fecha):
        salida = ""
        #no se pueden eliminar fechas que ya han pasado/ya se han disfrutado
        try:
            self.cursor.execute("SELECT * FROM fechas WHERE fechas.Fecha = '" + fecha + "' AND fechas.Usuario = '" + user + "' AND fechas.Fecha > NOW()")
            salida = self.cursor.fetchall()[0][1]
                
        except:
            messagebox.showerror(title="SQL Error", message="Usuario / Fecha no válidos")
            
        if salida == user:
            self.cursor.execute("DELETE FROM fechas WHERE fechas.Fecha = '" + fecha + "' AND fechas.Usuario = '" + user + "' AND fechas.Fecha > NOW()")
            messagebox.showinfo(title="Operación realizada", message="Se ha eliminado la fecha correctamente")
        self.conexion.commit()
        
    
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
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-25','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-02-12','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-05','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-04-09','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-15','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-06-30','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-08-11','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-10-04','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-11-17','admin');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-26','admin');''')
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-11-22','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-22','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-22','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-22','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-29','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-11-15','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-30','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-11','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-25','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-05','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-11','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-21','MarioSantos');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-06','MarioSantos');''')
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-11-22','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-22','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-22','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-22','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-29','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-11-14','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-15','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-14','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-11','Sergio');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-12','Sergio');''')
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-22','Pizarroso');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2021-06-23','Pizarroso');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2021-07-24','Pizarroso');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2020-08-25','Pizarroso');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-09-26','Pizarroso');''')
        
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-01-22','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-02-23','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-03-24','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-04-25','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-05-26','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-04-15','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-04-16','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-13','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-12','Jorge');''')
        self.cursor.execute('''INSERT INTO fechas VALUES ('2022-12-11','Jorge');''')
        
        
        self.conexion.commit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    