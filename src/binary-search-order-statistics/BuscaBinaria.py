"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

def busca_binaria(array, num, left, right):

  """
  Verifica se um número N está em uma sequência ordenada
  de inteiros, usando recursão. Retorna a posição de N.
  """

  result = -1
  mid = (left + right) // 2
  if (left <= right):
    if (num == array[mid]):
      result = mid
    elif (num < array[mid]):
      result = busca_binaria(array, num, left, mid - 1)
    else:
      result = busca_binaria(array, num, mid + 1, right)
  return result

def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  num = int(input())
  print(busca_binaria(lista, num, 0, len(lista) - 1))

main()
