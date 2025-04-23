# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import os


    

def html_download(doi,path):
    if len(doi)<7:
        return
    if (doi[0:7]=='10.1111')or(doi[0:7]=='10.1002'): #wiley':
        base_url = 'http://onlinelibrary.wiley.com/doi/'
        api_url = base_url + doi + 'full/'
    elif (doi[0:7]=='10.1007')or(doi[0:7]=='10.1557'): #'springer':
        base_url = 'http://link.springer.com/'
        api_url = base_url + doi + '.html'
    elif doi[0:7]=='10.1108': #'emeraldinsight':
        base_url = 'http://www.emeraldinsight.com/doi/full/'
        api_url = base_url + doi
    elif doi[0:7]=='10.1177': # SAGE
        base_url = 'http://sage.cnpereading.com/paragraph/article/?doi='
        api_url = base_url + doi 
    elif doi[0:7]=='10.1080': # taylor & franics
        base_url = 'https://www.tandfonline.com/doi/full/'
        api_url = base_url + doi 
    else:
        base_url = 'http://api.crossref.org/works/'
        api_url = base_url + doi
        headers = {'Accept': 'application/json'}
        response = json.loads(requests.get(api_url, headers=headers).text)
        api_url = response['message']['resource']['primary']['URL']
    
    name=doi.replace('/','_')
    f=open(path+name+'.html','wb')
    
    headers = {
        'Accept': 'text/html',
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }
    
    r = requests.get(api_url,stream=True,headers=headers)
    if r.status_code == 200:
        for chunk in r.iter_content(2048):
            f.write(chunk)
        print('DOWNLOADED: '+doi)  
    else:
        print('ERROR: '+doi)   
    
    f.close()


        
path=''
f=open("")
doi=[]
doiname=[]
for tmp in f.readlines():
    tmp1=tmp.replace("\n","")
    tmp1=tmp1.replace(" ","")
    doi.append(tmp1)
    doiname.append(tmp1.replace("/","_"))
f.close()

for i in range(0,len(doi)):

    lag=random.uniform(5,10)
    time.sleep(lag+1) 
    try:
        html_download(doi[i],path)
    except:
        print('ERROR0: '+doi[i]+'\n')
  

