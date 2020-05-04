import random
import sys
sys.setrecursionlimit(1000000)


def insertion_sort(sort_list, min, max):
    for i in range(min, max + 1):
        key = sort_list[i]
        j = i - 1
        while j >= min and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    return sort_list


def calcMedian(Array, min, max):
    mid = int((max + min) / 2)
    if Array[min] > Array[mid]:
        Array[min], Array[mid] = Array[mid], Array[min]
    if Array[min] > Array[max]:
        Array[max], Array[min] = Array[min], Array[max]
    if Array[mid] > Array[max]:
        Array[max], Array[mid] = Array[mid], Array[max]
    return mid


def quicksort_median(Array, min, max):
    if max - min >= 10:
        pivot_index = calcMedian(Array, min, max)
        Array[pivot_index], Array[max - 1] = Array[max - 1], Array[pivot_index]
        pivot_index = max - 1
        l_index = min
        r_index = max - 2
        bool = True
        while bool:
            while Array[l_index] <= Array[pivot_index] and l_index <= r_index:
                l_index += 1
            while Array[r_index] > Array[pivot_index] and r_index >= l_index:
                r_index -= 1
            if l_index < r_index:
                Array[l_index], Array[r_index] = Array[r_index], Array[l_index]
            else:
                bool = False
        Array[l_index], Array[pivot_index] = Array[pivot_index], Array[l_index]
        pivot_index = l_index
        quicksort_median(Array, min, l_index - 1)
        quicksort_median(Array, l_index + 1, max)
    else:
        Array = insertion_sort(Array, min, max)


def main():
    Array = []
    for x in range(1, 15000):
        Array.append(random.randint(1, 15000))
    #print(Array)
    quicksort_median(Array, 0, len(Array) - 1)
    print(Array)


main()
