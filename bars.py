# coding: utf-8
#
# This scrips parses json file with data for bars in Moscow.
# It finds biggest, smallest and closest bar in a given coordinates.
#
# Anton Demkin, 2017
# antondemkin@yandex.ru
#


import json
import math
import pprint

import codecs

file_json = 'moscow_pubs.json'


def load_data(data):
    '''reencodes data from cp1251 to utf-8 and load as json'''
    with open(file_json, encoding='cp1251') as data:
        string = data.read()
        encoded_string = codecs.encode(string, 'utf-8')
        return json.loads(encoded_string)


def get_biggest_bar(data):
    current_max_seats = 0
    biggest_bar = None
    for bar in data:
        if bar['SeatsCount'] > current_max_seats:
            current_max_seats = bar['SeatsCount']
            biggest_bar = bar
    return biggest_bar


def get_smallest_bar(data):
    current_min_seats = 999
    smallest_bar = None
    for bar in data:
        if bar['SeatsCount'] < current_min_seats:
            current_min_seats = bar['SeatsCount']
            smallest_bar = bar
    return smallest_bar


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


def main():
    # load data
    json_bar_data = load_data(file_json)
    # print(pprint.pprint(json_bar_data, indent=4))
    
    # find biggest bar
    biggest_bar = get_biggest_bar(json_bar_data)
    print("Самый большой бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (biggest_bar['Name'], biggest_bar['SeatsCount'], biggest_bar['Address']))
    
    # find smallest bar
    smallest_bar = get_smallest_bar(json_bar_data)
    print("Самый маленький бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (smallest_bar['Name'], smallest_bar['SeatsCount'], smallest_bar['Address']))
    
    # find closest bar
    raw_coordinates = input("Введите ваши координаты (скопируйте координаты из яндекс.карт в формате 11.111111, "
                            "22.222222)\n", )
    coordinates = raw_coordinates.split(',')
    closest_bar = get_closest_bar(json_bar_data, coordinates[0], coordinates[1])
    print("Самый близкий бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (closest_bar['Name'], closest_bar['SeatsCount'], closest_bar['Address']))


if __name__ == '__main__':
    main()
