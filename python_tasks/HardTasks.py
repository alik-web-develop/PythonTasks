# import itertools
# # ========================TAsk_N2==============
# x = [1, 2, 3, 4, 120, 6, 7, 8, 9, 10, 140, 11, 12, 13, 14, 15, 16, 17, 18,19]


# def longest_sequen(arr):
#     result = 0
#     counter = 0
#     for i in range(len(arr)-1):
#         if arr[i]+1 == arr[i+1]:
#             counter += 1
#             if counter > result:
#                 result = counter
#         else:
#             counter = 0
#     return result

# ЮД
# ,KeyboardInterruptf
# print(longest_sequen(x))


# #todo========================TAsk_N3==============
# # x = [1,2,3]
# # def all_options(arr):
# #     return list(itertools.permutations(arr))
# # print(all_options(x))
# #todo========================TAsk_N4==============
# # x = [3,4,1,5,76,7,3,12,23,4,6,12,90]
# # def k_smallest(arr):
# #     return sorted(arr)[0]
# # print(k_smallest(x))
# #todo========================TAsk_N5==============
# # x = [3,4,1,5,76,7,3,12,23,4,6,12,90]
# # def k_biggest(arr):
# #     return sorted(arr)[-1]
# # print(k_biggest(x))
# #todo========================TAsk_N6==============
# # x = [1,2,3]
# # def polindrome(arr):
# #     return arr[::-1] == arr
# # print(polindrome(x))
# #todo========================TAsk_N7==============
# # x = ["Hello","world","this","is","text"]
# # y = ["this","a","phone"]
# # def plus_lists(arr1,arr2):
# #     result = []
# #     for i in arr1:
# #         if i in arr2:
# #             result.append(i)
# #     return f" Union of said two lists {list(set(arr1+arr2))} \n and Intersection of said two lists: {result}"
# # print(plus_lists(x,y))
# #todo========================TAsk_N8==============
# # x = ["Hello","world","this","this","is","is","is","Hello","text"]
# # def no_repeat(arr):
# #     result = ""
# #     for i in arr:
# #         if i not in result:
# #             result += (i+" ")
# #     return result
# # print(no_repeat(x))
# #todo========================TAsk_N9==============
# # x = [1,2,3,4,5,6,7,8,9,10]
# # def pairs_sum(arr,x):
# #     result = []
# #     for i in arr:
# #         for y in arr:
# #             if (i + y) == x:
# #                 result.append(f"{i} and {y}")
# #     return result
# # print(pairs_sum(x,19))

