import json
import math
import codecs
import re
import os
import sys


def load_data(filepath):
    with open(filepath, encoding='cp1251') as data:
        string = data.read()
        encoded_string = codecs.encode(string, 'utf-8')
        return json.loads(encoded_string)


def get_biggest_bar(bar_data):
    return max(bar_data, key=lambda bar:bar["SeatsCount"])


def get_smallest_bar(bar_data):
    return min(bar_data, key=lambda bar:bar["SeatsCount"])


def get_vector_length(x1, y1, x2, y2):
    x = abs(float(x1) - float(x2))
    y = abs(float(y1) - float(y2))
    return math.sqrt(x**2 + y**2)


def get_closest_bar(bar_data, user_coordinate):
    return min(bar_data, key=lambda bar:get_vector_length(user_coordinate[0],
                                                          user_coordinate[1],
                                                          bar['Latitude_WGS84'],
                                                          bar['Longitude_WGS84']))


def print_bar_info(bar_size_string, bar_data):
    print("Самый %s бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (bar_size_string, bar_data['Name'], bar_data['SeatsCount'], bar_data['Address']))


def get_coordinates():

    raw_coordinates = input("Введите координаты или скопируйте их из яндекс.карт в формате 11.111111, "
                            "22.222222:\n> ", )
    # check if coordinates in format: (digits)(maybe . and digits)(coma space digits)(maybe . and digits)
    if re.search('\d+\.?\d*\,\s\d+\.?\d*', raw_coordinates) is not None:
        coordinates = raw_coordinates.split(',')
        return coordinates
    else:
        print('Неверный формат координат. ', end='')
        sys.exit()
        


def main():
    try:
        filepath = sys.argv[1]
        json_bar_data = load_data(filepath)

        biggest_bar = get_biggest_bar(json_bar_data)

        print_bar_info('большой', biggest_bar)

        smallest_bar = get_smallest_bar(json_bar_data)
        print_bar_info('маленький', smallest_bar)

        coordinates = get_coordinates()
        closest_bar = get_closest_bar(json_bar_data, coordinates)
        print_bar_info('близкий', closest_bar)
    except FileNotFoundError as error:
        print("%s: %s" % (error.strerror, error.filename))
    except IndexError:
        print("Usage: bars.py [file]")


if __name__ == '__main__':
    main()
