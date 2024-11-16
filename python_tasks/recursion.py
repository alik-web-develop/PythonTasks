# ==================TASK_1==============
# x = [1,23,3,4,5,7,8,8]
# def all_sum(arr, counter=0,result=0):
#     if counter < len(x):
#         return all_sum(arr,counter+1,result+arr[counter])
#     else:
#         return result
# print(all_sum(x))

# ==================TASK_3==============
# x = [1, 2, [3, 4], [5, 6,8]]
# def all_sum(arr, result=0, counter=0):
#     if len(arr) > counter:
#         if type(arr[counter]) == type(1):
#             return all_sum(arr, result+arr[counter], counter+1)
#         else:
#             return all_sum(arr, result+sum(arr[counter]), counter+1)
#     else:
#         return result
# print(all_sum(x))

# ==================TASK_4==============
# x = -5


# def num_factorial(num, result=1):
#     if num > 1:
#         return num_factorial(num-1, result=result * num)
#     elif num < 0:
#         return "your number is less than zero"
#     else:
#         return result


# print(num_factorial(x))

# ==================TASK_5==============
# def fib_nums(num,result=[1,2]):
#! "первый вариант вам дасть количество фибоначчи чисел например ессли скажете 7 фибоначчи чисел то он дасть вам лист в котором 7 чисел фибонначи"
# if num > 2:
#     result.append(result[-1]+result[-2])
#     return fib_nums(num-1,result)
# !=====================================================
# ! второй вариант это до какого то число например до 90 а не просто 90 чисел
# if num > result[-1]:
#     result.append(result[-1]+result[-2])
#     return fib_nums(num-1,result)
# !=====================================================
#     else:
#         return result
# print(fib_nums(150))
# ==================TASK_6================
# x = 345
# def sumDigits(num,result=0,counter=0):
#     if counter < len(str(num)):
#         return sumDigits(num,result+int(str(num)[counter]),counter+1)
#     else:
#         return result
# print(sumDigits(x))
# ==================TASK_7================
# x = 11
# def sum_series(num,result=0,counter=0):
#     if num+1 > counter:
#         return sum_series(num, result+counter, counter+1)
#     else:
#         return result
# print(sum_series(6))
# # ==================TASK_10================
# def power_num(num2, num1, result=1, counter=0):
#     if num1 > counter:
#         return power_num(num2, num1, result*num2, counter+1)
#     else:
#         return result


# print(power_num(3, 4))

# # ==================TASK_10================
# def Nod(num1, num2, result=0, counter=1):
#     if num1 > num2:
#         if num1 > counter:
#             if num1 % counter == 0 and num2 % counter == 0:
#                 result = counter
#                 return Nod(num1, num2, result, counter+1)
#             else:
#                 return Nod(num1, num2, result, counter+1)
#         return result
#     elif num2 > num1:
#         if num2 > counter:
#             if num1 % counter == 0 and num2 % counter == 0:
#                 result = counter
#                 return Nod(num1, num2, result, counter+1)
#             else:
#                 return Nod(num1, num2, result, counter+1)
#         else:
#             return result
#     else:
#         return num1


# print(Nod(90,140))

print("hello,world"*32)