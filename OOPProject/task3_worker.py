class Worker:
    def __init__(self, worker_name, worker_surname, worker_position):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income = {'wage': 0, 'bonus': 0}

    def set_income(self, wage=0, bonus=0):
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


my_position = Position('John', 'Smith', 'Front-end developer')
my_position.set_income(wage=100000, bonus=15000)
print(my_position.name, my_position.surname, my_position.position)
print(f'{my_position.get_full_name()}: {my_position.get_total_income()}')

