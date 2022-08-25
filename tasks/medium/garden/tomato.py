class Tomato:
    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.grow_val = 0
        self.ripeness = self.states[0]

    def grow(self):
        if self.grow_val < len(self.states) - 1:
            self.grow_val += 1
            self.ripeness = self.states[self.grow_val]
        else:
            self.grow_val += 0
        return self.ripeness

    def is_ripe(self):
        if self.ripeness is str('Красный'):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.index}-{self.ripeness}"
