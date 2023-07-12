# 1 Salarios abaixo de 128000 kz recebe um aumento de 20%

# 2 Salarios entre 128000 e 500000 recebe um aumento de 15%

# 3 Salarios entre 500000 e 1000000 recebe um ajuste de 10%

# 4 Salarios acima de 1000000 recebe um ajuste de 5%

salario = float(input("Informe o seu Salário: "))

if salario < 128000:
    percentagem = 0.2
    aumento = salario*percentagem
    novo_salario = salario+aumento
elif salario >= 128000 and salario <=500000:
    percentagem = 0.15
    aumento = salario*percentagem
    novo_salario = salario+aumento
elif salario >=500000 and salario <=1000000:
    percentagem = 0.1
    aumento = salario*percentagem
    novo_salario = salario+aumento
else:
    percentagem = 0.05
    aumento = salario*percentagem
    novo_salario = salario+aumento
print("Salário antes do reajuste: ",salario)
print("Percentagem a ser aplicada: ",percentagem)
print("Aumento a ser aplicado: ",aumento)
print("Novo salário: ",novo_salario)
    
    

