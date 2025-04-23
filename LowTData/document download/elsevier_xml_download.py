# -*- coding: utf-8 -*-
import requests
import time
import random


apikey = 'YOUR_KEY'

opath=""
f=open("Elsevier.txt")
fout=open(opath+"elsevier_xml_download_log.txt","a")
doi=[]
doiname=[]
for tmp in f.readlines():
    tmp1=tmp.replace("\n","")
    tmp1=tmp1.replace(" ","")
    doi.append(tmp1)
    doiname.append(tmp1.replace("/","_"))
f.close()

for i in range(0,len(doi)):
    try:
        response=requests.get("https://api.elsevier.com/content/article/doi/"+doi[i]+"?apiKey="+apikey)
        print(doi[i]+"  status: "+str(response.status_code))
    except:
        print(doi[i]+" ERROR")
        fout.write(doi[i]+" ERROR\n")
        
    f=open(opath+doiname[i]+".xml",'w',encoding='utf-8')
    f.write(response.text)
    f.close()
    lag=random.uniform(1,3)
    time.sleep(lag)      
    
fout.close()