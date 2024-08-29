"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 08

def quick_sort_hoare(array, left, right):

  """
  Aplique a estretégia de particionamento Hoare ao Quick Sort.
  Lembre-se que a ideia é usar dois índices para percorrer
  o array:

  1. O primeiro índice parte da posição à frente do
     pivot e percorre o array do início ao fim.
  2. O segundo índice parte da última posição e percorre
     o array do fim ao início.
  3. Sempre que encontra um elemento maior que o pivot,
     o primeiro índice pára.
  4. Sempre que encontra um elemento menor que o pivot,
     o segundo índice pára.
  5. Depois dessa primeira iteração, se primeiro-índice <
     segundo-índice, troca-se primeiro-índice por segundo-índice
     e repete-se esse processo.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada = input().split()
  lista = [int(e) for e in entrada]
  quick_sort_hoare(lista, 0, len(lista) - 1)
  print(lista)

main()
