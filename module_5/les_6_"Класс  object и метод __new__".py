# print(int.__mro__)
# print(object)

# # ---------------------
# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         print("Я в нью")
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, *args, **kwargs):  # def __init__(self):
#         print("Я в ините")
#         self.args = args
#         for key, values in kwargs.items():  # self.name = kwargs.get('name')    # self.kwargs = kwargs
#             setattr(self, key, values)  # self.age = kwargs.get('age')
#
#
# # user1 = User()
# # # print(User.__mro__)
# # print(user1)
# # user2 = User()
# # print(user1 is user2)
# # print(id(user1), id(user2))
#
# other = [1, 2, 3]
# user = {'name': 'Den', 'age': 25, 'gender': 'male'}
#
# user1 = User(*other, **user)
# print(user1.args)
# print(user1.name)
# print(user1.age)
# print(user1.gender)

# ------------------
class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)


    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)


ex = Example('data', second=25, third=3.14)
