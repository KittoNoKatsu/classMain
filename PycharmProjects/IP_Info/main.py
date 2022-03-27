#Библиотеки
import requests
from pyfiglet import Figlet
import folium

# Принятие IP адреса
def get_info_by_ip(ip='127.0.0.1'):
    # Запрос и обработка поступоющей информации
    try:
        #Словарь с данными ip адресса
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #Словарь данных для вывода в терминал
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        #Пробежка по словарю
        for k, v in data.items():
            #Вывод данных на печать
            print(f'{k} : {v}')
        # Определение локации на карте
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        #Сохранения в html файл
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    # В случаи ошибки выводить это
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    #Текст Превью
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    # Просим ip
    ip = input('Please enter a target IP: ')
    # Получаем ip
    get_info_by_ip(ip=ip)

# Вызываем функцию main
if __name__ == '__main__':
    main()