num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))


def maxTres(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"El {num1} es mayor que {num2} y {num3}")
    elif num2 > num1 and num2 > num3:
        print(f"El {num2} es mayor que {num1} y {num3}")
    else:
        print(f"El {num3} es mayor que {num1} y {num2}")


maxTres(num1,num2,num3)