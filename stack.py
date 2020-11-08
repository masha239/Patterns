class Stack:
    def __init__(self):
        self._number = 1
        self._attack = 1
        self._defence = 1
        self._damage = 1
        self._max_health = 1
        self._health = 1
        self._retaliation = True
        self._is_dead = False

    def get_damage(self, damage: int):
        all_healthpoints = (self._number - 1) * self._max_health + self._health
        all_healthpoints -= damage
        if all_healthpoints <= 0:
            self._is_dead = True
        else:
            self._number = all_healthpoints // self._max_health
            self._health = all_healthpoints % self._max_health
            if self._health == 0:
                self.health = self._max_health


