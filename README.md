# Ближайшие бары

Скрипт парсит json файл с данным по алкогольным заведениям в Москве.
Он находит самый маленький бар, самый большой, 
затем спрашивает координаты и выводит адрес ближайшего бара.

Антон Дёмкин, 2017

antondemkin@yandex.ru

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python

Самый большой бар называется 'Спорт бар «Красная машина»'. Он рассчитан на 450 мест и расположен по адресу: Автозаводская улица, дом 23, строение 1.
Самый маленький бар называется 'БАР. СОКИ'. Он рассчитан на 0 мест и расположен по адресу: Дубравная улица, дом 34/29.
Введите ваши координаты (скопируйте координаты из яндекс.карт в формате 11.111111, 22.222222)
55.787930, 37.694604
Самый близкий бар называется 'Lock Stock'. Он рассчитан на 70 мест и расположен по адресу: Преображенская улица, дом 2.

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
