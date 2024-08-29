"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 13

def order_statistics(array, k):

  """
  Retorna a k-ésima Estatística de Ordem de um array ordenado.
  Caso não exista a k-ésima Estatística de Ordem, então
  retorna -1. O valor de k deve ser entre 1 e N.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  num = int(input())
  print(order_statistics(lista, num))

main()
