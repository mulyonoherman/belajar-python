#@author RabbitGeex
#Python program to get IP Address

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Nama Komputer Anda adalah:" + hostname)
print("Alamat IP Komputer Anda adalah:" + IPAddr)
