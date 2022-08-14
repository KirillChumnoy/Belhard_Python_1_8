"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""
from types import FunctionType


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print("Выполнено {func.__name__}")
        return result
    return wrapper


class LogMeta(type):
    def __new__(mcs, clsname, superclasses, attribut):
        new_attribut = {}
        for atr_name, atr_value in attribut.items():
            if isinstance(atr_value, FunctionType):
                atr_value = log_decorator(atr_value)
            new_attribut[atr_name] = atr_value
        new_cls = super().__new__(mcs, clsname, superclasses, new_attribut)
        return new_cls
