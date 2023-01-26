import os

class Program:
    result = 0
    def printOptions(self):
        print("Elija una opción")
        print("1.- suma")
        print("2.- resta")
        print("3.- division")
        print("4.- multiplicacion")
        print("5.- salir")
    
    def doOperation(self, option, a, b):
        match option:
            case (1):
                self.result = a + b 
            case (2):
                self.result = a - b
            case (3):
                self.result = a / b
            case (4):
                self.result = a * b


def main():
    program = Program()
    default = True
    while(default):
        program.printOptions()
        option = int(input("> "))

        if option == 5:
            default = False
            os.system('clear')
        else:
            val1 = int(input("Introdusca el primer valor"))
            val2 = int(input("Introdusca el segundo valor"))
            program.doOperation(option, val1, val2)
            print("El resultado de lo operación es {}".format(program.result))

if __name__ == '__main__':
    main()

