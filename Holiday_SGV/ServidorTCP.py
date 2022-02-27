
#coding: utf-8

'''
Created on 26 feb 2022

@author: Sergio
'''
#
from socketserver import BaseRequestHandler, TCPServer
from Holiday_SGV.DDBB import DDBB
#

class RequestHandler(BaseRequestHandler):
    
    def handle(self):
        db = DDBB()
        
        while True:
            
            bloque = self.request.recv(1024)
            
            if not bloque: break
            
            try:
                
                if bloque[0].isdigit():
                    user = db.hacerQuery("SELECT Usuario FROM fechas WHERE Fecha = '" + bloque + "'")
                    db.eliminarDiaUsuario(user, bloque)
                    self.request.send("Se ha eliminado la fecha " + bloque)
                else:
                    diasEmple = db.getDiasQueLeQuedan(bloque)
                    self.request.send(diasEmple)
                    
            except:
                pass
            
            
            

def start_server():
    server = TCPServer(('localhost', 24000), RequestHandler)
    server.serve_forever()