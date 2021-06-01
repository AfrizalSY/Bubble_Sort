# Utility function to swap values at two indices in the list
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Function to perform bubble sort on list
def bubbleSortIterative(A):
 
    for k in range(len(A) - 1):
 
        # last k items are already sorted, so inner loop can
        # avoid looking at the last k items
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
def bubbleSortRecursive(A, n):
 
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)
 
    if n - 1 > 1:
        bubbleSortRecursive(A, n - 1)
    # the algorithm can be stopped if the inner loop
    # didn’t do any swap