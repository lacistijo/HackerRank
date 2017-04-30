def array_left_rotation(a, n, k):
    temp = a[:]
    for x in range(n):
        shift = int(((k+n+x) % n)) 
        a[x] = temp[shift]
    return a
        

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')