class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        super().draw()
        print(f'Рисование ручкой "{self.title}"...')


class Pencil(Stationary):
    def draw(self):
        super().draw()
        print(f'Рисование карандашом "{self.title}"...')


class Handle(Stationary):
    def draw(self):
        super().draw()
        print(f'Рисование маркером "{self.title}"...')


pen = Pen('Гелевая ручка')
pencil = Pencil('Восковой карандаш')
handle = Handle('Лайнер')
pen.draw()
pencil.draw()
handle.draw()

