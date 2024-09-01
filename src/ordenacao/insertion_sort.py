"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

def insertion_sort(array):

  """
  The Insertion Sort algorithm iterates over the array and
  assumes that the visited positions are already sorted
  in ascending order, meaning it only needs to find the
  right position for the current element and insert it there.
  """

  for i in range(1, len(array)):
    key = array[i]
    aux = i - 1
    while (aux >= 0 and array[aux] > key):
      array[aux + 1] = array[aux]
      aux -= 1
    array[aux + 1] = key

def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  insertion_sort(lista)
  print(lista)

main()