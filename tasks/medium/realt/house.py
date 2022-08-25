class House:
    address: str
    area: int
    cost: int

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, cost_up):
        self.cost += cost_up

    def decrease_cost(self, cost_down):
        self.cost += cost_down
