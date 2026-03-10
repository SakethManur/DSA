# s = "hello"

# reversed_string = s[::-1]
# print(reversed_string)

# s = "madam"

# if s == s[::-1]:
#     print("True")

# arr = [3,7,2,9,4]
# max_num = 0

# for i in arr:
#     if max_num < i:
#         max_num = i
# print(max_num)

# s = "placement"

# sort_s = sorted(s)
# count = 0
# for i in sort_s:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count += 1
# print(count)

# arr = [1,3,4,2,2]

# seen = set()

# duplicates = set()

# for i in arr:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)
# print(duplicates)

# nums = [2,7,11,15]
# target = 9

# seen = {}

# for i in range(len(nums)):
#     num = nums[i]

#     comp = target - num

#     if comp in seen:
#         print(seen[comp],i)
#         break
#     seen[num] = i

# i dont know 

# s = "listen"
# t = "silent"

# def check_anagram(s,t):
#     sorted_s = sorted(s)
#     sorted_t = sorted(t)

#     return sorted_s == sorted_t

# if (check_anagram(s,t)):
#     print("True")
# else:
#     print("False")



# s = "I love coding"
# reversed_s = " ".join(s.split()[::-1])
# print(reversed_s)


# arr = [3,0,1]
# sort_arr = sorted(arr)
# n = len(sort_arr)+1
# expected_sum = (n+1)//2

# actual_sum = 0

# for i in arr:
#     actual_sum += i

# print(abs(expected_sum - actual_sum))

# arr = [-2,1,-3,4,-1,2,1,-5,4]

# c_sum = 0
# max_sum = float('-inf')

# for i in arr:
#     c_sum += i

#     if c_sum > max_sum:
#         max_sum = c_sum
#     if c_sum < 0:
#         c_sum = 0
# print(max_sum)

# arr = [2,1,5,1,3,2]
# k = 3

# window_sum = 0

# for i in range(k):
#     window_sum += arr[i]

# max_sum = window_sum

# for i in range(k , len(arr)):
#         window_sum = window_sum - arr[i-k] + arr[i]
#         if window_sum > max_sum:
#             max_sum = window_sum
# print(max_sum)

# s = "abcabcbb"
# seen = set()
# left = 0
# max_len = 0

# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1
#     seen.add(s[right])
#     max_len = max(max_len, right - left + 1)
# print(max_len)



