
#coding: utf-8

'''
Created on 15 feb 2022

@author: Sergio
'''

import tkinter as tk
from tkinter import ttk,messagebox, scrolledtext
from tkinter.messagebox import Message 
from Holiday_SGV.DDBB import DDBB
#from functools import partial #para poder pasar parametros a los commands #no me funciona asi que uso funciones lambda
from threading import Thread

#

baseDeDatos = DDBB()

mainVentana = tk.Tk()
mainVentana.title("Holiday Tools - Sergio García - 2ºDAM")
mainVentana.iconbitmap('./recursos/icono.ico')
mainVentana.geometry("375x275")
mainVentana.resizable(False, False)

cMostrar:bool = False;

#

def minimizarVentana(v): #preguntar a mario
    v.iconify()

def desMinimizarVentana(v):
    v.deiconify()

def mostrarContrasenna():
    global cMostrar, entryContrasenna
    
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
    
def cargarImagenes():
    global fotoVillablanca, fotoLupa, fotoBarras, fotoSalir, fotoPerfil
    
    v = tk.PhotoImage(file='./recursos/iesVillablanca.png')
    fotoVillablanca = v.subsample(10)
    
    l = tk.PhotoImage(file='./recursos/lupa.png')
    fotoLupa = l.subsample(8)
    
    b = tk.PhotoImage(file='./recursos/graficoBarras.png')
    fotoBarras = b.subsample(8)
    
    s = tk.PhotoImage(file='./recursos/salir.png')
    fotoSalir = s.subsample(13)
    
    p = tk.PhotoImage(file='./recursos/usuario.png')
    fotoPerfil = p.subsample(10)
    
def cerrarPanel(ventana):
    
    global mainVentana
    
    ventana.destroy()
    desMinimizarVentana(mainVentana)

    
def abrirPanelAdmin():
    
    global fotoVillablanca, fotoLupa, fotoBarras, fotoSalir
    
    mainVentanaAdmin = tk.Toplevel()
    mainVentanaAdmin.title("Holiday Tools - Sergio García - 2ºDAM - (Admin) " + txtUsuario.get())
    limpiarLogin()
    mainVentanaAdmin.geometry("600x200")
    mainVentanaAdmin.resizable(False, False)
    
    ttk.Label(mainVentanaAdmin, text="Administrador", font=("bold",18), foreground="#FF0DE3").grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="S")
    
    frameAdmin = tk.Frame(mainVentanaAdmin, height=8, width=580)
    frameAdmin.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
    frameAdmin.config(bg="#FF0DE3")
    
    #fotoVillablanca
    villa = tk.Label(mainVentanaAdmin, image=fotoVillablanca)
    villa.place(x=520, y=10)
    
    #lupa
    btnLupa = ttk.Button(mainVentanaAdmin, image=fotoLupa, width=30)
    btnLupa.grid(row=2, column=0, padx=10, pady=10, sticky="S")
    
    #grafico barras
    btnBarras = ttk.Button(mainVentanaAdmin, image=fotoBarras)
    btnBarras.grid(row=2, column=1, padx=10, pady=10, sticky="S")
    
    #salir
    btnSalir = ttk.Button(mainVentanaAdmin, image=fotoSalir, command=lambda:cerrarPanel(mainVentanaAdmin))
    btnSalir.grid(row=2, column=2, padx=10, pady=10, sticky="S")
    


def abrirPanelUser():
    
    global fotoVillablanca, fotoLupa, fotoPerfil, fotoSalir
    
    mainVentanaUser = tk.Toplevel()
    mainVentanaUser.title("Holiday Tools - Sergio García - 2ºDAM - (Empleado) " + txtUsuario.get())
    limpiarLogin()
    mainVentanaUser.geometry("600x200")
    mainVentanaUser.resizable(False, False)
    
    ttk.Label(mainVentanaUser, text="Empleados", font=("bold",18), foreground="#00E013").grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="S")
    
    frameUser = tk.Frame(mainVentanaUser, height=8, width=580)
    frameUser.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
    frameUser.config(bg="#6DE069")
    
    #fotoVillablanca
    villa = tk.Label(mainVentanaUser, image=fotoVillablanca)
    villa.place(x=520, y=10)
    
    #lupa
    btnLupa = ttk.Button(mainVentanaUser, image=fotoLupa)
    btnLupa.grid(row=2, column=0, padx=10, pady=10, sticky="S")
    
    #perfil
    btnPerfil = ttk.Button(mainVentanaUser, image=fotoPerfil)
    btnPerfil.grid(row=2, column=1, padx=10, pady=10, sticky="S")
    
    #salir
    btnSalir = ttk.Button(mainVentanaUser, image=fotoSalir, command=lambda:cerrarPanel(mainVentanaUser))
    btnSalir.grid(row=2, column=2, padx=10, pady=10, sticky="S")
    
def cambiarContrasenna(contra1, contra2):
    global txtUsuario
    
    print("Usuario: " + txtUsuario.get() + "\n contra1: " + contra1 + "\ncontra2: "+ contra2)
    
    if contra1 == contra2:
        baseDeDatos.cambiarContrasenna(txtUsuario.get(), contra1)
        messagebox.showinfo(title="Update correcto", message="Se ha cambiado la contraseña de " + txtUsuario.get() + " correctamente")
    else:
        messagebox.showerror(title="Error al cambiar las contraseñas", message="Las contraseñas no coinciden")
        
    

