# primemodule.py

'''primemodule.py is a module that determines whether or not a number is prime
 or not. If it is, it is added to a list'''


def isPrime(n):
    '''isPrime checks if a number is prime or not. If it is it returns boolean
    True, otherwise False'''

    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def getNPrime(num):
    '''Iterates through range num to send to isPrime and if it is True it will
     be added to the list myList '''

    myList = []
    for x in range(num):
        if isPrime(x+1):
            myList.append(x+1)
    return myList
