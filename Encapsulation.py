# Encapsulation : binding up of data in a single class. python does not have any private keyword, unlike java.
# A class shouldn't be directly accessed but be prefixed in an underscore.

# class employee(object):
#     def __init__(self):
#         self.name = 1234
#         self.age = 1234
#         self.salary = 1234

# object1 = employee()
# print(object1.name)
# print(object1._age)
# print(object1.__salary)

# explanation : you will get this question what is the underscore and error?? well, python class treats the private variables
# as (__salary) which can not be accessed directly.
# so, I have made use of the setter method which provides indirect access to the in my next example.

class Employee():
    def __init__(self):
        self.__maxearn = 1000000

    def earn(self):
        print("earning is : {}".format(self.__maxearn))

    def setmaxearn(self, earn):  # setter method used for accessing private class
        self.__maxearn = earn

emp1 = Employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setmaxearn(10000)
emp1.earn()