"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 02

def troca_vizinhos(array):

  """
  Troca os elementos vizinhos.
  Se o tamanho da sequência for ímpar, troca os vizinhos
  e mantém o último elemento em sua posição.
  O algoritmo deve ser in-place.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  troca_vizinhos(lista)
  print(lista)

main()
