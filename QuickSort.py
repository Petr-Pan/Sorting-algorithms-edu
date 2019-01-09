import random

def QuickSort(A,l,r):
    x = A[(l+r)//2]
    i = l
    j = r
    while i<=j:
        while A[i] < x:
            i += 1
        while A[j] > x:
            j -= 1
        if i > j:
            break
        A = exch(A, i, j)
        i += 1
        j -= 1
        if not i<=j:
            break
    if l < j:
        A = QuickSort(A, l, j)
    if r > i:
        A = QuickSort(A, i, r)
    return A

#___________________________________________________________________________________
#Pseudocode simulation
def exch(A, index1, index2):
    A[index1], A[index2] = A[index2], A[index1]
    return A

#Array generation
def rand_intarray(size):
    output = []
    for item in range(size):
        output.append(random.randint(0,9))
    return output

#Generate array with unique numbers only
def rand_intarray_U(size):
    output = [number for number in range(size)]
    random.shuffle(output)
    return output

#Console output
if __name__ == '__main__':
    A = rand_intarray_U(random.randint(5,10))
    print(A)
    A = QuickSort(A, 0, len(A)-1)
    print(A)