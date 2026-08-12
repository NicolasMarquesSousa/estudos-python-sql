print("Ola meu nome e Nicolas")


frutas = ["maçã", "banana", "laranja"]

print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"

print(frutas[-1])  # Imprime "laranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "maçã"

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.insert(2, "morango")
print(frutas) # Imprime ["maçã", "uva", "morango", "banana", "laranja", "pera"]

frutas.append("abacaxi")
print(frutas) # Imprime ["maçã", "uva", "morango", "banana", "laranja", "pera", "abacaxi"]

frutas.remove("morango")
print(frutas) # Imprime ["maçã", "uva", "banana", "laranja", "pera", "abacaxi"]

#Listas de compreensao 

numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]

# Tuplas

ponto = (3, 4)  
print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4

minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2)) # Saida: 1
print (minha_tupla.index(2, 2)) #Saida: 3
print (minha_tupla.index(2, 2, 4)) #Saida: 3


#Dicionarios

pessoa = {"nome": "Nicolas", "idade": 20, "cidade": "Barueri"}
print(pessoa["nome"])  # Imprime "Nicolas"
print(pessoa["idade"])  # Imprime 20
print(pessoa["cidade"])  # Imprime "Barueri"


pessoa = {"nome": "Nicolas", "idade": 20, "cidade": "Barueri"}
print(pessoa.keys()) # Imprime dict_keys(['nome', 'idade', 'cidade'])
print(pessoa.values()) # Imprime dict_values(['Nicolas', 20, 'Barueri'])
print(pessoa.items()) # Imprime dict_items([('nome', 'Nicolas'), ('idade', 20), ('cidade', 'Barueri')])

pessoa.update({"profissao": "Estagiario"})
print(pessoa) # Imprime {"nome": "Nicolas", "idade": 20, "cidade": "Barueri", "profissao": "Estagiario"}

# Conjuntos (sets)

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1 | conjunto2
print(uniao) # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao) # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca) # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica) # Imprime {1, 2, 4, 5}

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas) # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("laranja")
print(frutas) # Imprime {"maçã", "banana", "pera"}

frutas.discard("uva")  # Não gera erro se o elemento não existir
print(frutas) # Imprime {"maçã", "banana", "pera"}

frutas.clear()
print(frutas) # Imprime set()

frutas.add("pera")
print(frutas) # Imprime {"pera"}