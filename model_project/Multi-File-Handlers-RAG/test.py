# ==============================
# 100 BASIC PYTHON PROGRAMS
# ==============================

# 1. Print Hello World
print("Hello, World!")

# 2. Add two numbers
print(5 + 3)

# 3. Subtract two numbers
print(10 - 4)

# 4. Multiply two numbers
print(6 * 7)

# 5. Divide two numbers
print(20 / 5)

# 6. Check even or odd
n = 10
print("Even" if n % 2 == 0 else "Odd")

# 7. Find largest of two numbers
print(max(10, 20))

# 8. Find largest of three numbers
print(max(3, 7, 5))

# 9. Check positive or negative
n = -5
print("Positive" if n > 0 else "Negative")

# 10. Sum of first n numbers
n = 5
print(n * (n + 1) // 2)

# 11. Factorial
import math
print(math.factorial(5))

# 12. Prime number check
n = 7
print(n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)))

# 13. Print primes up to n
n = 20
print([i for i in range(2, n) if all(i % j != 0 for j in range(2, int(i**0.5)+1))])

# 14. Fibonacci series
a, b = 0, 1
for _ in range(5):
    print(a, end=" ")
    a, b = b, a + b
print()

# 15. Reverse a number
n = 1234
print(int(str(n)[::-1]))

# 16. Palindrome number
n = 121
print(str(n) == str(n)[::-1])

# 17. Armstrong number
n = 153
print(n == sum(int(d)**3 for d in str(n)))

# 18. Sum of digits
print(sum(int(d) for d in "123"))

# 19. Count digits
print(len("12345"))

# 20. Swap two numbers
a, b = 5, 10
a, b = b, a
print(a, b)

# 21. Find HCF (GCD)
import math
print(math.gcd(12, 18))

# 22. Find LCM
a, b = 12, 18
print(a * b // math.gcd(a, b))

# 23. Power of number
print(pow(2, 5))

# 24. Square root
print(math.sqrt(16))

# 25. Celsius to Fahrenheit
c = 25
print((c * 9/5) + 32)

# 26. Fahrenheit to Celsius
f = 77
print((f - 32) * 5/9)

# 27. Simple interest
p, r, t = 1000, 5, 2
print((p * r * t) / 100)

# 28. Area of circle
r = 5
print(math.pi * r * r)

# 29. Area of rectangle
l, w = 10, 5
print(l * w)

# 30. Area of triangle
b, h = 10, 5
print(0.5 * b * h)

# 31. Print numbers 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()

# 32. Sum of array
arr = [1, 2, 3, 4]
print(sum(arr))

# 33. Max in list
print(max(arr))

# 34. Min in list
print(min(arr))

# 35. Average of list
print(sum(arr) / len(arr))

# 36. Count even numbers in list
print(len([i for i in arr if i % 2 == 0]))

# 37. Count odd numbers in list
print(len([i for i in arr if i % 2 != 0]))

# 38. Reverse a list
print(arr[::-1])

# 39. Sort list
print(sorted(arr))

# 40. Remove duplicates
print(list(set([1, 2, 2, 3])))

# 41. Linear search
print(3 in arr)

# 42. Binary search
import bisect
print(bisect.bisect_left(sorted(arr), 3))

# 43. Count vowels in string
s = "hello"
print(sum(1 for c in s if c in "aeiou"))

# 44. Reverse string
print(s[::-1])

# 45. Palindrome string
print(s == s[::-1])

# 46. String length
print(len(s))

# 47. Count words
sentence = "hello world python"
print(len(sentence.split()))

# 48. Replace substring
print(sentence.replace("python", "java"))

# 49. Uppercase string
print(s.upper())

# 50. Lowercase string
print(s.lower())

# 51. ASCII value
print(ord('A'))

# 52. Character from ASCII
print(chr(65))

# 53. Check leap year
year = 2024
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# 54. Print multiplication table
n = 5
for i in range(1, 11):
    print(n * i)

# 55. Sum of even numbers up to n
n = 10
print(sum(i for i in range(n+1) if i % 2 == 0))

# 56. Sum of odd numbers up to n
print(sum(i for i in range(n+1) if i % 2 != 0))

# 57. Generate random number
import random
print(random.randint(1, 10))

# 58. Shuffle list
random.shuffle(arr)
print(arr)

# 59. Count frequency
from collections import Counter
print(Counter([1,1,2,3,3]))

# 60. Check anagram
print(sorted("listen") == sorted("silent"))

# 61. Remove spaces
print("hello world".replace(" ", ""))

# 62. Find index
print(arr.index(arr[0]))

# 63. Merge lists
print([1,2] + [3,4])

# 64. Find common elements
print(set([1,2,3]) & set([2,3,4]))

# 65. List comprehension
print([i*i for i in range(5)])

# 66. Dictionary creation
d = {"a":1, "b":2}
print(d)

# 67. Iterate dictionary
for k, v in d.items():
    print(k, v)

# 68. Dictionary length
print(len(d))

# 69. Check key exists
print("a" in d)

# 70. Merge dictionaries
print({**{"a":1}, **{"b":2}})

# 71. Tuple example
t = (1, 2, 3)
print(t)

# 72. Set example
s = {1, 2, 3}
print(s)

# 73. Type conversion
print(int("10"))

# 74. Exception handling
try:
    print(10/0)
except ZeroDivisionError:
    print("Error")

# 75. Lambda function
print((lambda x: x * x)(5))

# 76. Map function
print(list(map(lambda x: x*2, [1,2,3])))

# 77. Filter function
print(list(filter(lambda x: x%2==0, [1,2,3,4])))

# 78. Reduce function
from functools import reduce
print(reduce(lambda a,b: a+b, [1,2,3]))

# 79. File write
# open("test.txt", "w").write("Hello")

# 80. File read
# print(open("test.txt").read())

# 81. Check number is perfect
n = 6
print(n == sum(i for i in range(1, n) if n % i == 0))

# 82. Count consonants
print(sum(1 for c in "hello" if c.isalpha() and c not in "aeiou"))

# 83. Remove punctuation
import string
print("hello!".translate(str.maketrans("", "", string.punctuation)))

# 84. Generate squares
print([i**2 for i in range(1, 6)])

# 85. Count lines in file
# print(len(open("test.txt").readlines()))

# 86. Find second largest
lst = [1, 4, 2, 9]
print(sorted(lst)[-2])

# 87. Check sorted list
print(lst == sorted(lst))

# 88. Convert list to string
print("".join(map(str, [1,2,3])))

# 89. Sum of matrix
matrix = [[1,2],[3,4]]
print(sum(sum(row) for row in matrix))

# 90. Transpose matrix
print(list(zip(*matrix)))

# 91. Recursive factorial
def fact(n):
    return 1 if n == 0 else n * fact(n-1)
print(fact(5))

# 92. Recursive Fibonacci
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
print(fib(6))

# 93. Check power of two
n = 8
print(n & (n-1) == 0)

# 94. Decimal to binary
print(bin(10)[2:])

# 95. Binary to decimal
print(int("1010", 2))

# 96. Count bits
print(bin(15).count("1"))

# 97. Swap without temp
a, b = 3, 4
a ^= b; b ^= a; a ^= b
print(a, b)

# 98. Time complexity example
print("O(n)")

# 99. Memory size of object
import sys
print(sys.getsizeof(100))

# 100. End of programs
print("100 Python programs completed!")
