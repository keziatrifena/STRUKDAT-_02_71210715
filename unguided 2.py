import timeit

def fibo_rek(n):
    for i in range(1,n):
        if n==1 or n==2:
            return 1
        else:
            return fibo_rek(n-1) + fibo_rek(n-2)


for i in range(1,12):
    start1 = timeit.default_timer()
    end1 = timeit.default_timer()
    print("Fibonacci rekursif: ", i, "dengan waktu: ", end1-start1, "second")


#iteraktif
def fibonacci_iteraktif(n):
    a = 0
    b = 1
    for i in range (0, n):
        x = a 
        a = b 
        b = x + b
    return a

for i in range (1, 11):
    start = timeit.default_timer()
    end = timeit.default_timer()
    print("Bilangan fibonacci ", i, "adalah", fibonacci_iteraktif(i), "selama", start-end, "detik.")