from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+ 1):
        if x % i == 0:
            return False
    return True

def primes():
    num = 1 + int(raw_input("What is the range for primes? "))
    return [x for x in range(num) if is_prime(x)]

def main():
    print(primes())

if __name__ == '__main__':
    main()