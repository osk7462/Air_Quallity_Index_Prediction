# for realtime prediction

from bs4 import BeautifulSoup
from selenium import webdriver

def get_data():
    browse = webdriver.Firefox(executable_path='./geckodriver')
    browse.get("https://www.worldweatheronline.com/lang/en-in/new-delhi-weather/delhi/in.aspx")
    soup = BeautifulSoup(browse.page_source, "html.parser")

    temp = soup.find("div", {"class" : "carousel-cell well text-center"})
    temp = temp.findAll("address")
    temp = temp[0].text
    TM = temp[:2]
    Tm = temp[4:6]




    temp = soup.find("div", {"class": "tb_row tb_temp"})
    temp1 = temp.findAll("div", {"class": "tb_cont_item"})
    i = 0
    total = 0
    for value in temp1:
        if i > 0:
            data = value.text
            total += int(data[:2])
        i += 1
    T = total/4

    temp = soup.find("div",{"class":"col-lg-6 col-md-6 col-sm-6 col-xs-6 text-left"})
    text = temp.text
    text = text.split(" ")
    pp = text[1]
    h = text[3]
    h = h.split("%")
    h = h[0]
    slp = text[4]
    vv = text[7]

    temp = soup.find("div", {"class": "tb_row tb_wind"})
    temp1 = temp.findAll("div", {"class": "tb_cont_item"})
    i = 0
    vm = 0
    total = 0
    for value in temp1:
        if i > 0:
            data = value.text
            total += int(data[:2])
            if vm < int(data[:2]):
                vm = int(data[:2])
        i += 1
    v = total/4
    test = [T,TM,Tm,slp,h,pp,vv,v,vm]
    browse.close()
    return test

