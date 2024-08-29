"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 04

def insertion_sort_variation(array):

  """
  The Insertion Sort algorithm iterates over the array and
  assumes that the visited positions are already sorted
  in ascending order, meaning it only needs to find the
  right position for the current element and insert it there.
  This variation iterates over the array on the contrary,
  starting by its last position.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  insertion_sort_variation(lista)
  print(lista)

main()
