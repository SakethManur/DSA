
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
