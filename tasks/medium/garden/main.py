from tasks.medium.garden.tomato import Tomato
from tasks.medium.garden.tomato_bush import TomatoBush
from tasks.medium.garden.gardener import Gardener

if __name__ == '__main__':

    pomidorka_1 = Tomato(1)
    pomidorka_2 = Tomato(2)
    pomidorka_3 = Tomato(3)
    pomidorka_4 = Tomato(4)
    pomidorka_5 = Tomato(5)

    kust_pomidorok_1 = TomatoBush(pomidorka_1, pomidorka_3, pomidorka_5)
    kust_pomidorok_2 = TomatoBush(pomidorka_2, pomidorka_4)

    gardener = Gardener('kirill', kust_pomidorok_1, kust_pomidorok_2)
    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.work())
    print(gardener.harvest())
