from decimal import Decimal
from datetime import datetime


class WrongOperationError(Exception):
    """"This exception is thrown when there is no specified operation"""
    pass


class City:
    __slots__ = ('name', 'population', 'square', 'year_of_creation')

    def __init__(self, name, population, square: Decimal, year_of_creation) -> None:
        self.name = name
        self.population = population
        self.square = square
        self.year_of_creation = year_of_creation

    def __gt__(self, other):
        if isinstance(other, City) and (self.name == other.name or self.name != other.name):
            return (self.population, self.square, self.year_of_creation) \
                > (other.population, other.square, other.year_of_creation)
        return False

    def __add__(self, other):
        name = self.name + other.name
        population = self.population + other.population
        square = self.square + other.square
        year_of_creation = datetime.now().strftime('%Y')
        return City(name, population, square, year_of_creation)

    def __str__(self):
        return f'City({self.name}, {self.population}, {self.square}, {self.year_of_creation})'

    def __repr__(self):
        return self.__str__()

    def __sub__(self, other):
        return WrongOperationError('Operation subtraction not available')

    def __le__(self, other):
        return WrongOperationError('Operation not available. Please, try other operations')

    def __ge__(self, other):
        return WrongOperationError('Operation not available. Please, try other operations')




city_1 = City('ART', 1000, 450, 1875)
city_2 = City('ArT', 800, 300.01, 1874)
print(city_1<=city_2)