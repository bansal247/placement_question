from abc import ABC, abstractmethod


# Question 1:Create a function in python to read the text file and replace specific content of the file.
def replace_file_content_with(filepath, from_word, with_word):
    with open(filepath, "r+") as file:
        for line in file:
            file.truncate(0)
            file.seek(0)
            file.write(line.replace(from_word, with_word))


# Question 2:Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.
class Vehicle(ABC):
    @abstractmethod
    def movement_type(self):
        pass


class Aeroplane(Vehicle):
    def movement_type(self):
        print("Aeroplane can Fly in the air")


class Ship(Vehicle):
    def movement_type(self):
        print("Ship can Sail in the sea")


class Car(Vehicle):
    def movement_type(self):
        print("Car can be driven on road")


class class_A:
    def m(self):
        print("A")


class class_B(class_A):
    def m(self):
        print("B")


class class_C(class_A):
    pass


def Function(func):
    def inner_funtion():
        print("before function execution")
        func()
        print("after function execution")

    return inner_funtion


def function():
    print("inside the function !!")


if __name__ == '__main__':
    replace_file_content_with('example.txt', "placement", "screening")

    A = Aeroplane()
    A.movement_type()
    S = Ship()
    S.movement_type()
    C = Car()
    C.movement_type()

    a = class_A()
    a.m()
    b = class_B()
    b.m()
    c = class_C()
    c.m()

    function = Function(function)
    function()
