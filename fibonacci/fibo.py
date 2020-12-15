fibarray = [0,1]

def fibonacci(n):
    for i in range(0,n):
        n = fibarray[len(fibarray)-1] + fibarray[len(fibarray)-2]
        fibarray.append(n)

fibonacci(100)         
print(fibarray)
