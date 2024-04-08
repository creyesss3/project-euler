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

print("total:", getFibonacciSequence(10000))