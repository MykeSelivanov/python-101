class Person:
    def __init__(self, x) -> None:
        print(x)

p1 = Person(2) # 2
p2 = Person(123) # 123
print(p1) # <__main__.Person object at 0x10a65de20>
print(type(p1)) # <class '__main__.Person'>


class ExtraPerson:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

ep1 = ExtraPerson("Jim", 21)
print(ep1.name, ep1.age) # Jim 21

ep1.name = "Tim"
print(ep1.name) # Tim

ep1.test = "test"
print(ep1.test) # test