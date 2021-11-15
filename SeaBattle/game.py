from random import randint


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return ' Выстрел за предел доски! '


class CantPlaceShipException(BoardException):
    def __str__(self):
        return ' Не могу тут разместить корабль! '


class SameShotException(BoardException):
    def __str__(self):
        return ' В эту клетку уже стреляли! '


class NotEmplementedError(BoardOutException):
    pass


class Dot:
    def __init__(self, dotx, doty):
        self.dotx = dotx
        self.doty = doty

    def __eq__(self, other):
        return self.dotx == other.dotx and self.doty == other.doty

    def __repr__(self):
        return f'Dot({self.dotx}, {self.doty})'


class Ship:
    def __init__(self, length, nose, direct, lives):
        self.length = length
        self.nose = nose
        self.direct = direct
        self.lives = lives

    def return_dots(self):
        dotlist = []
        for i in range(self.length):
            if self.direct == 0:
                dotlist.append(Dot(self.nose.dotx + i, self.nose.doty))
            if self.direct == 1:
                dotlist.append(Dot(self.nose.dotx, self.nose.doty + i))
        return dotlist

    def hit(self, shot):
        return shot in self.return_dots()


class Board:
    def __init__(self,  hid,  size=6):
        self.field = [['0']*size for i in range(size)]
        self.shiplist = []
        self.hid = hid
        self.shipsalive = 7
        self.size = size
        self.busy = []

    def __str__(self):
        curboard = ''
        curboard += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            curboard += f'\n{i + 1} | ' + ' | '.join(row) + ' |'

        if self.hid:
            curboard = curboard.replace('■', '0')
        return curboard

    def add_ship(self, newship):
        for d in newship.return_dots():
            if self.out(d) or d in self.busy:
                raise CantPlaceShipException('Попробуй в другом месте.')
        for d in newship.return_dots():
            self.field[d.dotx][d.doty] = '■'
            self.busy.append(d)
        self.shiplist.append(newship)
        self.contour(newship)
        # return True

    def contour(self, ship, verb=False):
        ship_dots = ship.return_dots()
        dot_contour = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 0), (0, 1),
                       (1, -1), (1, 0), (1, 1)]
        for i in ship_dots:
            for n1, n2 in dot_contour:
                cur_dot = (Dot(i.dotx + n1, i.doty + n2))
                if not self.out(cur_dot) and cur_dot not in self.busy:
                    if verb:
                        self.field[cur_dot.dotx][cur_dot.doty] = '.'
                    self.busy.append(cur_dot)

#    def hide_ships(self):
#        if self.hid:
#            return []
#        else:
#            return self.shiplist

    def out(self, dot):
        return not((0 <= dot.dotx < self.size) and (0 <= dot.doty < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()
        if dot in self.busy:
            raise SameShotException()
        self.busy.append(dot)

        for ship in self.shiplist:
            if ship.hit(dot):
                ship.lives -= 1
                self.field[dot.dotx][dot.doty] = 'X'
                if ship.lives == 0:
                    self.shipsalive -= 1
                    self.contour(ship, verb=True)
                    print('Корабль потоплен!')
                    return False
                else:
                    print('Корабль ранен!')
                    return True
        self.field[dot.dotx][dot.doty] = '.'
        print('Мимо!')
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotEmplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {dot.dotx + 1}, {dot.doty + 1}')
        return dot


class Person(Player):
    def ask(self):
        while True:
            coords = input('Ход Игрока: ').split()
            if len(coords) != 2:
               print('ВВедите две координаты!')
               continue
            coordx, coordy = coords
            if not coordx.isdigit() or not coordy.isdigit():
                print('Введите две цифры от 1 до 6')
                continue
            coordx, coordy = int(coordx), int(coordy)
            return Dot(coordx - 1, coordy - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        plboard = self.gb_sure()
        aiboard = self.gb_sure()
        aiboard.hid = True

        self.ai = AI(aiboard, plboard)
        self.pl = Person(plboard, aiboard)

    def greet(self):
        print("---=== 'МОРСКОЙ БОЙ' ===---")
        print("---======---===---======---")
        print(" ВВОДИ ООРДИНАТУ 'Х' И 'У' ")

    def gen_board(self):
        ship_lengths = [3, 2, 2, 1, 1, 1, 1]
        board = Board(0, size=self.size)
        tries = 0
        for l in ship_lengths:
            while True:
                tries += 1
                if tries >= 2000:
                    return None
                ship = Ship(l, Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1), l)
                try:
                    board.add_ship(ship)
                    break
                except CantPlaceShipException:
                    pass
        board.begin()
        return board

    def gb_sure(self):
        board = None
        while board is None:
            board = self.gen_board()
        return board

    def print_boards(self):
        print('-----------------------------')
        print(' ---== ДОСКА ИГРОКА ==--- ')
        print(self.pl.board)
        print('-----------------------------')
        print(' ---== ДОСКА КОМПЬЮТЕРА ==--- ')
        print(self.ai.board)
        print('-----------------------------')

    def loop(self):
        turnum = 0
        while True:
            self.print_boards()
            if turnum % 2 == 0:
                print(' ---== ХОД ИГРОКА! ==--- ')
                repeat = self.pl.move()
            else:
                print(' ---== ХОД КОМПЬЮТЕРА! ==--- ')
                repeat = self.ai.move()
            if repeat:
                turnum = -1

            if self.ai.board.shipsalive == 0:
                print('-----------------------------')
                self.print_boards()
                print(' ----=== ВЫ ПОБЕДИЛИ! ===-----')
                break

            if self.pl.board.shipsalive == 0:
                print('-----------------------------')
                self.print_boards()
                print(' ----=== ВЫ ПРОИГРАЛИ! ===-----')
                break

            turnum += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()

