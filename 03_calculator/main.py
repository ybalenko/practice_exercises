""" 
English below.
Напишите программу-калькулятор, которая поддерживает следующие операции:
сложение, вычитание, умножение, деление и возведение в степень.
Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
делении на ноль и возведении нуля в отрицательную степень. 

Опишите свой класс исключения. 
Напишите функцию, которая будет выбрасывать данное исключение, если пользователь введёт определённое значение, 
и перехватите это исключение при вызове функции.

Write a calculator that supports the following operations: addition, subtraction, multiplication, division, and power.
The program should raise error messages and continue working when entering incorrect data,
dividing by zero, and raising zero to a negative power.

Describe your exception class. Write a function that will throw this exception if the user enters a certain value,
and catch this exception when the function is called.
"""


class UndefinedResultError(Exception):
    pass


class Calculator():

    def __init__(self):
        pass

    def add(self, x: float, y: float):
        return x + y

    def sub(self, x: float, y: float):
        return x - y

    def multi(self, x: float, y: float):
        return x * y

    def div(self, x: float, y: float):
        if y == 0:
            raise Exception("You cannot divide by zero!")

        return x / y

    def power(self, x: float, y: float):
        # 0 to the power of 0 is a mathematical expression with no agreed-upon value
        if x == 0 and y == 0:
            raise UndefinedResultError(
                "It's a mathematical expression with no agreed-upon value!")
        # 0 to the power of negative one returns error
        if x == 0 and y < 0:
            raise UndefinedResultError("The result is error!")

        return x ** y


def main():

    try:
        x = float(input("Please enter x: "))
        y = float(input("Please enter y: "))
    except ValueError:
        print("You entered a wrong type of x or y")
        exit(1)

    try:
        operator = str(
            input("Please enter one of the following operators: +, -, /, *, ^  "))
    except ValueError:
        print("You entered a wrong type of operator")
        exit(1)

    calc = Calculator()
    actions = {
        "+": calc.add,
        "-": calc.sub,
        "*": calc.multi,
        "/": calc.div,
        "^": calc.power
    }

    if operator not in actions:
        print("You entered a wrong type of operator")
        exit(1)

    try:
        action = actions[operator]
        res = action(x, y)
        print("Your result is", res)
    except:
        print("An error occurred, please try different numbers")


if __name__ == '__main__':
    main()
