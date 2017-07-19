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
    return max([bar for bar in data], key=lambda bar:bar["SeatsCount"])


def get_smallest_bar(data):
    return min([bar for bar in data], key=lambda bar:bar["SeatsCount"])


def get_vector_length(x1, y1, x2, y2):
    '''Calculate distance between two coordinates'''
    x = abs(float(x1) - float(x2))
    y = abs(float(y1) - float(y2))
    length = math.sqrt(x ** 2 + y ** 2)
    return length


def get_closest_bar(data, user_coord_x, user_coord_y):
    return min([bar for bar in data], key=lambda bar:get_vector_length(user_coord_x,
                                                                       user_coord_y,
                                                                       bar['Latitude_WGS84'],
                                                                       bar['Longitude_WGS84']))


def print_bar_info(bar_size_string, bar_name, seats_count, address):
    print("Самый %s бар называется '%s'. Он рассчитан на %s мест и расположен по адресу: %s." %
          (bar_size_string, bar_name, seats_count, address))


def main():
    json_bar_data = load_data('pubs.json')
    
    biggest_bar = get_biggest_bar(json_bar_data)
    print_bar_info('большой', biggest_bar['Name'], biggest_bar['SeatsCount'], biggest_bar['Address'])
    
    smallest_bar = get_smallest_bar(json_bar_data)
    print_bar_info('маленький', smallest_bar['Name'], smallest_bar['SeatsCount'], smallest_bar['Address'])
    
    raw_coordinates = input("Введите координаты (скопируйте координаты из яндекс.карт в формате 11.111111, "
                            "22.222222):\n", )
    coordinates = raw_coordinates.split(',')
    closest_bar = get_closest_bar(json_bar_data, coordinates[0], coordinates[1])
    print_bar_info('близкий', closest_bar['Name'], closest_bar['SeatsCount'], closest_bar['Address'])


if __name__ == '__main__':
    main()
