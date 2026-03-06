# arr = [1, 2, 3, 4, 5]

# # def get_all(arr):
# #     for i in arr:
# #         print(i)

# # print(get_all(arr))
# # def example(arr):
# #     for i in range(len(arr)):
# #         print(arr[i])
# #     print("Done")
# # example(arr)

# Recursion
# def print_nums(n):
#     if n == 0:    # Base case
#         return
#     print(n)
#     print_nums(n-1) #Recursive function
# # print_nums(10)

# Factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(10))

# def mystery(n):
#     if n==0:
#         return 1
    
#     mystery(n-1)
    
#     print(n)
# mystery(3)
# Sum of nums
# def sum_n(n):
#     if n == 0:
#         return 0 
#     return n + sum_n(n-1)

# print(sum_n(10))

# Reverse string
# def rev(s):
#     if len(s) == 0:
#         return ""
#     return rev(s[1:]) + s[0]
# print(rev("Hello World"))

# Fibonacci sequence
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(10))

#Memoized Fiboo
# def fibo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0 or n == 1:
#         return n
#     memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
#     return memo[n]
# print(fibo(50))


# Nums from N to 1
# def print_nums(n):
#     if n <= 1:                
#         print(n)
#         return 
#     print(n)          
#     print_nums(n-1)

# print_nums(10)
    
# Nums from 1 to N
# def print_nums(n):
#     if n <= 1:
#         print(n)
#         return
#     print_nums(n-1)
#     print(n)
# print_nums(10)

# counting number of digits

# def count_digits(n):
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)
# print(count_digits(12345))

# For counting all negative numbers
# def count_negatives(n):
#     n =abs(n)

#     if n<10:
#         return 1
#     return 1 + count_negatives(n//10)
# print(count_negatives(-1234))