class Human:
    head = True
    _legs = True         # доступ до локального использования
    __arms = True        # обладание уникальные свойства


    def say_hello(self):
        print("Hello")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human):
    arms = False

    # def about(self):
    #     print("Я студент")


class Teacher(Human):
    pass


human = Human()
human.about()

student = Student()
student.about()

# print(dir(human))
# print(dir(student))

print(student._Human__arms)

