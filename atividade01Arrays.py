#questão 01

numeros = [0] * 10 #criando um array de 10 posições para armazenar os numeros digitados pelo usuario
qtd_pares = 0 #variavel para armazenar a quantidade de numeros pares digitados pelo usuario

for i in range(10): #percorrendo o array para preencher com os numeros digitados pelo usuario
    numeros[i] = int(input(f"Digite o {i + 1}: ")) #preenchendo o array com os numeros digitados pelo usuario

for i in range(10): #percorrendo o array para verificar a quantidade de numeros pares
    if numeros[i] != 0 and numeros[i] % 2 == 0: #verificando se o numero é par e diferente de 0
        qtd_pares += 1 #incrementando a quantidade de numeros pares

print("Qtd valores par:", qtd_pares) #imprimindo a quantidade de numeros pares

#questão 02

tamanho = int(input("Digite o tamanho das listas: "))

lista1 = [0] * tamanho
lista2 = [0] * tamanho

somaPar1 = somaImpar1 = 0
somaPar2 = somaImpar2 = 0

# Preenchendo a primeira lista
for i in range(tamanho):
    lista1[i] = int(input(f"Lista 1 - Valor {i + 1}: "))

    if lista1[i] != 0 and lista1[i] % 2 == 0:
        somaPar1 += lista1[i]
    elif lista1[i] % 2 != 0:
        somaImpar1 += lista1[i]

# Preenchendo a segunda lista
for i in range(tamanho):
    lista2[i] = int(input(f"Lista 2 - Valor {i + 1}: "))

    if lista2[i] != 0 and lista2[i] % 2 == 0:
        somaPar2 += lista2[i]
    elif lista2[i] % 2 != 0:
        somaImpar2 += lista2[i]

# Comparação dos pares
if somaPar1 > somaPar2:
    compPar = ">"
elif somaPar1 < somaPar2:
    compPar = "<"
else:
    compPar = "="

# Comparação dos ímpares
if somaImpar1 > somaImpar2:
    compImpar = ">"
elif somaImpar1 < somaImpar2:
    compImpar = "<"
else:
    compImpar = "="

print(f"Soma pares: {somaPar1} {compPar} {somaPar2}")
print(f"Soma ímpares: {somaImpar1} {compImpar} {somaImpar2}")

#questão 03

# 1. Pre-alocação da lista com 10 posições 
lista = [0] * 10
qtd_primos = 0

# 2. Leitura dos 10 valores inteiros
for i in range(10):
    lista[i] = int(input(f"Digite o {i+1}º valor: "))

# 3. Lógica para verificar cada número da lista
for i in range(10):
    valor = lista[i]
    
    # Números menores ou iguais a 1 não são primos
    if valor > 1:
        eh_primo = True
        
        # 4. Verifica se existe algum divisor entre 2 e o próprio número
        for divisor in range(2, valor):
            if valor % divisor == 0:
                eh_primo = False # Encontrou um divisor, então não é primo
                break
        
        # 5. Se a flag eh_primo continuou True, incrementa o contador
        if eh_primo:
            qtd_primos += 1

# 6. Saída formatada conforme o exemplo da fonte
print(f"Quantidade de valores primos: {qtd_primos}")

#questão 04

# 1. Leitura do tamanho das listas
n = int(input("Digite a quantidade de elementos: "))

# 2. Inicialização das listas com tamanho fixo (pre-alocação)
lista1 = [None] * n
lista2 = [None] * n
lista3 = [None] * (n * 2) # A lista resultante terá o dobro do tamanho

# 3. Preenchimento da primeira lista
for i in range(n):
    lista1[i] = input(f"Elemento {i+1} da lista 1: ")

# 4. Preenchimento da segunda lista
for i in range(n):
    lista2[i] = input(f"Elemento {i+1} da lista 2: ")

# 5. Lógica de intercalação manual
for i in range(n):
    # Posição par da lista3 recebe o elemento da lista1
    lista3[i * 2] = lista1[i]
    # Posição ímpar da lista3 recebe o elemento da lista2
    lista3[i * 2 + 1] = lista2[i]

# 6. Saída formatada conforme o exemplo da fonte
print(f"lista1 = {lista1}    lista2 = {lista2}    lista3 = {lista3}")



