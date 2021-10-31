#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
host = input("Insert IP ")
ports = range  (1,1024)
for port in ports :
     s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
     result = s.connect_ex ((host,port))
     if result == 0:
         print ("Port " + str(port) + " is open ")
     else:
         print ("Port " + str(port) + " is close ")
     s.close()
