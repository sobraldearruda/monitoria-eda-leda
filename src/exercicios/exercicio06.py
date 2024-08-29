"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

# EXERCÍCIO 06

def merge(array1, array2):

  """
  Em uma clínica, pacientes de todas as especialidades
  recebem fichas por ordem de chegada e são instruídos a
  formar filas para serem atendidos no meio da tarde. Porém,
  em certo momento, a recepcionista os informa que um dos
  médicos faltou e que as duas filas terão que se unir,
  respeitando a ordem de chegada. Para evitar confusão, ela
  requisitou ao sistema de cadastros para unir as duas
  sequências de números de fichas, retornando uma única
  sequência ordenada. Logo, escreva um algoritmo que resolva
  esse problema.
  """

  # Escreva seu código abaixo:


def main():

  """ Simula a entrada e a saída de dados. """

  entrada1 = input().split()
  lista1 = [int(e) for e in entrada1]
  entrada2 = input().split()
  lista2 = [int(e) for e in entrada2]
  merge(lista1, lista2)

main()