def heOlvidadoLaContrasenna():
    global txtUsuario
    
    if comprobarUsuario():
        
        mainVentanaOlvidoContrasenna = tk.Toplevel()
        mainVentanaOlvidoContrasenna.title("Holiday Tools - Sergio García - 2ºDAM - Restablecer Contraseña")
        mainVentanaOlvidoContrasenna.geometry("325x225")
        mainVentanaOlvidoContrasenna.resizable(False, False)
        
        lblContra1 = ttk.Label(mainVentanaOlvidoContrasenna, text="Contraseña", font=("Helvetica", 16, "bold"), foreground="#0B67D9")
        lblContra1.grid(row=0, column=0, padx=10, pady=(15,3), sticky="W")
        
        txtContra1 = tk.StringVar()
        entryContra1 = ttk.Entry(mainVentanaOlvidoContrasenna, show="*", textvariable=txtContra1, width=38)
        entryContra1.grid(row=1, column=0, padx=10, pady=0)
        
        
        lblContra2 = ttk.Label(mainVentanaOlvidoContrasenna, text="Reescriba la contraseña", font=("Helvetica", 16, "bold"), foreground="#0B67D9")
        lblContra2.grid(row=2, column=0, padx=10,pady=(15,3), sticky="W")
         
        
        txtContra2 = tk.StringVar()
        entryContra2 = ttk.Entry(mainVentanaOlvidoContrasenna, show="*", textvariable=txtContra2, width=38)
        entryContra2.grid(row=3, column=0, padx=10, pady=0)
        
        frameBtn = tk.Frame(mainVentanaOlvidoContrasenna)
        frameBtn.grid(row=4, column=0, padx=10, pady=10)
        frameBtn.config(bg="lightgrey")
        
        btnAceptarCambioContra = ttk.Button(frameBtn, text="Aceptar", width=30, command=lambda:cambiarContrasenna(txtContra1.get(), txtContra2.get()))  #expresion lambda para que me deje pasarle las contraseñas de parametro
        btnAceptarCambioContra.grid(row=0, column=0, padx=10, pady=10)
        
        #mainVentanaOlvidoContrasenna.destroy()
    
    else:
        messagebox.showerror(title="Error al restablecer", message="Debes introducir un usuario válido antes de reestablecer su contraseña")
    
    
    
        
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
    
    global txtUsuario
    
    for i in range(baseDeDatos.getNumeroUsuarios()):
        userActual = baseDeDatos.hacerQuery("SELECT Usuario FROM usuarios")[i][0]
        if userActual == txtUsuario.get():
            existe = True
            
        
    return existe

def comprobarContrasenna():
    
    global txtUsuario, txtContrasenna
    
    contrasennaCoincide:bool = False
    
    contrasennabuena = baseDeDatos.hacerQuery("SELECT Contraseña FROM usuarios WHERE Usuario LIKE '" + txtUsuario.get() +"'")[0][0]
    
    if txtContrasenna.get() == contrasennabuena:
        contrasennaCoincide = True
    
    return contrasennaCoincide

def mostrarLoginSuccesful():
    loginSuccesful = tk.Toplevel()
    loginSuccesful.title('Login succesful')
    loginSuccesful.geometry("200x100")
    tk.Message(loginSuccesful, text="Inicio de sesion correcto", padx=20, pady=20).pack()
    loginSuccesful.after(1500, loginSuccesful.destroy)
    
def iniciarSesion():
    
    if not comprobarUsuario():
        messagebox.showerror("Usuario erróneo", "El usuario introducido no está registrado")
    else:
        if comprobarContrasenna():
            #messagebox.showinfo("Login succesful", "Inicio de sesion correcto")
            #print("Inicio de sesion correcto")
            mostrarLoginSuccesful()
            entrarAlPanel()
            minimizarVentana(mainVentana) #le paso la ventana que quiero cerrar
        else:
            messagebox.showerror("Contraseña errónea", "La contraseña introducida no coincide")
        
        


#

lblUsuario = ttk.Label(
    mainVentana,
    text="Usuario",
    font=("Helvetica", 16, "bold"),
    foreground="#0B67D9")
lblUsuario.grid(row=0, column=0, padx=10, pady=(15,3), sticky="W")

txtUsuario = tk.StringVar()
entryUsuario = ttk.Entry(mainVentana, textvariable=txtUsuario, width=38)
entryUsuario.grid(row=1, column=0, padx=10, pady=0)


lblContrasenna = ttk.Label(
    mainVentana,
    text="Contraseña",
    font=("Helvetica", 16, "bold"),
    foreground="#0B67D9")
lblContrasenna.grid(row=2, column=0, padx=10,pady=(15,3), sticky="W")
 

txtContrasenna = tk.StringVar()
entryContrasenna = ttk.Entry(mainVentana, show="*", textvariable=txtContrasenna, width=38)
entryContrasenna.grid(row=3, column=0, padx=10, pady=0)


f = tk.PhotoImage(file = "./recursos/verContrasenna.png")
fotoBoton = f.subsample(20, 20) 

cargarImagenes()

btnMostrarContraseña = ttk.Button(mainVentana, image=fotoBoton, command=mostrarContrasenna)
btnMostrarContraseña.grid(row=3, column=1, padx=10,sticky="N", pady=(0,10), rowspan=2)


frameBotones = tk.Frame(mainVentana)
frameBotones.grid(row=4, column=0, padx=10, pady=10)
frameBotones.config(bg="lightgrey")
#frameBotones["bg"]="blue"

btnEntrar = ttk.Button(frameBotones, text="Entrar", width=30, command=iniciarSesion)
btnEntrar.grid(row=0, column=0, padx=10, pady=10)

btnContrasennaOlvidada = ttk.Button(frameBotones, text="He olvidado mi contraseña", width=30, command=heOlvidadoLaContrasenna)
btnContrasennaOlvidada.grid(row=1, column=0, padx=10, pady=10)







#

mainVentana.mainloop()









