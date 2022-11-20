def get_next_prime(num):
    k = 0
    for i in range(1, num + 1):
        if num % i == 0:
            k += 1
    if k == 2:
        return num
    else:
        return get_next_prime(num+1)

n = int(input())+1
print(get_next_prime(n))