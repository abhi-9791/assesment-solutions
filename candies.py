def count_sets(N):
    count = 0
    i = 1 
    while N > 0:
        if N % i == 0:
            count += 1
        N -= i
        i += 2
    return count
N = int(input())
result = count_sets(N)
print(result)