#questão 05
#Leitura da quantidade
n = int(input("Digite a quantidade de elementos: "))
vetor = [0] * n

# Preenchimento e Soma (para a média)
soma = 0
for i in range(n):
    vetor[i] = int(input(f"Digite o {i+1}º elemento: "))
    soma += vetor[i]

# Inicialização do menor e maior com o primeiro elemento
menor = vetor[0]
maior = vetor[0]

# Laço para identificar menor e maior
for i in range(1, n): #começa do segundo elemento, pois o primeiro já foi usado para inicializar menor e maior
    if vetor[i] < menor:
        menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]

# Cálculo da média
media = soma / n

# Saída formatada conforme o exemplo da fonte
print(f"Menor valor: {menor} Maior valor: {maior} Média aritmética: {int(media)}")


#questão 06

n01 = int(input("Informe a quantidade de elementos: "))

# 2. Inicialização da lista com tamanho fixo
lista = [None] * n01

# 3. Leitura dos números inteiros para preencher a lista
for i in range(n01):
    lista[i] = int(input(f"Digite o número para o índice {i}: "))

# 4. Leitura da string (que deve ter o mesmo comprimento 'n')
texto = input("Digite a string de mesmo comprimento: ")

# 5. Lógica de substituição nos índices ímpares
for i in range(n01):
    # Verifica se o índice atual é ímpar
    if i % 2 != 0:
        # Substitui o número pelo caractere da string na mesma posição
        lista[i] = texto[i]

# 6. Saída formatada: exibe os elementos separados por um espaço em branco
for i in range(n01):
    print(lista[i], end=" ")


#questão 07
# 1. Leitura e Inicialização
n02 = int(input("Quantos valores serão fornecidos? "))
lista = [0] * n02

for i in range(n02):
    lista[i] = int(input(f"Valor {i+1}: "))

# 2. Ordenação Manual (Bubble Sort) - Essencial para a Mediana
for i in range(n02):
    for j in range(0, n02 - i - 1):
        if lista[j] > lista[j + 1]:
            # Troca de posição (Swap)
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

