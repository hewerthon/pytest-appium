# Class are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor etc
# objects
# self keyword is mandatory for calling variable names in method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object


class Calculator:
    num = 100

    # default constructor __init__

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    @staticmethod
    def get_data():
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(3, 3)  # syntax to create objects in python
obj.get_data()  # Call method inside class
print(obj.num)  # call values of variable inside class
print(obj.summation())
