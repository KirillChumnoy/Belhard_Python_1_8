class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        [tomat.grow() for tomat in self.tomato_list]
        return f"Помидорки зреют"

    def all_are_ripe(self):
        for tomat in self.tomato_list:
            if tomat.ripeness == "Красный":
                return True
            else:
                return False

    def give_away_all(self):
        print(f"Собрано {len(self.tomato_list)} помидора(ов)\nКуст очищен")
        return self.tomato_list.clear()

    def __repr__(self):
        return f"{self.tomato_list}"
