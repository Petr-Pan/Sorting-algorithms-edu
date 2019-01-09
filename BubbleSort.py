import random
def BubbleSort(A, n):
    for i in range(n-2,0,-1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A = exch(A, j, j+1)
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
    #len(A)+1 because python's "for i in range" functions differently than pseudocode - it does not execute top bound
    A = BubbleSort(A, len(A)+1)
    print(A)
