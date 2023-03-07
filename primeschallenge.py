# function to find prime numbers
def is_prime(n):
    for e in range(2,n):
        if n%e==0:
            return False
    return True

#the every-pattern is used to populate the primes list
def primes_list(n):
    primes = []
    for e in range(1,n-1):
        if is_prime(e):
           primes.append(e)
    return primes

# save the primes to text file
def save_primes(filename,data):
    handler = open(filename,'w')
    for line in data:
        handler.write(str(line))
        handler.write("\n")

def run():
    n =251
    primes = primes_list(n)
    print(primes)
    save_primes("results.txt",primes)

run()
    
