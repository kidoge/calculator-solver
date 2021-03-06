"""This module contains the operators supported by calcsolver."""


import abc
from math import copysign


class Operator(object, metaclass=abc.ABCMeta):
    """Abstract base class for all operators."""
    @abc.abstractmethod
    def operate(self, current_number):
        """Performs an operation on the passed value."""
        pass

class OperatorWithNumber(Operator):
    """Abstract base class for operators that have numbers."""
    def __init__(self, value):
        self._value = value

    @abc.abstractmethod
    def operate(self, current_number):
        pass

    @property
    def value(self):
        """Returns the value to add to the current number."""
        return self._value

    def __eq__(self, other):
        return isinstance(other, type(self)) and self._value == other.value


class AddOperator(OperatorWithNumber):
    """Operator that adds a number to the current number."""
    def operate(self, current_number):
        return current_number + self._value

    def __str__(self):
        if self._value > 0:
            sign = "+"
        else:
            sign = "-"
        return "[ %s %d ]" % (sign, abs(self._value))


class MultiplyOperator(OperatorWithNumber):
    """Operator that multiplies the current number by a number."""
    def operate(self, current_number):
        return current_number * self._value

    def __str__(self):
        return "[ * %d ]" % self._value


class DivideOperator(OperatorWithNumber):
    """Operator that divides the current number by a number."""
    def operate(self, current_number):
        if (current_number * 1000 / self._value) % 1 != 0:
            raise ValueError
        return current_number / self._value

    def __str__(self):
        return "[ / %d ]" % self._value

class InsertOperator(OperatorWithNumber):
    """Operator that inserts a number as the lowest significant digit."""
    def operate(self, current_number):
        return copysign(abs(current_number) * 10 + self._value, current_number)

    def __str__(self):
        return "[ %d ]" % self._value
class DiscardOperator(Operator):
    """Operator that discards the lowest significant digit."""
    def operate(self, current_number):
        return int(current_number / 10)

    def __str__(self):
        return "[ << ]"
