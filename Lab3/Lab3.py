# Поведінковий Патерн - Стратегія

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_operation(self, n1, n2):
        pass


class Sum_strategy(Strategy):
    def do_operation(self, n1, n2):
        return n1 + n2


class Sub_strategy(Strategy):
    def do_operation(self, n1, n2):
        return n1 - n2


class Mul_strategy(Strategy):
    def do_operation(self, n1, n2):
        return n1 * n2


class Div_strategy(Strategy):
    def do_operation(self, n1, n2):
        if n2 != 0:
            result_number = n1 / n2
            return result_number
        else:
            raise ValueError("Помилка! На нуль ділити не можна :(")


class Calculator():
    def __init__(self):
        self._first_number = 0
        self._second_number = 0
        self._operation = None

    def __str__(self):
        return f'{self._first_number}, {self._second_number}, {self._operation}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self._first_number}, {self._second_number}, {self._operation})'

    @property
    def first_number(self):
        return self._first_number

    @property
    def second_number(self):
        return self._second_number

    @property
    def operation(self) -> Strategy:
        return self._operation

    @first_number.setter
    def first_number(self, new_number):
        self._first_number = new_number

    @second_number.setter
    def second_number(self, new_number):
        self._second_number = new_number

    @operation.setter
    def operation(self, operation: Strategy) -> None:
        self._operation = operation

    def __call__(self):
        return (self._operation.do_operation(self.first_number, self.second_number))