# 3. Cálculo da Mediana
if n02 % 2 != 0:
    # Se a quantidade é ímpar, pega o valor do meio
    mediana = lista[n02 // 2]
else:
    # Se for par, faz a média dos dois valores centrais
    mediana = (lista[n02 // 2 - 1] + lista[n02 // 2]) / 2

# 4. Cálculo da Moda
maior_frequencia = 0
valor_moda = None
amodal = True

for i in range(n02):
    contagem = 0
    # Conta quantas vezes o valor atual aparece na lista
    for j in range(n02):
        if lista[j] == lista[i]:
            contagem += 1
    
    # Verifica se este valor aparece mais vezes que os anteriores
    if contagem > maior_frequencia:
        maior_frequencia = contagem
        valor_moda = lista[i]

# Se a maior frequência for 1, o conjunto não tem repetições (amodal)
if maior_frequencia <= 1:
    resultado_moda = "amodal"
else:
    resultado_moda = valor_moda
    amodal = False

# 5. Saída formatada conforme o exemplo da fonte
if amodal:
    # Nota: O exemplo 2 da fonte mostra "Média aritmética" na saída da Q7, 
    # mas o enunciado pede a Mediana. Seguiremos o enunciado principal.
    print(f"Moda: {resultado_moda} Mediana: {mediana}")
else:
    print(f"Moda: {resultado_moda} Mediana: {mediana}")


#questão 08


# # 1. Leitura da string com os números
entrada = input("Digite os números separados por espaço: ")

# 2. Contagem manual de elementos para pre-alocação 
qtd_elementos = 1
for caracter in entrada:
    if caracter == " ":
        qtd_elementos += 1

# 3. Criação da lista com tamanho fixo 
lista = [0] * qtd_elementos

# 4. Lógica para converter a string em lista de inteiros manualmente
numero_atual_str = ""
indice_lista = 0

for i in range(len(entrada)):
    if entrada[i] != " ":
        numero_atual_str += entrada[i]
    
    # Se encontrar um espaço ou chegar no último caractere, salva o número
    if entrada[i] == " " or i == len(entrada) - 1:
        lista[indice_lista] = int(numero_atual_str)
        indice_lista += 1
        numero_atual_str = ""

# 5. Soma das posições ímpares e montagem da string de saída
soma_total = 0
calculo_visual = ""

for i in range(qtd_elementos):
    # Verifica se o índice é ímpar (1, 3, 5...)
    if i % 2 != 0:
        soma_total += lista[i]
        
        # Monta a parte visual (ex: "9+2+9")
        if calculo_visual == "":
            calculo_visual += str(lista[i])
        else:
            calculo_visual += "+" + str(lista[i])

# 6. Saída formatada conforme o exemplo da fonte
print(f"{calculo_visual} = {soma_total}")

#questão 09

# 1. Entrada de dados
texto = input("Digite o texto: ")

# 2. Limpeza manual de pontuação 
texto_limpo = ""
for char in texto:
    if char != "." and char != ",":
        texto_limpo += char

# 3. Contagem de palavras para pre-alocação 
qtd_palavras = 0
if texto_limpo != "":
    qtd_palavras = 1
    for char in texto_limpo:
        if char == " ":
            qtd_palavras += 1

# 4. Criação da lista e separação manual das palavras
palavras = [None] * qtd_palavras
palavra_temp = ""
posicao = 0

for i in range(len(texto_limpo)):
    if texto_limpo[i] != " ":
        palavra_temp += texto_limpo[i]
    
    # Se encontrar espaço ou for o fim da string, armazena a palavra
    if texto_limpo[i] == " " or i == len(texto_limpo) - 1:
        if palavra_temp != "":
            palavras[posicao] = palavra_temp
            posicao += 1
            palavra_temp = ""

# 5. Contagem de frequências e formatação da saída
saida = ""
for i in range(qtd_palavras):
    # Verifica se a palavra já foi processada anteriormente para não repetir na saída
    ja_processada = False
    for k in range(i):
        if palavras[k] == palavras[i]:
            ja_processada = True
            break
    
    if not ja_processada:
        contagem = 0
        # Conta quantas vezes a palavra atual aparece na lista inteira
        for j in range(qtd_palavras):
            if palavras[j] == palavras[i]:
                contagem += 1
        
        # Monta a string de saída conforme o exemplo: "palavra=X; "
        if saida == "":
            saida += f"{palavras[i]}={contagem}"
        else:
            saida += f"; {palavras[i]}={contagem}"

# 6. Exibição do resultado final
print(saida)

#questão 10

# 1. Inicialização da Matriz 3x3 (Pre-alocação)
# Criamos uma lista contendo 3 listas, cada uma com 3 posições
matriz = [[0,0,0], [0,0,0], [0,0,0]]
qtd_impares = 0

# 2. Leitura dos dados usando laços aninhados
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite o valor para [{linha}][{coluna}]: "))
        matriz[linha][coluna] = valor
        
        # 3. Verificação de números ímpares
        # Se o resto da divisão por 2 for diferente de zero, o número é ímpar
        if valor % 2 != 0:
            qtd_impares += 1

# 4. Saída formatada da Matriz
print("Matriz:")
for linha in range(3):
    for coluna in range(3):
        # O argumento end=" " mantém os números na mesma linha
        print(matriz[linha][coluna], end=" ")
    print() # Pula para a próxima linha após imprimir uma fileira completa

# 5. Exibição da contagem final
print(f"Quantidade de números ímpares: {qtd_impares}")

#questão 11

# 1. Leitura das dimensões da matriz
m = int(input("Informe a quantidade de linhas (m): "))
n = int(input("Informe a quantidade de colunas (n): "))

# 2. Inicialização da matriz m x n (Pre-alocação)

matriz = [None] * m
for i in range(m):
    matriz[i] = [None] * n

# 3. Leitura e armazenamento dos valores inteiros
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f"Valor para a posição [{i}][{j}]: "))

# 4. Processamento: Exibição da matriz e soma de cada LINHA
for i in range(m):
    soma_linha = 0
    # Percorre cada coluna da linha atual para imprimir e somar
    for j in range(n):
        print(matriz[i][j], end=" ")
        soma_linha += matriz[i][j] # Acumula o valor manualmente (sem sum())
    
    # Imprime o sinal de igual e o resultado final daquela linha
    print(f"= {soma_linha}")


#Questão 12

# # Solicita as dimensões da matriz
m = int(input("Informe a quantidade de linhas: "))
n = int(input("Informe a quantidade de colunas: "))

# Inicializa a matriz com zeros (m x n)
matriz = [ [0] * n for _ in range(m) ]

# Preenchimento da matriz com valores informados pelo usuário
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f"Valor para [{i}][{j}]: "))

