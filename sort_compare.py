"""
Tests the efficiency of 5 sperate types of sorting algorithms
 author: Ryan Callinan
 file: sort_compare.py
"""

import time
import random

def insertionsort(randlist):
    start = time.time()
    for i in range(1, len(randlist)):
        j = i
        while j > 0 and randlist[j] < randlist[j-1]:
            randlist[j], randlist[j - 1] = randlist[j - 1], randlist[j]
            j -= 1
    return end_time(start)



def selectionsort(randlist):
    start = time.time()
    for i in range(len(randlist)):
            least = i
            for k in range(i + 1, len(randlist)):
                if randlist[k] < randlist[least]:
                    least = k
            swap(randlist, least, i)
    return end_time(start)


def h_sort(randlist):
    """
    Sorts by checking the last nember on the left side of the array until correct.
    :param randlist:
    :return:
    """
    start = time.time()
    length = len(randlist) - 1
    leastParent = length / 2
    for i in range(int(leastParent), -1, -1):
        siftdown(randlist, i, length)
    for i in range(length, 0, -1):
        if randlist[0] > randlist[i]:
            swap(randlist, 0, i)
            siftdown(randlist, 0, i - 1)
    return end_time(start)


def siftdown(randlist, i, last):
    """
    Moves "incorrect" values down a slot and awaits the correct value.
    :param randlist:
    :param i:
    :param last:
    :return:
    """
    largest = 2 * i + 1
    while largest <= last:
        if (largest < last) and (randlist[largest] < randlist[largest + 1]):
            largest += 1
        if randlist[largest] > randlist[i]:
            swap(randlist, largest, i)
            i = largest;
            largest = 2 * i + 1
        else:
            return


def mergesort(randlist):
    """
    Sorts by spliting each side into singular integers then checking merging them back into one sorted list.
    :param randlist: Randomly generated list
    :return:
    """
    start = time.time()
    if len(randlist) > 1:
        left_idx, right_idx, total = 0, 0, 0
        mid = len(randlist) // 2
        leftside = randlist[:mid]
        rightside = randlist[mid:]
        mergesort(leftside)  # split the left side again
        mergesort(rightside)  # Split the right side again
        while left_idx < len(leftside) and right_idx < len(rightside):
            if leftside[left_idx] < rightside[right_idx]:
                randlist[total] = leftside[left_idx]
                left_idx += 1
            else:
                randlist[total] = rightside[right_idx]
                right_idx += 1
            total += 1
        while left_idx < len(leftside):
            randlist[total] = leftside[left_idx]
            left_idx += 1
            total += 1
        while right_idx < len(rightside):
            randlist[total]=rightside[right_idx]
            right_idx += 1
            total += 1
    return end_time(start)


def quicksort(randlist, first, last):
    """
    Uses stacks to sort
    :param randlist: Randomly generated list
    :param first:
    :param last:
    :return:
    """
    start = time.time()
    tmp_lst = []
    tmp_lst.append((first, last))
    while tmp_lst:
        pos = tmp_lst.pop()
        last, first = pos[1], pos[0]
        piv = find_pivot(randlist, first, last)
        if piv - 1 > first:
            tmp_lst.append((first, piv - 1))
        if piv + 1 < last:
            tmp_lst.append((piv + 1, last))
    return end_time(start)


def find_pivot(randlist, first, last):
    """
    Finds the pivot point for quicksort
    :param randlist:
    :param first:
    :param last:
    :return:
    """
    pivot = first
    swap(randlist, pivot, last)
    for i in range(first, last):
        if randlist[i] <= randlist[last]:
            swap(randlist, i, first)
            first += 1
    swap(randlist, first, last)
    return first


def swap(randlist, least, i):
    tmp = randlist[least]
    randlist[least] = randlist[i]
    randlist[i] = tmp


def end_time(start):
    """
    Gets the total time
    :param start:
    :return:
    """
    end = time.time()
    timer = end-start
    return timer


def main():
    """
    Collects the time data from each sorting algorithm
    :return:
    """
    randlist = []
    old_list = []
    min = int(input("What is the min possible value of an item in the list:"))
    max = int(input("What is the max possible value of an item in the list:"))
    size = int(input("what is the size of the list:"))
    display = input("Do you want to display the list? (Y/N)")
    for _ in range(size):
        randlist.append(random.randint(min,max))
    if display == "Y":
        print(randlist)
    old_list = randlist[:]
    print("Insertion Sort Time", insertionsort(randlist),"seconds")
    randlist = old_list[:]
    print("Selection Sort Time", selectionsort(randlist), "seconds")
    randlist = old_list[:]
    print("Heap Sort Time", h_sort(randlist), "seconds")
    randlist = old_list[:]
    print("Merge Sort Time", mergesort(randlist), "seconds")
    randlist = old_list[:]
    print("Quick Sort Time", quicksort(randlist,0,len(randlist) - 1), "seconds")
    print()

main()