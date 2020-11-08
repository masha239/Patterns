from stack import Stack
import random


class StackBuilder:

    def set_attack(self, attack: int):
        pass

    def set_defence(self, defence: int):
        pass

    def set_damage(self, damage: int):
        pass

    def set_number(self, number: int):
        pass

    def set_max_health(self, max_health: int):
        pass

    def make_no_retaliation(self):
        pass

    def get_stack(self) -> Stack:
        return Stack()


class ConcreteStackBuilder(StackBuilder):

    def __init__(self):
        self.stack = Stack()

    def set_attack(self, attack: int):
        self.stack._attack = attack

    def set_defence(self, defence: int):
        self.stack._defence = defence

    def set_damage(self, damage: int):
        self.stack._damage = damage

    def set_number(self, number: int):
        self.stack._number = number

    def set_max_health(self, max_health: int):
        self.stack._max_health = max_health
        self.stack._health = max_health

    def make_no_retaliation(self):
        self.stack._retaliation = False

    def get_stack(self) -> Stack:
        return self.stack


class RandomStackBuilder(StackBuilder):

    def __init__(self):
        self.stack = Stack()

    def set_attack(self):
        self.stack._attack = random.randint(1, 25)

    def set_defence(self):
        self.stack._defence = random.randint(1, 25)

    def set_damage(self):
        self.stack._damage = random.randint(1, 60)

    def set_number(self):
        self.stack._number = random.randint(1, 100)

    def set_max_health(self):
        self.stack._max_health = random.randint(1, 200)
        self.stack._health = self.stack._max_health

    def make_no_retaliation(self):
        if random.randint(1, 2) == 0:
            self.stack._retaliation = False

    def get_stack(self) -> Stack:
        return self.stack


