class BoardOutException:
    def __init__(self, dot):
        self.dot = dot
        if self.dot.dotx >= 6 or self.dot.doty >= 6:
            raise BoardOutException('Вы не попали даже в доску!')


class CantPlaceShipException:
    def __init__(self, newship, shiplist):
        self.newship = newship
        self.shiplist = shiplist
        for sh in self.shiplist:
            for d in newship.dotlist():
                if d in sh.dotlist():
                    raise CantPlaceShipException('Не могу тут разместить корабль!')


class SameShotException:
    def __init__(self, dot, dotlist):
        self.dot = dot
        self.dotlist = dotlist
        if dot in dotlist:
            raise SameShotException('В эту клетку уже стреляли!')


class Board:
    def __init__(self,  hid,  size=6):
        self.field = ['0'*size for i in range(size)]
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

    def out(self, dot):
        return not((0 < dot.dotx < self.size) and (0 < dot.doty < self.size))

    def contour(self, ship):
        dotlist = []
        ship_dots = ship.return_dots()
        for i in ship_dots:
            #print(Dot(i.dotx-1, i.doty))
            dotlist.append(Dot(i.dotx - 1, i.doty)) if i in dotlist else:
            dotlist.append(Dot(i.dotx, i.doty - 1))
            dotlist.append(Dot(i.dotx, i.doty + 1))
            dotlist.append(Dot(i.dotx + 1, i.doty))
            dotlist.append(Dot(i.dotx + 1, i.doty + 1))
            dotlist.append(Dot(i.dotx - 1, i.doty - 1))
            dotlist.append(Dot(i.dotx + 1, i.doty - 1))
            dotlist.append(Dot(i.dotx - 1, i.doty + 1))
        for i in ship_dots:
            if i in dotlist:
                dotlist.remove(i)
        #dotlist = list(set(dotlist))    # removing duplicant dots
        return dotlist
