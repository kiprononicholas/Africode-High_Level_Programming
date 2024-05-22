class Person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    
    def introduce(self):
        print(f'my name is {self.name} {self.age} {self.id}.')


# person = Person("ben", 23, "AASMOO2")
# person.introduce()



class Student(Person):
    def study(self):
        print(f"{self.name} {self.age} {self.id} is studing.")


class teacher(Person):
    def teach(self):
        print(f"{self.name} {self.age} {self.id} is teaaching.")


student = Student("nico", 23, "AASSM003")
student.study()

teacher = teacher("ben", 30, "AAASM001")
teacher.teach()





