# Importanat rules for array:
# -> for travering an array:
# we use "for i in range(len(array)):"
#  mainly used for:
#               -> max/min
#               -> counting
#               -> searching
# we use nested loops:
#  for i 
#     for j
# mainly used for:
#            -> duplicates
#            -> brute-force pairs
#            -> subarrays
#Array are also used for:
# -> prefix sum
# -> cumulative sum
# -> sliding window technique
#   - to find fixed size subarray
#   - maximum/minium window sum
#   Key points of sliding window :
#       -> To find the max sum, average and subarray sums we use: new = previous_sum - outgoing + incoming
#       -> To find duplicates, substring problem and distinct element we use: set() or hashmap

# -> kadane's algorithm is used for maximum sum of subarray
# -> Two pointer technique is used for:
#   - finding pairs with a given sum
#   - sorting an array
#   - reversing


# To find the largest and second largest elements in an array, you can use the following code:
# arr = [10, 3, 25, 7, 18]

# largest = arr[0]
# second_largest = float('-inf')

# for i in arr:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif largest > i > second_largest:
#         second_largest = i
# print(largest)
# print(second_largest)

# For finding the maximum and minimum elements in an array, you can use the following code:

# arr = [10, 3, 25, 7, 18]

# def max_min(arr):
#     maximum = arr[0]
#     minimum = arr[0]
#     for i in arr:
#         if i > maximum:
#             maximum = i
#         elif i < minimum:
#             minimum = i
#     return maximum, minimum
# print(max_min(arr))

# For revesing an array

# arr = [10, 3, 25, 7, 18]

# left = 0
# right = len(arr)-1

# while left < right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1
# print(arr)

# To identify number of even elements in an array, you can use the following code:

# arr = [10, 3, 25, 7, 18, 4, 11]
# even = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even += 1
# print(even)

# For finding the number of elements greater than a certain value in an array, you can use the following code:

# arr = [10, 3, 25, 7, 18, 4, 11]

# nums_greater_than_15 = 0

# for i in range(len(arr)):
#     if arr[i] > 15:
#         nums_greater_than_15 += 1
# print(nums_greater_than_15)

# To calculate the sum of all elements in an array, you can use the following code:
# arr = [10, 3, 25, 7, 18, 4, 11]

# total_sum = 0

# for i in range(len(arr)):
#     total_sum += arr[i]
# print(total_sum)

# To calculate the average of all elements in an array, you can use the following code:
# arr = [10, 3, 25, 7, 18, 4, 11]

# total_sum = 0
# count = 0

# for i in range(len(arr)):
#     total_sum += arr[i]
#     count += 1
# average = total_sum / count
# print(average) 

# To find the index of the largest element in an array, you can use the following code:
# arr = [10, 3, 25, 7, 18]
# val = arr[0]
# ind = 0
# for i in range(len(arr)):
#     if arr[i] > val:
#         val = arr[i]
#         ind = i
# print(f"Value:{val}, Index:{ind}")

# To count the number of occurrences of a specific element in an array, you can use the following code:
# arr = [5, 3, 7, 5, 2, 5, 9]
# target = 5
# count = 0

# for i in range(len(arr)):
#     if target == arr[i]:
#         count += 1
# print(count)

# To find the index of the first occurrence of a specific element in an array, you can use the following code:
# arr = [5, 3, 7, 5, 2, 5, 9]
# target = 5

# for i in range(len(arr)):
#     if target == arr[i]:
#         print(i)
#         break

# To find the index of the last occurrence of a specific element in an array, you can use the following code:

# arr = [5, 3, 7, 5, 2, 5, 9]
# target = 5

# index = -1

# for i in range(len(arr)):
#     if arr[i] == target:
#         index = i

# print(index)

# To find the minimum element in an array, you can use the following code:
# arr = [10, 3, 25, 7, 18]
# maximum = arr[0]
# minimum = arr[0]
# for i in range(len(arr)):
#     if arr[i] > maximum:
#         maximum = arr[i]
#     elif arr[i] < minimum:
#         minimum = arr[i]
# print(minimum)

# to search for a specific element in an array, you can use the following code:

# arr = [10, 3, 25, 7, 18]
# target = int(input())

# found = False

# for num in arr:
#     if num == target:
#         found = True
#         break

# if found:
#     print("Element found")
# else:
#     print("Element not found")

# To check if an array is sorted in ascending order, you can use the following code:
# arr = [10, 3, 25, 7, 18]

# sort_flag = True
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 sort_flag = False
#                 break
# if sort_flag:
#      print("Array is sorted")
# else:
#      print("Array is not sorted")

# To calculate the difference between the largest and smallest elements in an array, you can use the following code:

# arr = [10, 3, 25, 7, 18]

