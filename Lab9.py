class Student():
    def __init__(self, name, age, class_, score1, score2, score3, average):
        self.name = name
        self.age = age 
        self.class_ = class_
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.average = (score1+score2+score3)/3

    def __repr__(self):
        return f"Person name = {self.name} , Age = {self.age}, \
        Class = {self.class_}, Average = {self.average}"

person1 = Student("name1", 20, "Maths", 10, 20, 30, "")
person2 = Student("name2", 25, "English", 22, 11, 13, "")
print(repr(person1))
print(repr(person2))

class Bird:
    def __init__(self, name):
        self.name = name
    def output(self):
        print("Type of bird: ", self.name)

class Owl(Bird):
    def __init__(self, name):
        self.name = name
        self.type = "Owl"

class Dodo(Bird):
    def __init__(self, name):
        self.name = name
        self.type = "Dodo"

owl1 = Owl("Owl")
dodo1 = Dodo("Dodo")

owl1.output()
dodo1.output()