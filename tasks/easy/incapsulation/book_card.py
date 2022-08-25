"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str  # автор
    __title: str  # название книги
    __year: int  # год издания

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.__year == other

    def __lt__(self, other):
        return self.__year < other

    def __gt__(self, other):
        return self.__year > other

    def __ne__(self, other):
        return self.__year != other

    def __le__(self, other):
        return self.__year <= other

    def __ge__(self, other):
        return self.__year >= other

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        if isinstance(val, str):
            self.__author = val
        else:
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        if isinstance(val, str):
            self.__title = val
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if isinstance(val, int) and 0 < val <= CURRENT_YEAR:
            self.__year = val
        else:
            raise ValueError
