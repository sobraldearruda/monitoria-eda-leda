"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

def order_last(array, left, right):

  """
  Posiciona o último elemento de uma sequência de forma a
  ordená-la. A sequência de entrada está sempre ordenada de
  forma crescente, exceto pelo último número.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  order_last(lista, 0, len(lista) - 1)
  print(lista)

main()
