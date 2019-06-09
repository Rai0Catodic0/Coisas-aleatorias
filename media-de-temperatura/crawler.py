# encontra a temperatura e salva em um csv
import requests
from bs4 import BeautifulSoup as bs
import time

# criando arquivo csv pra armazenar os dados da tabela
tabela = open('temperaturas.csv', 'w')
tabela.write('dia,temperatura maxima, temperatura minima \n')
# requisição do html do clima tempo
r = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp')
texto = r.text

# função pra encontrar as temperaturas maximas e minimas do dia


def acha_temperatura():
    soup = bs(texto, 'html.parser')
    temp_max = soup.find('p', id='tempMax0').text
    temp_min = soup.find('p', id='tempMin0').text
    return temp_max, temp_min


# função pra salvar a temperatura maxima ,minima e dia no csv


def salva_temp(temp_min, temp_max):
    data = time.localtime()  # data do dia
    tabela.write(str(data[2])+','+temp_min+','+temp_max+'\n')


temp = acha_temperatura()
salva_temp(temp[0], temp[1])
