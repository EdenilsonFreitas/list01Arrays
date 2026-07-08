# #Questao 01
# tupla = ()

# quantidade = int(input("Quantos números deseja informar? "))

# for i in range(quantidade):
#     numero = int(input("Digite um número: "))
#     tupla += (numero,)

# pares = ()

# for numero in tupla:
#     if numero % 2 == 0:
#         pares += (numero,)

# print("Tupla original:", tupla)
# print("Tupla com os pares:", pares)

# """
# Escreva um programa que receba uma tupla de strings e exiba uma nova
# tupla com as strings ordenadas alfabeticamente e sem repetições. Por
# exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), o
# programa deve imprimir ("banana", "laranja", "maçã", "uva").
# """

# tupla_strings = ()
# quantidade_strings = int(input("Quantas strings deseja informar? "))

# for i in range(quantidade_strings):
#     string = input("Digite uma string: ")
#     tupla_strings += (string,)

# tupla_unica = set(tupla_strings)
# tupla_ordenada = tuple(sorted(tupla_unica))

# print("Tupla original:", tupla_strings)
# print("Tupla ordenada e sem repetições:", tupla_ordenada)  

#Questao 15
vendas = {}

quantidade = int(input("Quantidade de vendedores: "))

for i in range(quantidade):
    nome = input("Nome do vendedor: ")

    total = 0
    for mes in range(1, 4):
        total += float(input(f"Venda do mês {mes}: "))

    vendas[nome] = total

print("\nRelatório de vendas")
for nome in vendas:
    print(nome, "->", vendas[nome])






































































































