# largest = arr[0]
# smallest = arr[0]

# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#     elif arr[i] < smallest:
#         smallest = arr[i]
# diff = largest - smallest
# print(f"Difference between largest and smallest: {diff}")

# To find the duplicate elements in an array, you can use the following code:
# arr = [1, 3, 4, 2, 3, 1, 5]

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:
#             already_print = False

#             for k in range(i):
#                 if arr[k] == arr[i]:
#                     already_print = True

#             if not already_print:
#                 print(arr[i])

# To find the missing number in an array containing numbers from 1 to n, you can use the following code:

# arr = [1,2,3,5]
# n = len(arr)+1

# expected_sum = n*(n+1)//2

# actual_sum = 0
# for i in arr:
#     actual_sum += i
# print(expected_sum - actual_sum)

# To rotate an array to the right by one position, you can use the following code:
# arr = [1,2,3,4,5]
# last = arr[-1]

# for i in range(len(arr)-1,0,-1):
#     arr[i] = arr[i-1]
# arr[0] = last
# print(arr)

# To rotate an array to the left by one position, you can use the following code:
# arr = [1,2,3,4,5]

# first = arr[0]

# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
# arr[len(arr)-1] = first

# print(arr)

# To find the number of pairs in an array that sum up to a specific target value, you can use the following code:

# arr = [0,1,0,3,12]

# pos = 0

# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[pos] = arr[i]
#         pos += 1
# for i in range(pos , len(arr)):
#     arr[i] = 0
# print(arr)

# To find the indices of two numbers in an array that sum up to a specific target value, you can use the following code:

# arr = [2,7,11,15]
# target = 9

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i,j)

# To find the prefix sum of an array, you can use the following code:         
# arr = [1,2,3,4]

# pre = [0]*len(arr)

# pre[0] = arr[0]

# for i in range(1, len(arr)):
#     pre[i] = pre[i-1] + arr[i]
# print(pre)

# Kadane's algorithm for finding the maximum sum of an array[subarray] fixed size

# arr = [2, -3, 4, -1, 2]

# c_sum = 0
# max_sum = float('-inf')

# for i in arr:
#     c_sum += i

#     if c_sum > max_sum:
#         max_sum = c_sum
#     if c_sum < 0:
#         c_sum = 0
# print(max_sum)  

# Sliding window technique for finding the maximum sum of a subarray of size k

# formula of sliding window technique is:
# new_sum = old_sum - element_out + element_in

# arr = [2,1,5,1,3,2]

# k = 3

# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k , len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     max_sum = max(max_sum, window_sum)
# print(max_sum)  


# To find the maximum sum of a subarray of size k using sliding window technique, you can use the following code:
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

# arr = [6,2,1,3,4]
# k = 2

# window_sum = 0 
# for i in range(k):
#     window_sum += arr[i]
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]

#     if window_sum > max_sum:
#         max_sum = window_sum
# print(max_sum)

# To find the indices of two numbers in an array that sum up to a specific target value using a more efficient approach, you can use the following code:

# arr = [2,7,11,15]
# target = 9

# seen = {}

# for i in range(len(arr)):
#     num = arr[i]

#     comp = target - num

#     if comp in seen:
#         print(seen[comp],i)
#         break
#     seen[num] = i


# To pair sum problem using brute-force approach: O(n^2)
# arr = [1,5,3,7]
# target = 8


# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i],arr[j])
#             break -> only used for showing only a single pair


# Hash map approach: O(n)
# arr = [8,3,2,4]
# target = 6
# seen = {}

# for i in range(len(arr)):
#     num = arr[i]
#     need = target - num

#     if need in seen:
#         print(num,need)
#         break
#     seen[num] = i


# Frequency count of elements in an array:

# arr = [1,2,2,3,3,3]
# freq = {}

# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)


# To find the most frequent element in an array, you can use the following code:

# arr = [1,2,2,3,3,3]
# freq = {}

# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# count = 0
# result = None

# for key in freq:
#     if freq[key] > count:
#         count = freq[key]
#         result = key
# print(result)

# To find the frequency of each element in an array by using get()

# arr = [4,4,2,2,2,7,7,7,7]
# freq = {}

# for num in arr:
#     freq[num] = freq.get(num, 0) + 1
# print(freq)


# To find the most frequent element in an array, you can use the following code:

# arr = [5,5,5,2,2,3,3,3,3]

# freq = {}
# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# max_freq = 0
# result = None
# for key in freq:
#     if freq[key] > max_freq:
#         max_freq = freq[key]
#         result = key
# print(result)

# To find duplicates      
# arr = [1,2,3,1]

# freq = set()

# for i in arr:
#     if i in freq:
#         print(i)
#         break
#     freq.add(i)


# To find the longest substring using set

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
