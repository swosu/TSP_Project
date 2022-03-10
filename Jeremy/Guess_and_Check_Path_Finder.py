class Guess_and_Check_Path_Finder:
    def __init__(self, city_count):
        self.data = []
        self.city_count = city_count
        self.cities_to_visit = []
        self.file_name = ''
        self.distance_table = []
        self.path = []

    def say_hello(self):
        #self.say_hello()
        print('So that worked...')

    def find_path(self):
        import random
        self.get_cities_to_visit_list()
        for index in range(0, self.city_count):
            #print(f'our index is {index}.')
            next_city = random.choice(self.cities_to_visit)
            print(f'our next city is: {next_city}.')
            self.path.append(next_city)
            print(f'our current path is: {self.path}.')
            self.cities_to_visit.remove(next_city)
            print(f'remaining cities to visit: {self.cities_to_visit}.')

    def get_cities_to_visit_list(self):
        for index in range(0, self.city_count):
            #print(f'our index is {index}.')
            self.cities_to_visit.append(index)
        print(f'possible cites to visit are: {self.cities_to_visit}.')
