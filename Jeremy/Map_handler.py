class Map_handler:
    def __init__(self):
        self.data = []
        self.file_name = ''
        self.distance_table = []

    def say_hello(self):
        #self.say_hello()
        print('So that worked...')

    def make_file_name(self,city_count):
        file_name = f"spp{city_count}.bin"
        return file_name

    def build_map(self, city_count, file_name):
        import numpy as np
        import random
        print("We are going to build a distance table for", city_count, "cities.")
        rows, cols = (city_count, city_count)
        self.distance_table = [[0 for i in range(cols)] for j in range(rows)]

        for rowIndex in range(rows):
            for columnIndex in range(cols):
                self.distance_table[rowIndex][columnIndex] = random.randint(10,99)

        print(self.distance_table)
        np.array(self.distance_table).tofile(file_name)

    def load_map(self, city_count):
        import os.path
        from os import path
        import numpy as np

        print(f'loading map for {city_count} cities.')

        file_name = self.make_file_name(city_count)
        print(f'looking for file {file_name}.')
        print("We want to open file:", file_name)
        if(path.exists(file_name)):
            print ("File exists")
            self.distance_table = np.fromfile(file_name,  dtype=np.int, count = -1)
            self.distance_table = np.reshape(self.distance_table,(city_count,city_count))
            print(self.distance_table)
            #return distance_table
        else:
            print("File does not exist")
            print("Building distance table.")
            self.build_map(city_count,file_name)
            self.load_map(city_count)
