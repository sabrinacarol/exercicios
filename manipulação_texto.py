# Fatiamento(no fatiamento o ultimo valor é ingnorado pelo python)

frase = 'Sabrina Caroline Campos'
print(frase[:5], frase[15:], frase[9::3])
# antes dos : ele vai começar e vai ate a letra 5
# 15: indiquei o inicio mas nao coloquei o fim
# 9::3 vai começar no 9 e vai ate o final só que pulando de 3 em 3 casas

# Análise(analisar uma string)
# len comprimento da frase (conta quantas caracteres tem)
print(len(frase))

# count- contador
print(frase.count('o', 0, 13))
# fazendo uma contagem e fatiamento ao mesmo tempo

# find - encontrar - quantas vezes ele encontrou algo
print(frase.find('a'))

print(frase.find('Kiara'))
# Se ele retornar -1 significa que a string nao existe nao encontrado

# Usando o operador in que tbm dá para fazer análise
print('Sabrina' in frase)
# existe Curso em frase

# Transformação

# replace - trocar reposicionar
print(frase.replace('Sabrina', 'Kiara'))

# upper - para cima - maiuscula
print(frase.upper())
# coloca todos em maiusculo

# lower - minusculo
print(frase.lower())

# capitalize - joga todos os caracteres para minusculo e a primeira letra da frase fica maiuscula
print(frase.capitalize())

# title - transforma palavra por palavra a letra inicial em maiuscula

print(frase.title())

# strip - remove todos os espaços inúteis
print(frase.strip())

# rstrip - r= right direita - remove somente os espaços do direita
print(frase.rstrip())

# lstrip - l= left esquerda - remove somente os espaços do esquerda

# DIVISÃO
# split - pega os espaços em branco, tornando-as um lista separadas de palavras
# split - divide uma string em uma lista
print(frase.split())

# JUNÇÃO
# join - juntar uma coisa na outra
print('-'.join(frase))

print(frase.lower().find('a'))
