"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 07

def quick_sort_median_of_three(array, left, right):

  """
  A função quick_sort_median_of_three representa uma
  variação do Quick Sort, que funciona de forma ligeiramente
  diferente. Relembre que quando o pivot escolhido divide
  o array aproximadamente na metade, o Quick Sort tem um
  desempenho perto do ótimo. Para aproximar a entrada do
  caso ótimo, diversas abordagens podem ser utilizadas.
  Uma delas é usar a mediana de 3 para achar o pivot. Essa
  técnica consiste no seguinte:

  1. Comparar o elemento mais a esquerda, o central e o
     mais a direita do intervalo.
  2. Ordenar os elementos, tal que:
     A[left] < A[center] < A[right].
  3. Adotar o A[center] como pivot.
  4. Colocar o pivot na penúltima posição A[right-1].
  5. Aplicar o particionamento considerando o vetor menor,
     de A[left+1] até A[right-1].
  6. Aplicar o algoritmo na partição a esquerda e na partição
     a direita do pivot.
  """

  # Escreva seu código abaixo:


def main():

    """ Simula a entrada e a saída de dados. """

    entrada = input().split()
    lista = [int(e) for e in entrada]
    quick_sort_median_of_three(lista, 0, len(lista) - 1)
    print(lista)

main()
