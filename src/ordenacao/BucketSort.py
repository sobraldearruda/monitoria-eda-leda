"""
Estruturas de Dados e Algoritmos
Rafael de Arruda Sobral (UFCG/SEE-PB)
Prof. Dr. Adalberto Cajueiro de Farias (UFCG)
"""

def bucket_sort(array):

  """
  Bucket Sort divides the unsorted array elements into
  several groups called buckets. Each bucket is then sorted
  by using any of the suitable sorting algorithms or
  recursively applying the same bucket algorithm. Finally,
  the sorted buckets are combined to form a final sorted array.
  """

  # If so, return the empty array
  if len(array) == 0:
    return array

  # Determine the number of buckets
  num_buckets = len(array)
  max_value = max(array)

  # Create empty buckets
  bucket = [[] for _ in range(num_buckets)]

  # Insert elements into their respective buckets
  for j in array:
    index_b = int(num_buckets * j / (max_value + 1))
    bucket[index_b].append(j)

  # Sort the elements of each bucket using Insertion Sort
  for i in range(num_buckets):
    bucket[i] = insertion_sort(bucket[i])

  # Get the sorted elements
  sorted_array = []
  for i in range(num_buckets):
    sorted_array.extend(bucket[i])

  return sorted_array

def insertion_sort(array):

  """ Insertion Sort algorithm. """

  for i in range(1, len(array)):
    key = array[i]
    aux = i - 1
    while (aux >= 0 and array[aux] > key):
      array[aux + 1] = array[aux]
      aux -= 1
    array[aux + 1] = key
  return array

def asserts():

  """ Test the Bucket Sort """

  # Test 1: Basic test case
  assert bucket_sort([0.2, 0.7, 0.1]) == [0.1, 0.2, 0.7]
  print("Test 1 Passed: [0.1, 0.2, 0.7]")

  # Test 2: Empty list
  if bucket_sort([]) == []:
    print("Test 2 Passed: []")
    assert True
  else:
    print("Test 2 Failed: Expected []")
    assert False

  # Test 3: Single element
  if bucket_sort([0.5]) == [0.5]:
    print("Test 3 Passed: [0.5]")
    assert True
  else:
    print("Test 3 Failed: Expected [0.5]")
    assert False

  # Test 4: Already sorted
  if bucket_sort([0.1, 0.2, 0.3, 0.4, 0.5]) == [0.1, 0.2, 0.3, 0.4, 0.5]:
    print("Test 4 Passed: [0.1, 0.2, 0.3, 0.4, 0.5]")
    assert True
  else:
    print("Test 4 Failed: Expected [0.1, 0.2, 0.3, 0.4, 0.5]")
    assert False

  # Test 5: Reverse sorted
  if bucket_sort([0.5, 0.4, 0.3, 0.2, 0.1]) == [0.1, 0.2, 0.3, 0.4, 0.5]:
    print("Test 5 Passed: [0.1, 0.2, 0.3, 0.4, 0.5]")
    assert True
  else:
    print("Test 5 Failed: Expected [0.1, 0.2, 0.3, 0.4, 0.5]")
    assert False

  # Test 6: Random order
  if bucket_sort([0.9, 0.2, 0.4, 0.1, 0.5, 0.8, 0.6, 0.3, 0.7]) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    print("Test 6 Passed: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]")
    assert True
  else:
    print("Test 6 Failed: Expected [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]")
    assert False

  # Test 7: Duplicates
  if bucket_sort([0.5, 0.3, 0.5, 0.3, 0.5]) == [0.3, 0.3, 0.5, 0.5, 0.5]:
    print("Test 7 Passed: [0.3, 0.3, 0.5, 0.5, 0.5]")
    assert True
  else:
    print("Test 7 Failed: Expected [0.3, 0.3, 0.5, 0.5, 0.5]")
    assert False

  # Test 8: Mixed small and large numbers
  if bucket_sort([0.12, 0.34, 0.23, 0.45, 0.56, 0.78, 0.67, 0.89]) == [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.89]:
    print("Test 8 Passed: [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.89]")
    assert True
  else:
    print("Test 8 Failed: Expected [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.89]")
    assert False

# Run the tests
asserts()
