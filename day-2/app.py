# Q1. Count Trailing Zeros in Factorial

# Input: n = 10
# Output: 2

# n = 10
# digit = 1
# fact = 0

# while n > 0:
#     n //= 5
#     fact += n

# print(fact)

# Q2. GCD (Greatest Common Divisor)
# Input: a = 12, b = 18 → 6


# Q3. LCM using GCD
# 👉 Relationship:

# LCM * GCD = a * b
# a, b = map(int, input().split())

# x, y = a, b

# while b != 0:
#     a, b = b, a % b

# gcd = a
# lcm = (x * y) // gcd

# print(lcm)

# Q4. Perfect Number

# Input: 28 → True
# (1 + 2 + 4 + 7 + 14 = 28)

# num = 15

# digit = 0

# for i in range(1,num):
#    if num % i == 0:
#        digit += i 
#    else :
#        pass
   
# print(digit)
# if num == digit:
#     print(True)
# else:
#     print(False)

# Q5. Strong Number

# Input: 145 → True
# (1! + 4! + 5! = 145)
# import math
# num = 145 
# digit = 0
# fact = 0
# remainder = 0

# while num >0:
#     remainder = num % 10
#     fact += math.factorial(remainder)
#     num //=10

# print(fact)

# 🔹 Section B: Loop + Condition Mastery
# Q6. Count Frequency of Digits

# Input: 112233
# Output:

# 1 → 2 times  
# 2 → 2 times  
# 3 → 2 times

# n = input()
# freq = {}

# for ch in n:
#     freq[ch] = freq.get(ch, 0) + 1

# for k, v in freq.items():
#     print(k, "→", v)

# Q7. Sum of Even Indexed Digits

# Input: 12345
# Output: 1 + 3 + 5 = 9

# n = input()

# total = 0
# for i in range(0, len(n), 2):
#     total += int(n[i])

# print(total)

# Q8. Binary to Decimal

# Input: 1011 → 11

# binary = input()

# decimal = 0
# power = 0

# for digit in reversed(binary):
#     decimal += int(digit) * (2 ** power)
#     power += 1

# print(decimal)

# Q9. Decimal to Binary (No built-in)

# 👉 Reverse logic + remainder

# n = int(input())

# binary = ""

# while n > 0:
#     binary = str(n % 2) + binary
#     n //= 2

# print(binary)

# Q10. Check Harshad Number

# A number divisible by sum of its digits
# Input: 18 → True

# numbers = 0
# num = 18
# digit = num
# sm =0

# while  num > 0:
#     numbers = num % 10 
#     sm += numbers
#     num //= 10

# print(sm)
# print(digit)

# if digit % sm == 0 :
#     print(True)
# else:
#     print(False)

# Q11. Right Triangle (Numbers)
# 1
# 12
# 123
# 1234

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
    
    
# Q12. Reverse Triangle
# ****
# ***
# **
# *

# for i in range(5 , 0 , -1):
#     print('*' * i)

# Q13. Pyramid Pattern
#   *
#  ***
# *****

# n = 5

# for i in range(1 , n+1):
#     print( ' ' *(n-i)  + '*' * (2 * i - 1))
    
# 🔹 Section D: Prime + Advanced Logic
# Q14. Print all primes in range

# Input: 1 to 20
# rng = 20
# for num in range(rng+1):
#     if num < 2:
#         continue
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")
    
# Q15. Count primes in range
# rng = 20 
# count = 0

# for num in range(rng+1):
#     if num <2:
#         continue
#     for i in range(2, int(num**0.5) + 1):
#         if num % i ==0:
#             break
#     else:
#         count += 1
        
# print(count)
# Q16. Twin Primes

# Example: (3,5), (5,7), (11,13)

# 👉 Difference = 2

# 🔹 Section E: Slightly Tricky (Interview Style)
# Q17. Reverse Only Even Digits

# Input: 123456
# Output: 163452
n = list(input())

evens = [d for d in n if int(d) % 2 == 0]
evens.reverse()

result = []
idx = 0

for d in n:
    if int(d) % 2 == 0:
        result.append(evens[idx])
        idx += 1
    else:
        result.append(d)

print("".join(result))
      
# Q18. Check Automorphic Number

# Input: 25 → True
# (25² = 625 → ends with 25)

# Q19. Sum of Series
# 1 + 11 + 111 + 1111 ... n terms
# Q20. Missing Number in Range

# Input: [1,2,4,5] → Output: 3