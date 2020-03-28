# input
n = int(input())

# solution
divisor = 2
while divisor ** 2 <= n: # Use observation 1
    power_cnt = 0
    while n % divisor == 0: 
        '''
        Observation 2:
        Note that if n % divisor == 0 
        then the divisor must be a prime 
        '''
        n //= divisor
        power_cnt += 1
    if power_cnt != 0:
        print(divisor, power_cnt)
    # try the next integer
    divisor += 1

if n != 1: # deal with the case we have not found all prime divisors yet
    print(n, 1)
