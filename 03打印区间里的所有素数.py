def is_prime(num):
    if num in (1,2):#1 既不是素数也不是合数
        return True
    # for idx in range(2,num):
    #     if num % idx == 0:
    #         return False
    #     else:
    #         return True
    #
    for idx in range(2,num):#这里不能加一 否则都能整除了
        if num % idx == 0:
            return False           
    return True #内层循环结束 才会到return 这时候说明除了1，本身，没有他的余数

def print_primes(begin,end):
    for number in range(begin,end+1):
        if is_prime(number):
            print(f"{number} is a prime")

begin=11
end=25
print_primes(begin,end)