import requests
import bs4

weather_minsk = 'https://world-weather.ru/pogoda/belarus/minsk/'
weather_mogilev = 'https://world-weather.ru/pogoda/belarus/mogilev/'
weather_gomel = 'https://world-weather.ru/pogoda/belarus/gomel/'
weather_grodno = 'https://world-weather.ru/pogoda/belarus/grodno/'
weather_vitebsk = 'https://world-weather.ru/pogoda/belarus/vitebsk/'
weather_brest = 'https://world-weather.ru/pogoda/belarus/brest/'

r_minsk = requests.get(weather_minsk)
b_minsk = bs4.BeautifulSoup(r_minsk.text, 'html.parser')
result_minsk = b_minsk.select('span.dw-into')
for i in result_minsk:
    text_result_minsk = i.getText()

r_mogilev = requests.get(weather_mogilev)
b_mogilev = bs4.BeautifulSoup(r_mogilev.text, 'html.parser')
result_mogilev = b_mogilev.select('span.dw-into')
for i in result_mogilev:
    text_result_mogilev = i.getText()

r_gomel = requests.get(weather_gomel)
b_gomel = bs4.BeautifulSoup(r_gomel.text, 'html.parser')
result_gomel = b_gomel.select('span.dw-into')
for i in result_gomel:
    text_result_gomel = i.getText()

r_grodno = requests.get(weather_grodno)
b_grodno = bs4.BeautifulSoup(r_grodno.text, 'html.parser')
result_grodno = b_grodno.select('span.dw-into')
for i in result_grodno:
    text_result_grodno = i.getText()

r_brest = requests.get(weather_brest)
b_brest = bs4.BeautifulSoup(r_brest.text, 'html.parser')
result_brest = b_brest.select('span.dw-into')
for i in result_brest:
    text_result_brest = i.getText()

r_vitebsk = requests.get(weather_vitebsk)
b_vitebsk = bs4.BeautifulSoup(r_vitebsk.text, 'html.parser')
result_vitebsk = b_vitebsk.select('span.dw-into')
for i in result_vitebsk:
    text_result_vitebsk = i.getText()
