
# Question 1
# arr = [8, 3, 10, 2, 7]

# largest = arr[0]
# smallest = arr[0]

# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#     elif arr[i] < smallest:
#         smallest = arr[i]
# diff = largest - smallest

# print(diff)

# Question 2

# arr = [4, 1, 6, 2, 1, 8]
# seen = set()

# for num in arr:
#     if num in seen:
#         print(True)
#         break
#     seen.add(num)

# Question 3

# arr = [1, 2, 3, 4, 6]
# target = 6

# left = 0

# right = len(arr) - 1

# while left < right:
#     s = arr[left] + arr[right]

#     if s == target:
#         print(arr[left], arr[right])
#         break
#     elif s < target:
#         left += 1
#     else:
#         right -= 1


# Question 4

# arr = [4,2,2,7,8,1,2,8,1,0]
# k = 3

# window_sum = 0

# for i in range(k):
#     window_sum += arr[i]

# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]

#     if window_sum > max_sum:
#         max_sum = window_sum
# print(max_sum)

# arr=[1,3,2,5,1,1,2,3]
# k = 3

# window_sum = 0

# for i in range(k):
#     window_sum += arr[i]
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     if window_sum > max_sum:
#         max_sum = window_sum
# print(max_sum)


# s = "I love coding"

# reverse_s = s[::-1]

# print(reverse_s)

# arr = [2,1,5,1,3,2]
# k = 3

# window_sum = 0

# for i in range(k):
#     window_sum += arr[i]
# max_sum = window_sum

# for i in range(k , len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     if window_sum > max_sum:
#         max_sum = window_sum
# print(max_sum)

# nums = [3,2,4]
# target = 6

# seen={}
# for i in range(len(nums)):

#     new = nums[i]
#     comp = target - new
#     if comp in seen:
#          print([seen[comp],i])
#     seen[new] = i

# nums = [1,3,4,2,2]

# freq = set()

# for i in nums:
#     if i in freq:
#         print(i)
#         break
#     freq.add(i)

# def check_anagram(s,t):
#     if len(s) != len(t):
#         return False
    
#     s1 = sorted(s)
#     s2 = sorted(t)

#     if s1 == s2:
#         return True

# s = "listen"
# t = "silent"

# if (check_anagram(s,t)):
#     print("True")
# else:
#     print("False")