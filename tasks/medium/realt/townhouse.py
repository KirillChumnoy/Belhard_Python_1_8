from tasks.medium.realt.house import House


class Townhouse(House):

    def __init__(self, address, cost, area=60):
        super().__init__(address, cost, area)
