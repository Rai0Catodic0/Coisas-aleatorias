import requests
r = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp')
texto = r.text
print(r)
