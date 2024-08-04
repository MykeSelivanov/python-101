class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def say_hello(self):
        print("Hello, ", self.name)

p1 = Person("Myke")
p1.say_hello()
