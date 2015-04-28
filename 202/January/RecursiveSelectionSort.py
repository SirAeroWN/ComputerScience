import sys
import random
import time
sys.setrecursionlimit(15000)

def sort(lst):
    sortHelper(lst, 0, len(lst) - 1) # Sort the entire lst

def sortHelper(lst, low, high):
    if low < high:
        # Find the smallest number and its index in lst[low .. high]
        indexOfMin = low;
        min = lst[low];
        for i in range(low + 1, high + 1):
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i

        # Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low]
        lst[low] = min

        # Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high)

def main():
    lst = []
    length = 10000
    for i in range(0, length):
        lst.append(random.randint(1, length))
    sort(lst)
    print(lst)

start = time.time()
main()
print(format((time.time() - start), '.3f'))
