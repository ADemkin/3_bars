#
# This scrips parses json file with data for bars in Moscow.
# It finds biggest, smallest and closest bar in a given coordinates.
#
# Anton Demkin, 2017
# antondemkin@yandex.ru
#


import json
import math
import codecs


def load_data(file):
    '''encodes data from cp1251 to utf-8 and load as json'''
    with open(file, encoding='cp1251') as data:
        string = data.read()
        encoded_string = codecs.encode(string, 'utf-8')
        return json.loads(encoded_string)


def get_biggest_bar(data):
    return max((bar['SeatsCount'], bar['Name'], bar['Address']) for bar in data)


def get_smallest_bar(data):
    return min((bar['SeatsCount'], bar['Name'], bar['Address']) for bar in data)


def get_vector_length(x1, y1, x2, y2):
    '''Calculate distance between two coordinates'''
    x = abs(float(x1) - float(x2))
    y = abs(float(y1) - float(y2))
    length = math.sqrt(x ** 2 + y ** 2)
    return length


def get_closest_bar(data, user_coordinates_x, user_coordinates_y):
    closest_bar = None
    best_min_distance = 10000
    for bar in data:
        bar_x = bar['Latitude_WGS84']
        bar_y = bar['Longitude_WGS84']
        if get_vector_length(bar_x, bar_y, user_coordinates_x, user_coordinates_y) < best_min_distance:
            best_min_distance = get_vector_length(bar_x, bar_y, user_coordinates_x, user_coordinates_y)
            closest_bar = bar
    return closest_bar


def print_bar_info(bar_size_string, bar_name, seats_count, address):
    print("Самый %s бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (bar_size_string, bar_name, seats_count, address))


def main():
    json_bar_data = load_data('pubs.json')
    
    biggest_bar = get_biggest_bar(json_bar_data)
    print_bar_info('большой', biggest_bar[1], biggest_bar[0], biggest_bar[2])
    
    smallest_bar = get_smallest_bar(json_bar_data)
    print_bar_info('маленький', smallest_bar[1], smallest_bar[0], smallest_bar[2])
    
    raw_coordinates = input("Введите координаты (скопируйте координаты из яндекс.карт в формате 11.111111, "
                            "22.222222)\n", )
    coordinates = raw_coordinates.split(',')
    closest_bar = get_closest_bar(json_bar_data, coordinates[0], coordinates[1])
    print_bar_info('близкий', closest_bar['Name'], closest_bar['SeatsCount'], closest_bar['Address'])


if __name__ == '__main__':
    main()
