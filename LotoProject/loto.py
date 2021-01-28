from random import shuffle, choice, sample


class LotoCard:
    def __init__(self, holder):
        self.holder = holder
        self.card_data = self.create_card()
        self.get_amount = 27

    def create_card(self):
        count = 27
        card = []
        rows = sample(range(1, 90), count)
        n = 0
        for n in range(0, 27, 9):
            row = rows[n:n+9]
            permutations = sorted(range(len(row)), key=lambda k: row[k])
            empty_marks = [0, 0, 0, 0, 1, 1, 1, 1, 1]
            row = sorted(row)
            new_empty_marks = []
            for permutation in permutations:
                new_empty_marks.append(empty_marks[permutation])
            for i, el in enumerate(new_empty_marks):
                if el == 0:
                    row[i] = ''
            card.append(row)
        return card

    def __str__(self):
        return '-'*26 + '\n' + '\n'.join([' '.join(f'{str(el):2}' for el in line) for line in self.card_data]) + '\n' + '-'*26

    def cross(self, number):
        for line in self.card_data:
            if number in line:
                number_id = line.index(number)
                line[number_id] = '-'
                self.get_amount -= 1
                return True
        return False


class LotoGame:
    def __init__(self, player_name, level=2):
        self.card_player = LotoCard(player_name)
        self.card_computer = LotoCard('Компьютер')
        if not level:
            self.level = 2
        else:
            self.level = int(level)
        self.level_dict = {1: 10, 2: 20, 3: 0}

    def print_state(self):
        print(self.card_player.holder)
        print(self.card_player)
        print('Компьютер')
        print(self.card_computer)

    def play(self):
        print('Уровень сложности:', self.level)
        game_list = list(range(1, 91))
        shuffle(game_list)
        for i, tub in enumerate(game_list):
            self.print_state()
            print("Новый бочонок:", tub, "Осталось:", 90 - i - 1)
            move = input('Хотите зачеркнуть? y/n\n')
            if not self.player_move(move, tub):
                print('Вы проиграли')
                break
            elif not self.computer_move(tub):
                print('Вы выиграли')
                break

    def player_move(self, move, tub):
        cross_result = self.card_player.cross(tub)
        if (move == 'y' and not cross_result) or (move == 'n' and cross_result):
            return False
        return True

    def computer_move(self, tub):
        if self.level == 3:
            cross_result = self.card_computer.cross(tub)
            return True
        else:
            move = choice(range(0, self.level_dict[self.level]))
            if move != 0:
                cross_result = self.card_computer.cross(tub)
                return True
        return False


name = input('Это игра лото. Прежде чем начать игруб представьтесь: ')
lev = input('Выберите уровень сложности:\n1 - Easy\n2 - Medium\n3 - Hard\n')
print('Игра началась!')
play_game = LotoGame(name, level=lev)
play_game.play()

