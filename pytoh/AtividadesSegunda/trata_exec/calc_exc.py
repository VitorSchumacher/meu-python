

from decimal import DivisionByZero
from msilib.schema import Error


if __name__ == "__main__":
    while True:
        print("1- somar\n2- subtrair\n3- dividir\n4- multiplicar")
        try:
            n1 = int(input("escolha:"))
            try:
                n2 = int(input("numero 1"))
                n3 = int(input("numero 2"))
            except ValueError:
                print("um numero mano!")
        except ValueError:
            print("um numero mano!")
        if n1 == 1:
            try:
                resp = n2+n3
                print(resp)
            except ValueError:
                print("Mano, deu erro aq, me desculpe")
        elif n1 == 2:
            try:
                resp = n2+n3
                print(resp)
            except ValueError:
                print("Mano, deu erro aq, me desculpe")
        elif n1 == 3:
            try:
                resp = n2/n3
                print(resp)
                break
            except ZeroDivisionError:
                print("Mano, deu erro aq, me desculpe")
        elif n1 == 4:
            try:
                resp = n2*n3
                print(resp)
            except ValueError:
                print("Mano, deu erro aq, me desculpe")


