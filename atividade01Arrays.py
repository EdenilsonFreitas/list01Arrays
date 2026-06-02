#questão 01

# numeros = [0] * 10 #criando um array de 10 posições para armazenar os numeros digitados pelo usuario
# qtd_pares = 0 #variavel para armazenar a quantidade de numeros pares digitados pelo usuario

# for i in range(10): #percorrendo o array para preencher com os numeros digitados pelo usuario
#     numeros[i] = int(input(f"Digite o {i + 1}: ")) #preenchendo o array com os numeros digitados pelo usuario

# for i in range(10): #percorrendo o array para verificar a quantidade de numeros pares
#     if numeros[i] != 0 and numeros[i] % 2 == 0: #verificando se o numero é par e diferente de 0
#         qtd_pares += 1 #incrementando a quantidade de numeros pares

# print("Qtd valores par:", qtd_pares) #imprimindo a quantidade de numeros pares

#questão 02

# tamanho = int(input("Digite o tamanho das listas: "))

# lista1 = [0] * tamanho
# lista2 = [0] * tamanho

# somaPar1 = somaImpar1 = 0
# somaPar2 = somaImpar2 = 0

# # Preenchendo a primeira lista
# for i in range(tamanho):
#     lista1[i] = int(input(f"Lista 1 - Valor {i + 1}: "))

#     if lista1[i] != 0 and lista1[i] % 2 == 0:
#         somaPar1 += lista1[i]
#     elif lista1[i] % 2 != 0:
#         somaImpar1 += lista1[i]

# # Preenchendo a segunda lista
# for i in range(tamanho):
#     lista2[i] = int(input(f"Lista 2 - Valor {i + 1}: "))

#     if lista2[i] != 0 and lista2[i] % 2 == 0:
#         somaPar2 += lista2[i]
#     elif lista2[i] % 2 != 0:
#         somaImpar2 += lista2[i]

# # Comparação dos pares
# if somaPar1 > somaPar2:
#     compPar = ">"
# elif somaPar1 < somaPar2:
#     compPar = "<"
# else:
#     compPar = "="

# # Comparação dos ímpares
# if somaImpar1 > somaImpar2:
#     compImpar = ">"
# elif somaImpar1 < somaImpar2:
#     compImpar = "<"
# else:
#     compImpar = "="

# print(f"Soma pares: {somaPar1} {compPar} {somaPar2}")
# print(f"Soma ímpares: {somaImpar1} {compImpar} {somaImpar2}")

#questão 03

# # 1. Pre-alocação da lista com 10 posições 
# lista = [0] * 10
# qtd_primos = 0

# # 2. Leitura dos 10 valores inteiros
# for i in range(10):
#     lista[i] = int(input(f"Digite o {i+1}º valor: "))

# # 3. Lógica para verificar cada número da lista
# for i in range(10):
#     valor = lista[i]
    
#     # Números menores ou iguais a 1 não são primos
#     if valor > 1:
#         eh_primo = True
        
#         # 4. Verifica se existe algum divisor entre 2 e o próprio número
#         for divisor in range(2, valor):
#             if valor % divisor == 0:
#                 eh_primo = False # Encontrou um divisor, então não é primo
#                 break
        
#         # 5. Se a flag eh_primo continuou True, incrementa o contador
#         if eh_primo:
#             qtd_primos += 1

# # 6. Saída formatada conforme o exemplo da fonte
# print(f"Quantidade de valores primos: {qtd_primos}")

#questão 04

# 1. Leitura do tamanho das listas
# n = int(input("Digite a quantidade de elementos: "))

# # 2. Inicialização das listas com tamanho fixo (pre-alocação)
# lista1 = [None] * n
# lista2 = [None] * n
# lista3 = [None] * (n * 2) # A lista resultante terá o dobro do tamanho

# # 3. Preenchimento da primeira lista
# for i in range(n):
#     lista1[i] = input(f"Elemento {i+1} da lista 1: ")

