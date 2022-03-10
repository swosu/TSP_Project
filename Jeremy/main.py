print('Hello.')
from Map_handler import Map_handler

city_count = 6
print(f'City count is {city_count}.')

print('Load map')
map_handler_object = Map_handler()
map_handler_object.load_map(city_count)

print('Generate path')

print('Get path distance')
