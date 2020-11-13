numbers = [3,6,8,7,9,10,11,13,14,16,29]

def isprime(numbers):
    prime = []
    for n in numbers:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            prime.append(n)
        return prime
