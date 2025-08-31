import sys, time
a=list(sys.argv[1])

def sorting(a):
    print("got here!")
    for i in range(0, len(a)-1):
        minIndex=i
        for j in range(i+1, len(a)):
            if a[j]<a[minIndex]:
                minIndex=j
        if minIndex!=i:
            a[i],a[minIndex]=a[minIndex],a[i]
    return(a)
print(sorting(a))