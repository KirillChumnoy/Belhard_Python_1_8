class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        [plant.grow_all() for plant in self.plants]
        return f"Ухаживаем за растениями и смотрим как они зреют"

    def harvest(self):
        all_tomato = []
        for plant in self.plants:
            if plant.all_are_ripe() is False:
                break
            all_tomato.extend(plant.tomato_list)
            plant.give_away_all()
        else:
            return all_tomato
        print(f"Помидорки не созрели")

