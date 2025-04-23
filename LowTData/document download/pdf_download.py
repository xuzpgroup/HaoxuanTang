# -*- coding: utf-8 -*-
import requests
import json
import time
import random

def pdf_download(path,doi):
    global fout
    base_url = 'http://api.crossref.org/works/'
    name=doi.replace('/','_')
    
    f=open(path+name+'.pdf','wb')
    
    api_url = base_url + doi
    
    headers = {
        'Accept': 'application/json'
    }
    
    response = json.loads(requests.get(api_url, headers=headers).text)
    
    pdf_url = response['message']['link'][0]['URL']
    
    app_type = str(response['message']['link'][0]['content-type'])
    
    if app_type in ['application/pdf', 'unspecified']:
        headers = {
            'Accept': 'application/pdf'
        }
        r = requests.get(pdf_url, stream=True, headers=headers)
        if r.status_code == 200:
            for chunk in r.iter_content(2048):
                f.write(chunk)
            print('DOWNLOADED: '+doi)
            fout.write('DOWNLOADED: '+doi+'\n')
        else:
            print('ERROR: '+doi)
            fout.write('ERROR: '+doi+'\n')
    
    f.close()


path=""
f=open(path+"other.txt")
doi=[]
for tmp in f.readlines():
    if '/' in tmp:
        tmp1=tmp.replace("\n","")
        tmp1=tmp1.replace(" ","")
        doi.append(tmp1)
f.close()

fout=open(path+"other_doi.log","w")
for i in range(0,len(doi)):
    #if (i>0)and(len(doi[i])>7)and(len(doi[i-1])>7)and(doi[i-1][0:7]==doi[i][0:7]):
    lag=random.uniform(3,6)
    time.sleep(lag+1) 
    try:
        pdf_download(path,doi[i])
    except:
        print('ERROR0: '+doi[i])
        fout.write('ERROR0: '+doi[i]+'\n')

f.close()

