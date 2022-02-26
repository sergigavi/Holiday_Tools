
#coding: utf-8

'''
Created on 26 feb 2022

@author: Sergio
'''
#
from socketserver import BaseRequestHandler, TCPServer
#

class RequestHandler(BaseRequestHandler):
    
    def handle(self):
        
        while True:
            bloque = self.request.recv(1024)
            
            if not bloque: break
            
            self.request.send(bloque)
            
            

def start_server():
    server = TCPServer(('localhost', 24000), RequestHandler)
    server.serve_forever()