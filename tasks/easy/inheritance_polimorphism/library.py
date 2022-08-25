"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:
    fullname: str  # ФИО
    phone: str  # номер телефона

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int  # номер читательского билета
    books: set  # список книг

    def __init__(self, fullname, phone, uid, books=None):
        super().__init__(fullname, phone)
        if books is None:
            books = set()
        self.uid = uid
        self.books = books

    def take_books(self, *args):
        sorted_args = ', '.join(sorted(args))
        self.books.update(args)
        if len(self.books) <= 3:
            return f"{self.fullname} взял(а) книги: {sorted_args}"
        else:
            return f"{self.fullname} взял(а) 4 книги"

    def return_book(self, *args):
        sorted_args = ', '.join(sorted(args))
        if self.books.issuperset(set(args)) and len(set(args)) <= 3:
            return f"{self.fullname} вернул(а) книги:{sorted_args}"
        elif self.books.issuperset(set(args)) and len(set(args)) > 3:
            return f"{self.fullname} вернул(а) 4 книги"
        else:
            raise ValueError(f"{self.fullname} не брал: {set(args).difference(self.books)}")
