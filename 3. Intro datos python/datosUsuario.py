peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

resultado = peso / (estatura**2)
print(f"{resultado:.2f}")

if resultado < 18.5:
    print("Tu peso está por debajo de lo normal")
elif 18.5 <= resultado <= 24.9:
    print("Tu peso es normal (promedio)")
elif 25 <= resultado <= 29.9:
    print("Tienes sobrepeso (aumentado)")
elif 30 <= resultado <= 34.9:
    print("Tienes obesidad de grado I (moderado)")
elif 35 <= resultado <= 39.9:
    print("Tienes obesidad de grado II (severo)")
else:
    print("Tienes obesidad de grado III (muy severo)")



