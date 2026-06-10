#Questao 01
quantidade = int(input("Quantos números deseja informar? "))

lista = []

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    lista.append(numero)

tupla = tuple(lista)

pares = ()

for numero in tupla:
    if numero % 2 == 0:
        pares += (numero,)

print("Tupla original:", tupla)
print("Tupla com os pares:", pares)