# Exibe os elementos da matriz em sequência (conforme os exemplos)
for i in range(m):
    for j in range(n):
        print(matriz[i][j], end=" ")

# Cálculo e exibição da soma de cada coluna
for j in range(n):
    soma_coluna = 0
    for i in range(m):
        soma_coluna += matriz[i][j]
    print(f"Coluna{j+1}: {soma_coluna}", end=" ")

#questao 13

# Inicialização das matrizes 3x3 com zeros 
matriz_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Leitura dos valores para a Matriz A
for i in range(3):
    for j in range(3):
        matriz_a[i][j] = int(input(f"Digite valor para A[{i}][{j}]: "))

# Leitura dos valores para a Matriz B
for i in range(3):
    for j in range(3):
        matriz_b[i][j] = int(input(f"Digite valor para B[{i}][{j}]: "))

# Comparação e preenchimento da Matriz C com os maiores valores
for i in range(3):
    for j in range(3):
        if matriz_a[i][j] > matriz_b[i][j]:
            matriz_c[i][j] = matriz_a[i][j]
        else:
            matriz_c[i][j] = matriz_b[i][j]

# Exibição da Matriz C resultante
for i in range(3):
    for j in range(3):
        print(matriz_c[i][j], end=" ")


#questão 14
# Inicializa a matriz 4x4 com zeros 
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Preenchimento da matriz com entradas do usuário
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Valor para [{i}][{j}]: "))

soma = 0
termos = "" # Para armazenar a exibição "6 + 8 + 14 + 16"

# Processamento da soma conforme os índices do exemplo
for i in range(4):
    for j in range(4):
        # Verifica se o índice da linha e da coluna são ímpares (1 ou 3)
        if i % 2 != 0 and j % 2 != 0:
            valor = matriz[i][j]
            soma += valor
            # Lógica para construir a string de saída
            if termos == "":
                termos = str(valor)
            else:
                termos += " + " + str(valor)

# Exibe o resultado final formatado
print(f"Resultado: {termos} = {soma}")

#questão 15

# # Solicita as dimensões da matriz
m = int(input("Informe a quantidade de linhas (2 a 10): "))
n = int(input("Informe a quantidade de colunas (2 a 10): "))

# Inicializa a matriz pré-alocada com zeros 
matriz = [[0] * n for _ in range(m)]

# Preenchimento da matriz com valores informados pelo usuário
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite o valor para [{i}][{j}]: "))

# Exibição da matriz completa em uma única linha 
for i in range(m):
    for j in range(n):
        print(matriz[i][j], end=" ")
print()  # Quebra de linha após exibir a matriz

# Lógica manual para encontrar o maior, o menor e suas posições
# CORREÇÃO: inicializa com o primeiro elemento da matriz
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(m):
    for j in range(n):
        # Comparação manual para o maior valor
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        
        # Comparação manual para o menor valor
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

# Exibição final conforme o formato solicitado
print(f"Menor valor: {menor} {pos_menor} Maior valor: {maior} {pos_maior}")

# #questão 16

# # Inicialização das matrizes 3x3 com zeros 
matriz_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_r = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Leitura dos valores para a Matriz A
for i in range(3):
    for j in range(3):
        matriz_a[i][j] = int(input(f"Valor para A[{i}][{j}]: "))

# Leitura dos valores para a Matriz B
for i in range(3):
    for j in range(3):
        matriz_b[i][j] = int(input(f"Valor para B[{i}][{j}]: "))

# Cálculo do Produto Matricial (R = A x B)
for i in range(3):
    for j in range(3):
        soma_produto = 0
        for k in range(3):
            soma_produto += matriz_a[i][k] * matriz_b[k][j]
        matriz_r[i][j] = soma_produto

# Exibição dos resultados
print("\nMatriz A:")
for i in range(3):
    for j in range(3):
        print(matriz_a[i][j], end=" ")
    print()

