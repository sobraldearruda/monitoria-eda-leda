"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 05

def odd_even_sort(array):

  """
  O algoritmo Odd-EvenSort é uma variação do BubbleSort.
  Ele funciona através da comparação de todos os pares
  indexados com ímpar de elementos adjacentes. Se um par
  está na ordem errada (A[i] A[i+1] estão na ordem errada),
  os elementos são trocados. O próximo passo repete isso
  para os pares indexados com par de elementos adjacentes.
  E o algoritmo continua até que a entrada esteja ordenada.
  Você pode pensar no algoritmo como se a cada iteração um
  BubbleSort é aplicado considerando índices ímpares e
  outro considerando índices pares (as trocas são feitas
  entre elementos A[i] e A[i+1]). Quando não houver mais
  trocas significa que o array está ordenado.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  odd_even_sort(lista)
  print(lista)

main()
