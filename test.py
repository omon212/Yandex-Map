import requests

API_KEY = '71792a6e-5159-4720-8edf-11fa8f3a398e'

def get_route(start, end):
    url = 'https://api.routing.yandex.net/v2/route'
    params = {
        'apikey': API_KEY,
        'waypoints': f'{start[1]},{start[0]}|{end[1]},{end[0]}',
        'mode': 'driving'
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and 'routes' in data:
        return data['routes'][0]['legs'][0]['points']
    else:
        raise Exception(f"Yo'lni topishda xatolik yuz berdi: {data}")

def generate_yandex_map_link(start, end):
    start_point = f'{start[1]},{start[0]}'
    end_point = f'{end[1]},{end[0]}'
    link = f'https://yandex.ru/maps/?rtext={start_point}~{end_point}&rtt=auto'
    return link

if __name__ == '__main__':
    start_location = (55.751244, 37.618423)
    end_location = (55.755814, 37.617635)

    try:
        map_link = generate_yandex_map_link(start_location, end_location)
        print(f"Eng yaqin yo'l uchun havola: {map_link}")
    except Exception as e:
        print(e)