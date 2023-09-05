# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# решение п. А:

import random
random_songs = random.sample(my_favorite_songs, 3)
total_time = (random_songs[0][1] + random_songs[1][1] + random_songs[2][1])
print(f'Три песни звучат: {round((total_time), 1)} минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение п. В:
    
import random
a = my_favorite_songs_dict.items()
b = list(a)
random_songs_B = random.sample(b, 3)
total_time_B = (random_songs_B[0][1] + random_songs_B[1][1] + random_songs_B[2][1])
print(f'Три песни звучат: {round((total_time_B), 1)} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Решение п. С:

import random
print(random.choice(my_favorite_songs)) 
print(random.choice(b))

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Решение п. D:

import datetime

time_song = my_favorite_songs_dict.get('Easy')
result = str(datetime.timedelta(minutes=time_song))
print(result)