nomefunci = input("Digite o nome do funcionário: ")
valorhora = float(input("Digite o valor da hora trabalhada: "))
horastrab = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salariototal = valorhora * horastrab

print(f"O salário total do funcionário {nomefunci} é: R$ {salariototal:.2f}")   
