#!/usr/bin/env python

class Animal:
    year = 2021
    weight = 0

    def __init__(self, weight):
        self.weight = weight

    @classmethod
    def set_year(cls,year):
        cls.year = year

    @classmethod
    def get_year(cls):
        print(cls)
        print('year',cls.year)
        print('weight',cls.weight)
        

    def get_weight(self):
        print(self)
        print('weight',self.weight)


a = Animal(5)
a.set_year(2020)
a.get_year()
a.get_weight()

b = Animal(10)
b.get_year()
b.get_weight()

print(Animal.year)

public class Animal {
    public static int a()
    public b()
}

Animal bird = new Animal()

L.get_light(id=1)

l1 = LIight()