# # 4. Preenchimento da segunda lista
# for i in range(n):
#     lista2[i] = input(f"Elemento {i+1} da lista 2: ")

# # 5. Lógica de intercalação manual
# for i in range(n):
#     # Posição par da lista3 recebe o elemento da lista1
#     lista3[i * 2] = lista1[i]
#     # Posição ímpar da lista3 recebe o elemento da lista2
#     lista3[i * 2 + 1] = lista2[i]

# # 6. Saída formatada conforme o exemplo da fonte
# print(f"lista1 = {lista1}    lista2 = {lista2}    lista3 = {lista3}")



#questão 05
# Leitura da quantidade
# n = int(input("Digite a quantidade de elementos: "))
# vetor = [0] * n

# # Preenchimento e Soma (para a média)
# soma = 0
# for i in range(n):
#     vetor[i] = int(input(f"Digite o {i+1}º elemento: "))
#     soma += vetor[i]

# # Inicialização do menor e maior com o primeiro elemento
# menor = vetor[0]
# maior = vetor[0]

# # Laço para identificar menor e maior
# for i in range(1, n): #começa do segundo elemento, pois o primeiro já foi usado para inicializar menor e maior
#     if vetor[i] < menor:
#         menor = vetor[i]
#     if vetor[i] > maior:
#         maior = vetor[i]

# # Cálculo da média
# media = soma / n

# # Saída formatada conforme o exemplo da fonte
# print(f"Menor valor: {menor} Maior valor: {maior} Média aritmética: {int(media)}")


#questão 06

# n01 = int(input("Informe a quantidade de elementos: "))

# # 2. Inicialização da lista com tamanho fixo
# lista = [None] * n01

# # 3. Leitura dos números inteiros para preencher a lista
# for i in range(n01):
#     lista[i] = int(input(f"Digite o número para o índice {i}: "))

# # 4. Leitura da string (que deve ter o mesmo comprimento 'n')
# texto = input("Digite a string de mesmo comprimento: ")

# # 5. Lógica de substituição nos índices ímpares
# for i in range(n01):
#     # Verifica se o índice atual é ímpar
#     if i % 2 != 0:
#         # Substitui o número pelo caractere da string na mesma posição
#         lista[i] = texto[i]

# # 6. Saída formatada: exibe os elementos separados por um espaço em branco
# for i in range(n01):
#     print(lista[i], end=" ")


#questão 07
# 1. Leitura e Inicialização
# n02 = int(input("Quantos valores serão fornecidos? "))
# lista = [0] * n02

# for i in range(n02):
#     lista[i] = int(input(f"Valor {i+1}: "))

# # 2. Ordenação Manual (Bubble Sort) - Essencial para a Mediana
# for i in range(n02):
#     for j in range(0, n02 - i - 1):
#         if lista[j] > lista[j + 1]:
#             # Troca de posição (Swap)
#             aux = lista[j]
#             lista[j] = lista[j + 1]
#             lista[j + 1] = aux

# # 3. Cálculo da Mediana
# if n02 % 2 != 0:
#     # Se a quantidade é ímpar, pega o valor do meio
#     mediana = lista[n02 // 2]
# else:
#     # Se for par, faz a média dos dois valores centrais
#     mediana = (lista[n02 // 2 - 1] + lista[n02 // 2]) / 2

# # 4. Cálculo da Moda
# maior_frequencia = 0
# valor_moda = None
# amodal = True

# for i in range(n02):
#     contagem = 0
#     # Conta quantas vezes o valor atual aparece na lista
#     for j in range(n02):
#         if lista[j] == lista[i]:
#             contagem += 1
    
#     # Verifica se este valor aparece mais vezes que os anteriores
#     if contagem > maior_frequencia:
#         maior_frequencia = contagem
#         valor_moda = lista[i]

