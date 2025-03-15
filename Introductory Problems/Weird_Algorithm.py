def number(n):
    print(n, sep=' -> ', end=' ')
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n, end=' ')
    # return n

n = int(input())
number(n)