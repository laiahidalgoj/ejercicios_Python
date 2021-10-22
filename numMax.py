num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))


def num_max(num1, num2):
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    else:
        print(f"El número {num2} es mayor que  {num1}")


num_max(num1, num2)
