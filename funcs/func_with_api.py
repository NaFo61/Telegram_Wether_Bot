from datetime import datetime as dt
from Project_1.config_data.config import RapidAPI_Key_TOKEN, RapidAPI_Host_TOKEN
import requests


def get_coords(query):
    url_coords = "https://weather338.p.rapidapi.com/locations/search"  # Ссылка для получения API ответа

    params = {  # Что хотим получить
        "query": query,
        "language": "ru_RU"
    }

    headers = {  # TOKEN, вспомогательный переменные
        "X-RapidAPI-Key": RapidAPI_Key_TOKEN,
        "X-RapidAPI-Host": RapidAPI_Host_TOKEN
    }

    response = requests.get(url_coords, headers=headers, params=params).json()

    # print(__import__('pprint').pprint(response))

    res = response.get('location', 'Error')
    if res != 'Error':
        latitude = res.get('latitude', 'Error')[0]
        longitude = res.get('longitude', 'Error')[0]

        # print(f"latitude: {latitude}, longitude: {longitude}")
        return (latitude, longitude)
    return 'Error'


def get_forecast(latitude, longitude, data=str(dt.now().date()).replace('-', '')):
    url_forecase = "https://weather338.p.rapidapi.com/weather/forecast"

    params = {
        "date": data,
        "latitude": latitude,
        "longitude": longitude,
        "language": "ru_RU",
        "units": "m"}

    headers = {
        "X-RapidAPI-Key": RapidAPI_Key_TOKEN,
        "X-RapidAPI-Host": RapidAPI_Host_TOKEN
    }

    response = requests.get(url_forecase, headers=headers, params=params).json()

    res = response.get('v3-wx-observations-current', 'Error')
    # print(__import__('pprint').pprint(res))
    if res != 'Error':
        dct_information = {
            'type_of_weather': res.get('cloudCoverPhrase', 'Error'),
            'today_day': res.get('dayOfWeek', 'Error'),
            'altimetr': res.get('pressureAltimeter', 'Error'),
            'snow_detect': res.get('snow24Hour', 'Error'),
            'sun_rise': res.get('sunriseTimeLocal', 'Error'),
            'sun_set': res.get('sunsetTimeLocal', 'Error'),
            'temperature': res.get('temperature', 'Error'),
            'temperature_feel': res.get('temperatureFeelsLike', 'Error'),
            'temperature_max': res.get('temperatureMax24Hour', 'Error'),
            'temperature_min': res.get('temperatureMin24Hour', 'Error'),
            'wind_speed': res.get('windSpeed', 'Error')
        }

        return dct_information
    return 'Error'
    # =============================================================================


def get_information(query):
    res = get_coords(query)
    if res != 'Error':
        latitude, longitude = res
        dct_information = get_forecast(latitude, longitude)
        if dct_information != 'Error':
            dct_information['sun_rise'] = dct_information['sun_rise'][11:19]
            dct_information['sun_set'] = dct_information['sun_set'][11:19]
            return dct_information
        return 'Error'
    return 'Error'