print("\nMatriz B:")
for i in range(3):
    for j in range(3):
        print(matriz_b[i][j], end=" ")
    print()

print("\nMatriz Resultante:")
for i in range(3):
    for j in range(3):
        print(matriz_r[i][j], end=" ")
    print()

#questao 17

# # 1. Solicita as dimensões das duas matrizes
j = int(input("Informe as linhas da Matriz A: "))
k = int(input("Informe as colunas da Matriz A: "))
m = int(input("Informe as linhas da Matriz B: "))
n = int(input("Informe as colunas da Matriz B: "))

# 2. Inicializa as matrizes com zeros (sem usar .append)
matriz_a = [ [0] * k for _ in range(j)]
matriz_b = [ [0] * n for _ in range(m)]

# 3. Leitura dos valores da Matriz A
for i in range(j):
    for c in range(k):
        matriz_a[i][c] = int(input(f"Valor para A[{i}][{c}]: "))

# 4. Leitura dos valores da Matriz B
for i in range(m):
    for c in range(n):
        matriz_b[i][c] = int(input(f"Valor para B[{i}][{c}]: "))

# 5. Verifica se o produto matricial é possível (k deve ser igual a m)
if k == m:
    # Inicializa a matriz resultante (j x n)
    matriz_r = [ [0] * n for _ in range(j)]
    
    # 6. Cálculo do produto matricial
    for i in range(j): # Percorre linhas de A
        for col in range(n): # Percorre colunas de B
            soma_prod = 0
            for x in range(k): # Realiza o somatório dos produtos
                soma_prod += matriz_a[i][x] * matriz_b[x][col]
            matriz_r[i][col] = soma_prod

    # 7. Exibição dos resultados (Matrizes A, B e Resultante)
    print("\nMatriz A:")
    for i in range(j):
        for c in range(k):
            print(matriz_a[i][c], end=" ")
        print()

    print("\nMatriz B:")
    for i in range(m):
        for c in range(n):
            print(matriz_b[i][c], end=" ")
        print()

    print("\nMatriz Resultante:")
    for i in range(j):
        for c in range(n):
            print(matriz_r[i][c], end=" ")
        print()
else:
    # 8. Caso não seja possível realizar o produto
    print("\nImpossibilidade de realizar o produto matricial.")
    print("Matriz A:")
    for i in range(j):
        for c in range(k):
            print(matriz_a[i][c], end=" ")
        print()
    print("\nMatriz B:")
    for i in range(m):
        for c in range(n):
            print(matriz_b[i][c], end=" ")
        print()


#Questao 18

# 1. Inicializa a matriz 3x6 e uma cópia para preservar a original
matriz = [[0.0] * 6 for _ in range(3)]
original = [[0.0] * 6 for _ in range(3)]

# 2. Leitura dos valores reais
for i in range(3):
    for j in range(6):
        valor = float(input(f"Digite o valor para [{i}][{j}]: "))
        matriz[i][j] = valor
        original[i][j] = valor # Salva na cópia para exibir depois

# 3. Soma dos elementos das colunas ímpares (1ª, 3ª e 5ª -> índices 0, 2, 4)
soma_col_impares = 0
for i in range(3):
    for j in [1, 2]:
        soma_col_impares += matriz[i][j]

# 4. Média aritmética da segunda e quarta colunas (índices 1 e 3)
soma_media = 0
for i in range(3):
    soma_media += matriz[i][3] + matriz[i][4]
media = soma_media / 6 # 3 elementos em cada uma das 2 colunas = 6 elementos

# 5. Substituir a sexta coluna (índice 5) pela soma das colunas 4 e 5 (índices 3 e 4)
for i in range(3):
    matriz[i][5] = matriz[i][4] + matriz[i][2]

# 6. Exibição dos resultados e das matrizes
print(f"\nSoma das colunas ímpares: {soma_col_impares}")
print(f"Média da 2ª e 4ª colunas: {media:.2f}")

print("\nMatriz Original:")
for i in range(3):
    for j in range(6):
        print(original[i][j], end=" ")
    print()

print("\nMatriz Modificada:")
for i in range(3):
    for j in range(6):
        print(matriz[i][j], end=" ")
    print()
