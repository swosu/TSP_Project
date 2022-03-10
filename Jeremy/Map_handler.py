class Map_handler:
    def __init__(self):
        self.data = []
        self.file_name = ''
        self.distance_matrix = []

    def say_hello(self):
        print('So that worked...')

    def make_file_name(self,city_count):
        #m0016x0016.bin
        short_nugget = str(city_count).zfill(4)
        file_name = "m" + short_nugget + 'x' + short_nugget + '.bin'
        return file_name

    def load_map(self, city_count):
        print(f'loading map for {city_count} cities.')
        self.say_hello()
        file_name = self.make_file_name(city_count)
        print(f'looking for file {file_name}.')
