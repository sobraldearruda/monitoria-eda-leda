"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 12

def ceil(array, num, left, right):

  """
  Ceil é o elemento do array igual a x, ou maior e mais
  próximo possível de x (caso x não pertença ao array).
  O algoritmo deve ter tempo O(n log n) e deve ser in-place,
  usando recursão. Você pode assumir que o array não tem
  elementos repetidos.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  num = int(input())
  print(ceil(lista, num, 0, len(lista) - 1))

main()
