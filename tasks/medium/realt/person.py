class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        return f"{self.name}, {self.age} , {self.money}$, {self.realty}"

    def earn_money(self, plus):
        self.money += plus
        return self.money

    def make_deal(self, cls):
        if self.money >= cls.cost:
            self.realty.append((cls.address, cls.cost, cls.area))
            self.money -= cls.cost
            return f"Сделка успешно завершена"
        else:
            return f"Недостаточно средств для закрытия сделки"
