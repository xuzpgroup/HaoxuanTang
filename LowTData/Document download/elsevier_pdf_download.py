# -*- coding: utf-8 -*-
import requests
import time
import random

apikey='39a5c442bea9f963195796983fef8d21'
opath="D:/University work/research/Low temperature alloy database/LT_data/6yuebuchong/zhihou/xiazai/pdf_els/test/"
f=open("D:/University work/research/Low temperature alloy database/LT_data/6yuebuchong/zhihou/xiazai/pdf_els/test/els.txt")
fout=open("D:/University work/research/Low temperature alloy database/LT_data/6yuebuchong/zhihou/xiazai/pdf_els/test/elsevier_pdf_download_log.txt","a")
fout.write("-----------------------------------\n")
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
        response=requests.get("https://api.elsevier.com/content/article/doi/"+doi[i]+"?apiKey="+apikey+"&httpAccept=application%2Fpdf")
        print(doi[i]+"  status: "+str(response.status_code)+"\n")
        fout.write(doi[i]+"  status: "+str(response.status_code)+"\n")
    except:
        print(doi[i]+" ERROR\n")
        fout.write(doi[i]+" ERROR\n")
    
    f=open(opath+doiname[i]+".pdf",'wb')
    f.write(response.content)
    f.close()
    lag=random.uniform(0,2)
    time.sleep(lag+1)      
 
fout.close()