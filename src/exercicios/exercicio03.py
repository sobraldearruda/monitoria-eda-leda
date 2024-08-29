"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 03

def selection_sort_variation(array):

  """
  The Selection Sort algorithm chooses the BIGGEST element
  from the array and puts it in the LAST position. Then,
  it chooses the second BIGGEST element and stores it in
  the previous LAST position, and so on until the array is sorted.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  selection_sort_variation(lista)
  print(lista)

main()
