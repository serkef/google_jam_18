t = int(input(''))

for case in range(t):

    lim = input('').split()
    a = int(lim[0])
    b = int(lim[1])
    n = int(input(''))

    for i in range(n):
        q = int((a + 1 + b + 1)/2)
        print(q)
        s = input()
        if s == 'CORRECT':
            break
        elif s == 'TOO_BIG':
            b = q - 1
        elif s == 'TOO_SMALL':
            a = q