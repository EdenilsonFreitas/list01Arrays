#Questão 01

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
estado = input("Digite seu estado: ")

dados = (nome, idade, estado)

print(f"Nome: {dados[0]} Idade: {dados[1]} Estado: {dados[2]}")

#Questão 02


x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))
x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

ponto1 = (x1, y1)
ponto2 = (x2, y2)

xa, ya = ponto1
xb, yb = ponto2

distancia = ((xb - xa)**2 + (yb - ya)**2)**0.5

if distancia == int(distancia):
    print(f"Distância: {int(distancia)}")
else:
    print(f"Distância: {distancia:.2f}")


#Questão 03


f1 = input("Digite a primeira fruta: ")
f2 = input("Digite a segunda fruta: ")
f3 = input("Digite a terceira fruta: ")

v1 = input("Digite o primeiro vegetal: ")
v2 = input("Digite o segundo vegetal: ")

frutas = (f1, f2, f3)
vegetais = (v1, v2)

alimentos = frutas + vegetais

print(f"Alimentos: {alimentos}")

#Questão 04


lista = [1,2,3,4,5]

tupla_original = tuple(lista)

tupla_slice = tupla_original[:3]

print(f"Lista original: {lista}")
print(f"Tupla: {tupla_original}")
print(f"Slice da tupla: {tupla_slice}")

#Questão 05

tupla_a = (1, 2, 3, 4, 5)

pos1 = int(input("Posição 1: "))
pos2 = int(input("Posição 2: "))

lista_auxiliar = list(tupla_a)

aux = lista_auxiliar[pos1]
lista_auxiliar[pos1] = lista_auxiliar[pos2]
lista_auxiliar[pos2] = aux

tupla_b = tuple(lista_auxiliar)

print(f"Tupla A: {tupla_a}")
print(f"Tupla B: {tupla_b}")

#Questao 06

entrada = input("Digite os números separados por espaço: ")
lista = list(map(int, entrada.split()))

conjunto = set(lista)

maior = max(conjunto)

conjunto.add(maior * 2)

print(f"Lista: {lista}")
print(f"Conj: {conjunto}")

#Questao 07


print("Digite os elementos separados por vírgula (ex: 1,2,3,4)")

# Conjunto A
entrada = input("A: ")
A = set()
numero = ""
for caractere in entrada:
    if caractere != "," and caractere != " ":
        numero = numero + caractere
    elif numero != "":
        A = A | {int(numero)}
        numero = ""
if numero != "":
    A = A | {int(numero)}

# Conjunto B
entrada = input("B: ")
B = set()
numero = ""
for caractere in entrada:
    if caractere != "," and caractere != " ":
        numero = numero + caractere
    elif numero != "":
        B = B | {int(numero)}
        numero = ""
if numero != "":
    B = B | {int(numero)}

# Conjunto C
entrada = input("C: ")
C = set()
numero = ""
for caractere in entrada:
    if caractere != "," and caractere != " ":
        numero = numero + caractere
    elif numero != "":
        C = C | {int(numero)}
        numero = ""
if numero != "":
    C = C | {int(numero)}

# União: A ∪ B (usando operador |)
uniao_AB = A | B

# Diferença: (A ∪ B) - C (usando operador -)
diferenca = uniao_AB - C

# Exibe os resultados
print(f"União: {uniao_AB}")
print(f"Diferença: {diferenca}")


#Questão 08

entrada = input("Valores: ")

divisor = int(input("Divisor: "))

elementos = entrada.split(',')
conj1 = set()
for x in elementos:
    conj1.add(int(x))

conj2 = set()
for num in conj1:
    if num % divisor == 0:
        conj2.add(num)

print(f"Conj 1: {conj1} Conj 2: {conj2}")

#Questão 09

entrada_a = input("Digite os elementos de A (separados por espaço): ").split()
A = set()
for x in entrada_a:
    if x.isdigit():
        A.add(int(x))
    else:
        A.add(x)

entrada_b = input("Digite os elementos de B (separados por espaço): ").split()
B = set()
for x in entrada_b:
    if x.isdigit():
        B.add(int(x))
    else:
        B.add(x)
if B.issubset(A):
    status = "B é subconjunto de A"
else:
    status = "B não é subconjunto de A"

C = A.difference(B)

print(f"{status} A: {A} B: {B} C: {C}")

#Questão 10

conjunto = set()

while True:
    valor = input("Digite um valor para o conjunto (ou '$$' para parar): ")
    if valor == '$$':
        break
    conjunto = conjunto | {int(valor)}

lista_verificacao = []

while True:
    valor = input("Digite um valor para a lista (ou '$$' para parar): ")
    if valor == '$$':
        break
    lista_verificacao += [int(valor)]
resultado_lista = ""
for i in range(len(lista_verificacao)):
    item = lista_verificacao[i]
    presenca = "Sim" if item in conjunto else "Não"
    
    if resultado_lista == "":
        resultado_lista = f"{item}:{presenca}"
    else:
        resultado_lista += f", {item}:{presenca}"

print(f"Conjunto: {conjunto}")
print(f"Lista: {resultado_lista}")

#Questao 11

texto = input("Digite o texto: ")

texto_limpo = ""
for char in texto:
    if char != "." and char != ",":
        texto_limpo += char
texto_minusculo = texto_limpo.lower()

palavras = texto_minusculo.split()

contagem = {}

for p in palavras:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1

print(f"Contagem de palavras: {contagem}")

#questao 12

itens = [('banana', 3), ('uva', 5), ('uva', 2), ('banana', 2), ('pêra', 2)]

valores = {}

for fruta, valor in itens:
    
    if fruta in valores:
        
        valores[fruta] += valor
    else:
        
        valores[fruta] = valor

print(f"Lista: {itens}")
print(f"Valores: {valores}")

#questao 13

aluno_nota = {'Ana': 70, 'José': 80, 'João': 20, 'Rita': 20}

nota_aluno = {}

for aluno, nota in aluno_nota.items():
    
    if nota not in nota_aluno:
        
        nota_aluno[nota] = aluno
    else:
        
        if type(nota_aluno[nota]) is list:
            
            nota_aluno[nota].append(aluno)
        else:
            
            nota_aluno[nota] = [nota_aluno[nota], aluno]

print(f"nota_aluno: {nota_aluno}")

#Questão 14
loja1 = {'Item 1': 10, 'Item 2': 5, 'Item 3': 10}
loja2 = {'Item 1': 10, 'Item 2': 2, 'Item 4': 10}

estoque_total = loja1.copy()

for item, quantidade in loja2.items():
    if item in estoque_total:
        estoque_total[item] += quantidade
    else:
        estoque_total[item] = quantidade
print(f"Loja 1: {loja1}")
print(f"Loja 2: {loja2}")
print(f"Estoque: {estoque_total}")

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
