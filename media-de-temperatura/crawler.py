import csv
import requests
from bs4 import BeautifulSoup as bs


r = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp')
texto = r.text
# print(texto)


def acha_temperatura():
    soup = bs(texto, 'html.parser')
    temp_max = soup.find('p', id='tempMax0').text
    temp_min = soup.find('p', id='tempMin0').text
    print(temp_max)
    print(temp_min)
