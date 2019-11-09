#!/usr/bin/env python
import csv
import time
from datetime import datetime 
import requests
from bs4 import BeautifulSoup



while True:
    page = requests.get("https://banco.santanderrio.com.ar/exec/cotizacion/index.jsp")
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    #print("----------")

    #print(soup.find_all('div', class_='fortable'))
    div_class=soup.find_all('div', class_='fortable')
    #print("----------")
    #print(div_class)

    #print("----------")
    texto=str(div_class)
    #print(texto[25+40+20+20+5:50+70+20-5-3])

    #print("compra")
    compra=texto[110:115]
    #print(compra)
    #print("venta")
    venta=texto[127:132]
    #print(venta)



    # open a csv file with append, so old data will not be erased
    with open("DolarDataBase.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([datetime.now(),compra,venta])

    time.sleep(60*60)# tiempo en segundos
