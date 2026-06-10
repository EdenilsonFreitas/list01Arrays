#Questao 01
tupla = ()

quantidade = int(input("Quantos números deseja informar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    tupla += (numero,)

pares = ()

for numero in tupla:
    if numero % 2 == 0:
        pares += (numero,)

print("Tupla original:", tupla)
print("Tupla com os pares:", pares)