# # Se a maior frequência for 1, o conjunto não tem repetições (amodal)
# if maior_frequencia <= 1:
#     resultado_moda = "amodal"
# else:
#     resultado_moda = valor_moda
#     amodal = False

# # 5. Saída formatada conforme o exemplo da fonte
# if amodal:
#     # Nota: O exemplo 2 da fonte mostra "Média aritmética" na saída da Q7, 
#     # mas o enunciado pede a Mediana. Seguiremos o enunciado principal.
#     print(f"Moda: {resultado_moda} Mediana: {mediana}")
# else:
#     print(f"Moda: {resultado_moda} Mediana: {mediana}")


#questão 08


# # 1. Leitura da string com os números
# entrada = input("Digite os números separados por espaço: ")

# # 2. Contagem manual de elementos para pre-alocação 
# qtd_elementos = 1
# for caracter in entrada:
#     if caracter == " ":
#         qtd_elementos += 1

# # 3. Criação da lista com tamanho fixo 
# lista = [0] * qtd_elementos

# # 4. Lógica para converter a string em lista de inteiros manualmente
# numero_atual_str = ""
# indice_lista = 0

# for i in range(len(entrada)):
#     if entrada[i] != " ":
#         numero_atual_str += entrada[i]
    
#     # Se encontrar um espaço ou chegar no último caractere, salva o número
#     if entrada[i] == " " or i == len(entrada) - 1:
#         lista[indice_lista] = int(numero_atual_str)
#         indice_lista += 1
#         numero_atual_str = ""

# # 5. Soma das posições ímpares e montagem da string de saída
# soma_total = 0
# calculo_visual = ""

# for i in range(qtd_elementos):
#     # Verifica se o índice é ímpar (1, 3, 5...)
#     if i % 2 != 0:
#         soma_total += lista[i]
        
#         # Monta a parte visual (ex: "9+2+9")
#         if calculo_visual == "":
#             calculo_visual += str(lista[i])
#         else:
#             calculo_visual += "+" + str(lista[i])

# # 6. Saída formatada conforme o exemplo da fonte
# print(f"{calculo_visual} = {soma_total}")

#questão 09

# 1. Entrada de dados
# texto = input("Digite o texto: ")

# # 2. Limpeza manual de pontuação 
# texto_limpo = ""
# for char in texto:
#     if char != "." and char != ",":
#         texto_limpo += char

# # 3. Contagem de palavras para pre-alocação 
# qtd_palavras = 0
# if texto_limpo != "":
#     qtd_palavras = 1
#     for char in texto_limpo:
#         if char == " ":
#             qtd_palavras += 1

# # 4. Criação da lista e separação manual das palavras
# palavras = [None] * qtd_palavras
# palavra_temp = ""
# posicao = 0

# for i in range(len(texto_limpo)):
#     if texto_limpo[i] != " ":
#         palavra_temp += texto_limpo[i]
    
#     # Se encontrar espaço ou for o fim da string, armazena a palavra
#     if texto_limpo[i] == " " or i == len(texto_limpo) - 1:
#         if palavra_temp != "":
#             palavras[posicao] = palavra_temp
#             posicao += 1
#             palavra_temp = ""

# # 5. Contagem de frequências e formatação da saída
# saida = ""
# for i in range(qtd_palavras):
#     # Verifica se a palavra já foi processada anteriormente para não repetir na saída
#     ja_processada = False
#     for k in range(i):
#         if palavras[k] == palavras[i]:
#             ja_processada = True
#             break
    
#     if not ja_processada:
#         contagem = 0
#         # Conta quantas vezes a palavra atual aparece na lista inteira
#         for j in range(qtd_palavras):
#             if palavras[j] == palavras[i]:
#                 contagem += 1
        
#         # Monta a string de saída conforme o exemplo: "palavra=X; "
#         if saida == "":
#             saida += f"{palavras[i]}={contagem}"
#         else:
#             saida += f"; {palavras[i]}={contagem}"

# # 6. Exibição do resultado final
# print(saida)

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
