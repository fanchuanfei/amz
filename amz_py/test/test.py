

class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def say(self):
        print(self._name)

class Man(Student):
    def __init__(self, weight, name, age):
        super().__init__(name, age)
        self.weight = weight

    def football(self):
        print(self._age)

class Women(Student):
    def __init__(self, biutity, name):
        super().__init__(name)
        self.biutity = biutity





print(women.biutity)

student = Student("liu",77)

print(student.name)


