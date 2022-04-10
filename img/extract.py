from bs4 import BeautifulSoup as bs
import urllib.request
import re
import csv
import os

def extract(url,repo,name):
    
    try:
        html_page = urllib.request.urlopen(url)
        soup = bs(html_page,features="html5lib")
        images = []
        for img in soup.findAll('img'):
            images.append(img.get('src'))
        url_final=images[0].split('?')[0]
        urllib.request.urlretrieve(url_final,repo+name+".jpg")
    except:
        print('\nUrl failed '+url)



csv_path = "C:/Users/user/Desktop/Cours 2A/S8 cours/MUC/Work/Mobile-and-Ubiquitous-Computing/meta.csv"

def download_img(path):
    file = open(path)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    file.close()

    #Retrieve url and test if valid before copying
    for i in range(len(rows)):
        compt=0
        place_name=rows[i][1]
        place_id=rows[i][0]
        os.mkdir("C:/Users/user/Desktop/Cours 2A/S8 cours/MUC/Work/Mobile-and-Ubiquitous-Computing/img/"+place_name+"-"+place_id+"/")
        #Split according to ' which will give a lot of wrong url eliminated by validators
        list_url=rows[i][-1].split("'")
        print(list_url)
        for url in list_url:
            if (url!=', ' and url !='"[' and url!=']' and url!='['):
                compt+=1
                extract(url,"C:/Users/user/Desktop/Cours 2A/S8 cours/MUC/Work/Mobile-and-Ubiquitous-Computing/img/"+place_name+"-"+place_id+"/",place_name+str(compt))


download_img(csv_path)