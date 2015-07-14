#__author__ = 'techxsh'
# -*- coding: utf-8 -*-
import re,os
data = input("输入反转的ascii码：")
asciidata = ""
datalists = re.findall(r"[0-9]{2,3}", data)
#print(datalists)
for datalist in datalists:
    asciidata += chr(int(datalist))
    #print(chr(int(datalist)))
print("反转后的ascii码：\n"+asciidata)
os.system("pause")