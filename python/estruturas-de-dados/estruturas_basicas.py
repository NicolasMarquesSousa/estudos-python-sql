"""Exemplos básicos de Python desenvolvidos durante os estudos."""

from datetime import datetime
from math import sqrt
from pathlib import Path
from random import randint


def demonstrar_listas() -> None:
    frutas = ["maçã", "banana", "laranja"]
    print(frutas[0], frutas[-1])

    frutas.append("pera")
    frutas.insert(1, "uva")
    frutas.insert(2, "morango")
    frutas.append("abacaxi")
    frutas.remove("morango")
    print(frutas)

    numeros = [1, 2, 3, 4, 5]
    quadrados_pares = [numero**2 for numero in numeros if numero % 2 == 0]
    print(quadrados_pares)


def demonstrar_tuplas() -> None:
    ponto = (3, 4)
    print(ponto[0], ponto[1])

    valores = (1, 2, 3, 2, 4, 2)
    print(valores.index(2))
    print(valores.index(2, 2))
    print(valores.index(2, 2, 4))


def demonstrar_dicionarios() -> None:
    pessoa = {"nome": "Nicolas", "idade": 20, "cidade": "Barueri"}
    print(pessoa["nome"], pessoa["idade"], pessoa["cidade"])
    print(pessoa.keys())
    print(pessoa.values())
    print(pessoa.items())

    pessoa.update({"profissão": "Estagiário"})
    print(pessoa)


def demonstrar_conjuntos() -> None:
    conjunto1 = {1, 2, 3}
    conjunto2 = {3, 4, 5}
    print(conjunto1 | conjunto2)
    print(conjunto1 & conjunto2)
    print(conjunto1 - conjunto2)
    print(conjunto1 ^ conjunto2)

    frutas = {"maçã", "banana", "laranja"}
    frutas.add("pera")
    frutas.remove("laranja")
    frutas.discard("uva")
    print(frutas)
    frutas.clear()
    print(frutas)


def demonstrar_excecoes() -> None:
    try:
        resultado = 10 / 0
        print(resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")

    try:
        int("texto")
    except ValueError:
        print("Erro: valor inválido")
    finally:
        print("Exemplo de exceção finalizado")


def demonstrar_arquivos() -> None:
    caminho = Path(__file__).with_name("dados_exemplo.txt")

    caminho.write_text("Olá, mundo!", encoding="utf-8")
    conteudo = caminho.read_text(encoding="utf-8")
    print(conteudo)
    caminho.unlink(missing_ok=True)


def demonstrar_modulos() -> None:
    print(sqrt(25))
    print(randint(1, 10))
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


def apresentar_usuario() -> None:
    nome = input("Digite seu nome: ").strip()
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("A idade deve ser um número inteiro.")
        return

    classificacao = "maior" if idade >= 18 else "menor"
    print(f"Olá, {nome}! Você tem {idade} anos e é {classificacao} de idade.")


def main() -> None:
    demonstrar_listas()
    demonstrar_tuplas()
    demonstrar_dicionarios()
    demonstrar_conjuntos()
    demonstrar_excecoes()
    demonstrar_arquivos()
    demonstrar_modulos()


if __name__ == "__main__":
    main()
