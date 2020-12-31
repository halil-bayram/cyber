#import socket


import pyfiglet 
import sys 
import socket 
from datetime import datetime 
   
ascii_banner = pyfiglet.figlet_format("PİNK PANTHER PORT SCANNER") 
print(ascii_banner) 

port_liste=[]
banner_liste=[]
dosya=open("ip.txt","r")
ipler=dosya.read()
dosya.close()
for ip in ipler.splitlines():
    print(ip)      
    # will scan ports between 1 to 65,535 
    for port in range(1,6000): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
          
        # returns an error indicator 
        result = s.connect_ex((ip,port)) 
        if result ==0: 
            print("Port {} is open".format(port)) 
        s.close() 

print(port_liste)
print(banner_liste)

"""
port_liste=[]
banner_liste=[]
dosya=open("ip.txt","r")
ipler=dosya.read()
dosya.close()
for ip in ipler.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            soket=socket.socket()
            soket.connect((str(ip)),(int(port)))
            banner=soket.recv(1024)
            banner_liste.append(str(banner))
            port_liste.append(str(port))
            soket.close()
            print(port)
            print(banner)
        except:
            print("Şuan burda")
            pass

print(port_liste)
print(banner_liste)
"""

        