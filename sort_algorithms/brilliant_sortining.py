import os
input("Input a list:")
A=list()
print(A)
for current in range(1, len(A)-1):
    minIndex=current
    for i in range(current+1, len(A)):
        if A[i]<A[minIndex]:
            minIndex=i
    A[current], A[minIndex]=A[minIndex],A[current]
print(A)