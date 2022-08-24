from tasks.medium.realt.house import House
from tasks.medium.realt.person import Person
from tasks.medium.realt.townhouse import Townhouse

if __name__ == '__main__':
    house_1 = House("Место для отдыха", 86, 7000)
    t_house_1 = Townhouse("Мессто для работы", 60, 9600)
    house_2 = Townhouse("Местечко для души", 10, 500)

    p = Person("Kirill", 38)
    print(p.earn_money(10))
    print(p.make_deal(house_1))
    print(p.earn_money(10000))
    print(p.make_deal(t_house_1))
    print(p.info())
