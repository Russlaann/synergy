# Задание 1

class CashRegister:
    def __init__(self, initial_amount=0):
        self.money = initial_amount

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if x > self.money:
            raise ValueError("Не достаточно денег в кассе")
        self.money -= x


# Задание 2

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("s не может стать ≤ 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s

        return moves_x + moves_y