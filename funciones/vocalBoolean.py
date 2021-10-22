caracter = input("Introduce un caracter: ")
minuscula = caracter.lower()


def vocal(minuscula):
    if minuscula == "a" or minuscula == "e" or minuscula == "i" or minuscula == "o" or minuscula == "u":
        print("True")
    else:
        print("False")


vocal(minuscula)
