class MyHouse:
    def __init__(self, window_count, door_count, color_name):
        self.windows = window_count
        self.doors = door_count
        self.color = color_name
        self.age = 0

    def age_it(self, years):
        if years < 1:
            print('Wprowadzono zla liczbe')
        else:
            self.age += years

    def doors_and_windows(self):
        return self.windows + self.doors


house1 = MyHouse(5, 10, 'red')
house2 = MyHouse(10, 20, 'green')
house3 = MyHouse(15, 30, 'blue')

print(f'Dom 1, liczba okien: {house1.windows}, liczba drzwi: {house1.doors}, color: {house1.color}, age: {house1.age}')
print(f'Dom 2, liczba okien: {house2.windows}, liczba drzwi: {house2.doors}, color: {house2.color}, age: {house2.age}')
print(f'Dom 3, liczba okien: {house3.windows}, liczba drzwi: {house3.doors}, color: {house3.color}, age: {house3.age}')

print(f'Dom 1 liczba drzwi i okien: {house1.doors_and_windows()}')
print(f'Dom 2 liczba drzwi i okien: {house2.doors_and_windows()}')
print(f'Dom 3 liczba drzwi i okien: {house3.doors_and_windows()}')

