"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

def merge_sort(array, left, right):

  """
  The Merge Sort algorithm consists of recursively dividing
  the unsorted list in the middle, sorting each sublist,
  and then merging them into one single sorted list.
  """

  if (left < right):
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)

def merge(array, left, mid, right):

  """ Merge two sorted lists. """

  aux = [e for e in array]
  i = left
  j = mid + 1
  k = left
  while (i <= mid and j <= right):
    if (aux[i] <= aux[j]):
      array[k] = aux[i]
      i += 1
    else:
      array[k] = aux[j]
      j += 1
    k += 1
  while (i <= mid):
    array[k] = aux[i]
    i += 1
    k += 1

def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  merge_sort(lista, 0, len(lista) - 1)
  print(lista)

main()
