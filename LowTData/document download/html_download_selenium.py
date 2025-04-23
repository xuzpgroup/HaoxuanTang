# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def html_download(doi):
    if len(doi)<7:
        return
    if (doi[0:7]=='10.1111')or(doi[0:7]=='10.1002'): #wiley':
        base_url = 'http://onlinelibrary.wiley.com/doi/'
        api_url = base_url + doi
    elif doi[0:7]=='10.1088': 
        base_url='https://iopscience.iop.org/article/'
        api_url = base_url + doi
    else:  
        return
    option=ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-automation'])
    option.add_argument("--no-sandbox")
    option.add_argument("--lang=zh-CN")

    option.add_argument("--window-size=1000,800")
    driver=webdriver.Chrome(ChromeDriverManager().install(),options=option)
    driver.get(api_url)

    lag=random.uniform(5,10)
    time.sleep(lag+1)     
    name=doi.replace('/','_')
    f=open('D:/University work/research/Low temperature alloy database/LT_data/6yuebuchong/zhihou/xiazai/html_wiley/'+name+'.html',"w",encoding='utf-8')
    f.write(driver.page_source)
    f.close()
    driver.close()
       

    
    
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

    try:
        html_download(doi[i])
        print('COMPLETED')
    except:
        print('ERROR')