#Questão 01

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# estado = input("Digite seu estado: ")

# dados = (nome, idade, estado)

# print(f"Nome: {dados[0]} Idade: {dados[1]} Estado: {dados[2]}")

#Questão 02

# Leitura dos 4 valores inteiros para os dois pontos
# x1 = int(input("Digite x1: "))
# y1 = int(input("Digite y1: "))
# x2 = int(input("Digite x2: "))
# y2 = int(input("Digite y2: "))

# # Armazenamento dos valores em tuplas
# ponto1 = (x1, y1)
# ponto2 = (x2, y2)

# # Desempacotamento das tuplas em variáveis individuais
# xa, ya = ponto1
# xb, yb = ponto2

# # Cálculo da distância Euclidiana: raiz quadrada de ((xb-xa)^2 + (yb-ya)^2)
# # O expoente 0.5 é utilizado para calcular a raiz quadrada sem importar módulos externos
# distancia = ((xb - xa)**2 + (yb - ya)**2)**0.5

# # Exibição do resultado conforme o formato dos exemplos
# if distancia == int(distancia):
#     print(f"Distância: {int(distancia)}")
# else:
#     print(f"Distância: {distancia:.2f})

#Questão 03

# 1. Leitura dos valores para a tupla de frutas
# f1 = input("Digite a primeira fruta: ")
# f2 = input("Digite a segunda fruta: ")
# f3 = input("Digite a terceira fruta: ")

# # 2. Leitura dos valores para a tupla de vegetais
# v1 = input("Digite o primeiro vegetal: ")
# v2 = input("Digite o segundo vegetal: ")

# # 3. Criação das tuplas individuais
# frutas = (f1, f2, f3)
# vegetais = (v1, v2)

# # 4. Concatenação das duas tuplas em uma nova estrutura
# alimentos = frutas + vegetais

# # 5. Exibição do resultado final formatado
# print(f"Alimentos: {alimentos}")

#Questão 04


# lista = [1,2,3,4,5]

# tupla_original = tuple(lista)

# #  Criamos uma nova tupla com o slice dos três primeiros elementos (índices 0, 1 e 2)
# tupla_slice = tupla_original[:3]

# print(f"Lista original: {lista}")
# print(f"Tupla: {tupla_original}")
# print(f"Slice da tupla: {tupla_slice}")

# Questão 05

# tupla_a = (1, 2, 3, 4, 5)

# pos1 = int(input("Posição 1: "))
# pos2 = int(input("Posição 2: "))

# lista_auxiliar = list(tupla_a)

# aux = lista_auxiliar[pos1]
# lista_auxiliar[pos1] = lista_auxiliar[pos2]
# lista_auxiliar[pos2] = aux

# tupla_b = tuple(lista_auxiliar)

# print(f"Tupla A: {tupla_a}")
# print(f"Tupla B: {tupla_b}")

#Questao 06

# entrada = input("Digite os números separados por espaço: ")
# lista = list(map(int, entrada.split()))

# conjunto = set(lista)

# maior = max(conjunto)

# conjunto.add(maior * 2)

# print(f"Lista: {lista}")
# print(f"Conj: {conjunto}")

# Questao 07

# Leitura dos conjuntos A, B e C
# print("Digite os elementos separados por vírgula (ex: 1,2,3,4)")

# # Conjunto A
# entrada = input("A: ")
# A = set()
# numero = ""
# for caractere in entrada:
#     if caractere != "," and caractere != " ":
#         numero = numero + caractere
#     elif numero != "":
#         A = A | {int(numero)}
#         numero = ""
# if numero != "":
#     A = A | {int(numero)}

# # Conjunto B
# entrada = input("B: ")
# B = set()
# numero = ""
# for caractere in entrada:
#     if caractere != "," and caractere != " ":
#         numero = numero + caractere
#     elif numero != "":
#         B = B | {int(numero)}
#         numero = ""
# if numero != "":
#     B = B | {int(numero)}

# # Conjunto C
# entrada = input("C: ")
# C = set()
# numero = ""
# for caractere in entrada:
#     if caractere != "," and caractere != " ":
#         numero = numero + caractere
#     elif numero != "":
#         C = C | {int(numero)}
#         numero = ""
# if numero != "":
#     C = C | {int(numero)}

# # União: A ∪ B (usando operador |)
# uniao_AB = A | B

# # Diferença: (A ∪ B) - C (usando operador -)
# diferenca = uniao_AB - C

# # Exibe os resultados
# print(f"União: {uniao_AB}")
# print(f"Diferença: {diferenca}")


#Questão 08
# # 1. Solicita a sequência de valores (ex: 1, 9, 3, 2, 3, 6, 4)
# entrada = input("Valores: ")

# # 2. Solicita o divisor
# divisor = int(input("Divisor: "))

# # 3. Cria o primeiro conjunto (Conj 1)
# # O split(',') separa a string pelas vírgulas conforme o exemplo da fonte
# elementos = entrada.split(',')
# conj1 = set()
# for x in elementos:
#     conj1.add(int(x))

# # 4. Cria o segundo conjunto (Conj 2) com a regra de divisibilidade
# conj2 = set()
# for num in conj1:
#     if num % divisor == 0:
#         conj2.add(num)

# # 5. Exibe os resultados conforme o formato solicitado
# print(f"Conj 1: {conj1} Conj 2: {conj2}")

#Questão 09
# # 1. Entrada de dados para o conjunto A
# entrada_a = input("Digite os elementos de A (separados por espaço): ").split()
# A = set()
# for x in entrada_a:
#     # Tenta converter para inteiro, se falhar mantém como string para aceitar letras
#     if x.isdigit():
#         A.add(int(x))
#     else:
#         A.add(x)

# # 2. Entrada de dados para o conjunto B
# entrada_b = input("Digite os elementos de B (separados por espaço): ").split()
# B = set()
# for x in entrada_b:
#     if x.isdigit():
#         B.add(int(x))
#     else:
#         B.add(x)

# # 3. Verifica se B é subconjunto de A
# if B.issubset(A):
#     status = "B é subconjunto de A"
# else:
#     status = "B não é subconjunto de A"

# # 4. Cria o conjunto C com a diferença (A - B)
# C = A.difference(B)

# # 5. Exibição do resultado final conforme o formato do exemplo
# print(f"{status} A: {A} B: {B} C: {C}")

#Questão 10
# 1. Inicializa um conjunto vazio
conjunto = set()

# 2. Loop para preencher o conjunto até encontrar '$$'
while True:
    valor = input("Digite um valor para o conjunto (ou '$$' para parar): ")
    if valor == '$$':
        break
    # Adiciona ao conjunto usando o operador | conforme exigido
    conjunto = conjunto | {int(valor)}

# 3. Inicializa uma lista vazia para os valores de verificação
lista_verificacao = []

# 4. Loop para preencher a lista até encontrar '$$'
while True:
    valor = input("Digite um valor para a lista (ou '$$' para parar): ")
    if valor == '$$':
        break
    # Adiciona à lista via concatenação (evitando .append)
    lista_verificacao += [int(valor)]

# 5. Processamento dos resultados da lista
resultado_lista = ""
for i in range(len(lista_verificacao)):
    item = lista_verificacao[i]
    presenca = "Sim" if item in conjunto else "Não"
    
    # Formata a string de saída com vírgulas entre os itens
    if resultado_lista == "":
        resultado_lista = f"{item}:{presenca}"
    else:
        resultado_lista += f", {item}:{presenca}"

# 6. Exibição final conforme o formato do exemplo
print(f"Conjunto: {conjunto}")
print(f"Lista: {resultado_lista}")



