
#coding: utf-8

'''
Created on 15 feb 2022

@author: Sergio
'''

import tkinter as tk
from tkinter import ttk,messagebox, scrolledtext
from Holiday_SGV.DDBB import DDBB
from threading import Thread

#

baseDeDatos = DDBB()

mainVentana = tk.Tk()
mainVentana.title("Holiday Tools - Sergio García - 2ºDAM")
mainVentana.iconbitmap('icono.ico')
mainVentana.geometry("375x275")
mainVentana.resizable(False, False)

cMostrar:bool = False;

#

def minimizarVentana(v):
    v.iconify()

def desMinimizarVentana(v):
    v.deiconify()

def mostrarContrasenna():
    #global cMostrar, entryContrasenna
    
    if not cMostrar:
        cMostrar = True
    else:
        cMostrar = False
    
    if cMostrar:
        entryContrasenna.config(show="")
    else:
        entryContrasenna.config(show="*")
    
#Esta funcion se encarga de vaciar los valores del formulario de inicio de sesion, por si se van a iniciar varias a la vez, así no aparecen los datos del anterior
def limpiarLogin():
    txtUsuario.set("")
    txtContrasenna.set("")
    
def abrirPanelAdmin():
    mainVentanaAdmin = tk.Toplevel()
    mainVentanaAdmin.title("Holiday Tools - Sergio García - 2ºDAM - (Admin) " + txtUsuario.get())
    limpiarLogin()
    mainVentanaAdmin.geometry("600x200")
    mainVentanaAdmin.resizable(False, False)
    

def abrirPanelUser():
    mainVentanaUser = tk.Toplevel()
    mainVentanaUser.title("Holiday Tools - Sergio García - 2ºDAM - (Empleado) " + txtUsuario.get())
    limpiarLogin()
    mainVentanaUser.geometry("600x200")
    mainVentanaUser.resizable(False, False)
    
        
def entrarAlPanel():
    #comprobar el tipo de usuario que ha iniciado sesion y dependiendo abrir la vista de usuario o la vista de administrador
    tipo = baseDeDatos.hacerQuery("SELECT Tipo FROM usuarios WHERE usuarios.Usuario LIKE '" + txtUsuario.get() + "'")[0][0]
    
    if tipo == "administrador":
        hiloAdmin = Thread(target=abrirPanelAdmin, name="Hiloadmin")
        hiloAdmin.start()
        
    else: #tipo == "empleado"
        hiloUser = Thread(target=abrirPanelUser, name="Hilouser")
        hiloUser.start()
        
def comprobarUsuario():
    existe:bool = False
    
    #global txtUsuario
    
    for i in range(baseDeDatos.getNumeroUsuarios()):
        userActual = baseDeDatos.hacerQuery("SELECT Usuario FROM usuarios")[i][0]
        if userActual == txtUsuario.get():
            existe = True
            
        
    return existe

def comprobarContrasenna():
    
    #global txtUsuario, txtContrasenna
    
    contrasennaCoincide:bool = False
    
    contrasennabuena = baseDeDatos.hacerQuery("SELECT Contraseña FROM usuarios WHERE Usuario LIKE '" + txtUsuario.get() +"'")[0][0]
    
    if txtContrasenna.get() == contrasennabuena:
        contrasennaCoincide = True
    
    return contrasennaCoincide
    
def iniciarSesion():
    
    if not comprobarUsuario():
        messagebox.showerror("Usuario erróneo", "El usuario introducido no está registrado")
    else:
        if comprobarContrasenna():
            oleHasIniciao = messagebox.showinfo("Login succesful", "Inicio de sesion correcto")
            #oleHasIniciao.kill()
            entrarAlPanel()
            minimizarVentana(mainVentana) #le paso la ventana que quiero cerrar
        else:
            messagebox.showerror("Contraseña errónea", "La contraseña introducida no coincide")
        
        
    

def heOlvidadoMiContrasenna():
    pass

#

lblUsuario = ttk.Label(
    mainVentana,
    text="Usuario",
    font=("Helvetica", 16),
    foreground="#0B67D9")
lblUsuario.grid(row=0, column=0, padx=10, pady=(15,3), sticky="W")

txtUsuario = tk.StringVar()
entryUsuario = ttk.Entry(mainVentana, textvariable=txtUsuario, width=38)
entryUsuario.grid(row=1, column=0, padx=10, pady=0)


lblContrasenna = ttk.Label(
    mainVentana,
    text="Contraseña",
    font=("Helvetica", 16),
    foreground="#0B67D9")
lblContrasenna.grid(row=2, column=0, padx=10,pady=(15,3), sticky="W")
 

txtContrasenna = tk.StringVar()
entryContrasenna = ttk.Entry(mainVentana, show="*", textvariable=txtContrasenna, width=38)
entryContrasenna.grid(row=3, column=0, padx=10, pady=0)


f = tk.PhotoImage(file = "verContrasenna.png")
fotoBoton = f.subsample(20, 20) 

btnMostrarContraseña = ttk.Button(mainVentana, image=fotoBoton, command=mostrarContrasenna)
btnMostrarContraseña.grid(row=3, column=1, padx=10,sticky="N", pady=(0,10), rowspan=2)


frameBotones = tk.Frame(mainVentana)
frameBotones.grid(row=4, column=0, padx=10, pady=10)
frameBotones.config(bg="lightgrey")
#frameBotones["bg"]="blue"

btnEntrar = ttk.Button(frameBotones, text="Entrar", width=30, command=iniciarSesion)
btnEntrar.grid(row=0, column=0, padx=10, pady=10)

btnContrasennaOlvidada = ttk.Button(frameBotones, text="He olvidado mi contraseña", width=30, command=heOlvidadoMiContrasenna)
btnContrasennaOlvidada.grid(row=1, column=0, padx=10, pady=10)







#

mainVentana.mainloop()









