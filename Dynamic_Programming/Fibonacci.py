def fib(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    print(a)
    return a[n]


def main():
    n = 13
    value = fib(n)
    print("the fib of {0} is  = {1}".format(n,value))




main()