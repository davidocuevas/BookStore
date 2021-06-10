"""Implementations of some sorting"""
import random

def merge(a0, a1, a):
    # todo
    i0 = i1 = 0
    for k in range (0, len(a)):
        if i0 == len(a0):
            a[k] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[k] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[k] = a0[i0]
            i0 += 1
        else:
            a[k] = a1[i1]
            i1 += 1

def merge_sort(a):
    # todo
    if len(a) <= 1:
        return a
    else:
        m = len(a)//2
        a0 = merge_sort(a[:m])
        a1 = merge_sort(a[m:])
        merge(a0, a1, a)
        return a

def _quick_sort(a, i, n):
    # todo
    if n <= 1:
        return a
    x = a[i + random.randint(1, n-1)]
    p = i - 1
    j = i
    q = i + n
    while j < q:
        if a[j] < x:
            p += 1
            a[j], a[p] = a[p], a[j]
            j += 1
        elif a[j] > x:
            q -= 1
            a[j], a[q], = a[q], a[j]
        else:
            j += 1
    _quick_sort(a, i, p-i+1)
    _quick_sort(a, q, n-(q-i))

def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a
    
def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while r > 1:
        m = (r + 1)//2
        if x <= a[m]:
            r = m
        else:
            l = m + 1
    if a[l] == x:
        return l
    else:
        return -1

