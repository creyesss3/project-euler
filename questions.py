"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""
def sumOfMultiples(n):
    ''' Finds the sum of all the multiples of 3 or 5 below n. '''
    nums = []
    for i in range(n):
        if i % 3 == 0:
            nums.append(i)
        elif i % 5 == 0:
            nums.append(i)
    return sum(nums)


def SumDivisibleBy(target, n):
   ''' 
    Solution given by Project Euler.
    Finds the sum of all the multiples of 3 or 5 below n.
    The target variable should be true target - 1.
   '''
   p = target // n
   return n * (p * (p + 1)) // 2


def getFibonacciSequence(n):
    a = 0
    b = 1
    seq = [a, b]
    evens = []
    for _ in range(n):
        a, b = b, a + b
        seq.append(b)
        print(b)
        if b > 4000000:
            break
    for i in seq:
        if i % 2 == 0:
            evens.append(i)
    return sum(evens)

def largestPrimeFactor(n):
    """Find the largest prime factor of an integer n."""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n = n / d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return int(max(factors))

def largestPalindromeProduct(n):
    max_num = int('9' * n)
    min_num = int('1' + '0' * (n-1))
    largest_palindrome = 0
    
    for i in range(max_num, min_num-1, -1):
        for j in range(i, min_num-1, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if str(product) == str(product)[::-1]:
                largest_palindrome = product
    
    return largest_palindrome        

def gcd(a, b):
    # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Least common multiple
    return (a * b) // gcd(a, b)

def smallestMultiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print(smallestMultiple(20))