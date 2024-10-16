num = float(input("Dígite o primeiro número: "))
num1 = float(input("Dígite o segundo número: "))
num3 = float(input("Dígite o terceiro número: "))

if num > num1 and num > num3:
    print(f"O número {num} é Maior")

elif num1 > num and num1 > num3:
    print(f"O número {num1} é Maior!")

else:
    print(f"O Número {num3} é Maior!!")