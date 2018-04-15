import  pyowm

print('OpenWeatherMap')

observation=owm.weather_at_place('Rostov-on-Don,ru')
weather=observation.get_weather()
location=observation.get_location()
translate={'Rostov-on-Don':'Ростов-на-Дону','Moscow':'Москва'}

def WhatISCloudness():
    if 0 <= weather.get_clouds() <= 10;
        return'ясная'
    if 10 < weather.get_clouds() <= 30;
        return 'немного облачная'
    if 30 < weather.get_clouds() <= 70;
        return'пасмурная'
    if 70 < weather.get_clouds() <= 100;
        return 'мрачная'

print('Погода в городе'+ translate[location.get_name()]+''+
      WhatISCloudness()+',температура'+
      str(weather.get_temperature('celsius')['temp'])+'градусов цельсия'+
      'скорость ветра'+str(weather.get_wind()['speed'])+'м/с.')
