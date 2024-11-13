class Human:
    head = False

    # def __init__(self):
    #     self.about()


    def say_hello(self):
        print("Hello")

class Student(Human):
    def about(self):
        print("Я студент")


class Teacher(Human):
    pass

# human = Human()
student = Student()
# print(human.head)
# student.about()
print(student.head)
# human.about()

teacher = Teacher()
teacher.say_hello()
student.say_hello()