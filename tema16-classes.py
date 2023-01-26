class Operasbas:

    num1 = 0
    num2 = 0
    res = 0

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def suma(self):
        self.res = self.num1 + self.num2

    def restar(self):
        self.res = self.num1 - self.num2


def main():
    obj = Operasbas(3, 4)
    obj.suma()
    print("La suma es: {} ".format(obj.res))

if __name__ == '__main__':
    main()
