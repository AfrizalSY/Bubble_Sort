import BubbleSort
import List
import timeit
import execution
import sys


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    data = "list6.dat"


    arr = List.LoadList(data)
    print("Banyak data : {}".format(len(arr)))
    # print("Data:", arr)

    # iterative section
    start = timeit.default_timer()
    BubbleSort.bubbleSortIterative(arr)
    execution.calulate("Iterative bubble sort", start)
    
    # recursive section
    arr = List.LoadList(data)
    start = timeit.default_timer()
    BubbleSort.bubbleSortRecursive(arr,len(arr))
    execution.calulate("Recursive bubble sort", start)