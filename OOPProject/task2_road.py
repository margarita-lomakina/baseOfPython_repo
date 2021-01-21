class Road:
    def __init__(self, len, wid):
        self._length = len
        self._width = wid

    def calculate_pavement(self):
        return self._length * self._width * 5 * 0.025


my_road = Road(5000, 20)
print(f'Требуется {my_road.calculate_pavement()} тонн асфальта.')

