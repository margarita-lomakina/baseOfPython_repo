from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title=None):
        self.title = title

    @abstractmethod
    def count_textile(self):
        pass


class Coat(Clothes):
    def __init__(self, size, title=None):
        super().__init__(title)
        self.size = size

    @property
    def count_textile(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height, title=None):
        super().__init__(title)
        self.height = height

    @property
    def count_textile(self):
        return self.height * 2 + 0.3


clothes_list = [Coat(44, 'Пальто'), Suit(1.75, 'Костюм')]
for obj in clothes_list:
    print(f'Чтобы пошить {obj.title} нужно {obj.count_textile:.2} м ткани')

