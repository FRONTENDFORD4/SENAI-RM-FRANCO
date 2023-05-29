salario = float(input("Qual seu salario: "))

if salario > 8250.00:
       novosalario=salario + salario * 0.1
else:
       novosalario=salario + salario * 0.15
       print("Seu aumento foi de: " ,novosalario)