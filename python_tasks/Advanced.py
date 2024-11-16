#todo=========================================ADVANCED_TASKS==========================
#?==============================CREATE_ID=====================
# import random
# def create_id(num):
#     result = ""
#     letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#     for _ in range(num):
#         random_num = int(random.random() * len(letters))
#         result += letters[random_num]
#     return result
# print(create_id(10))

#?==============================Upper_first_letter=====================
# text = "hello world this is text"
# def upper_first_letter(arr):    
#     result = []
#     for i in arr.split(" "):
#         word = i[0].upper() + i[1:len(i)]
#         result.append(word)
#     return str(result).replace("'", "").replace(",", "").replace("]","").replace("[","")
# print(upper_first_letters(text))

#?==============================Reverse_str_in_arr=====================
# texts = ["Hello world", "This is text", "In the world", "Easy"]
# def reverse_arr(arr):
#     result = []
#     for i in arr:
#         result.append(i[::-1])
#     return result
# print(reverse_arr(texts))
#?==============================sorting_by_length_of_text_inside_anarray=====================
# text = ["Hello", "world","bubble","sort"]
# def bubble_str_sort(arr):
#     for j in arr:
#         for i in range(len(arr) - 1):
#             if len(arr[i]) > len(arr[i+1]):
#                 arr[i], arr[i+1] = arr[i+1],arr[i]
#     return str(arr).replace("'", "").replace(",", "").replace("]","").replace("[","")
# print(bubble_str_sort(text))
#?==============================replace_vowels_with_the_following_vowels=====================
# text = "replace vowels with the following vowels"
# def change_next_vowels(arr):
#     arr = list(arr)
#     for i in range(len(arr)):
#         if arr[i] == "a":
#             arr[i] = "e"
#         elif arr[i] == "e":
#             arr[i] = "i" 
#         elif arr[i] == "i":
#             arr[i] = "o" 
#         elif arr[i] == "o":
#             arr[i] = "u" 
#         elif arr[i] == "u":
#             arr[i] = "a"
            
#     return "".join(arr)
# print(change_next_vowels(text))
#?===========================Origin_symbol===========================
# text = "Hello world this is test text"
# def most_frequent_char(string):
#     max_count = 0
#     most_frequent = ''
    
#     for char in string:
#         if char == ' ':
#             continue
#         count = 0
#         for c in string:
#             if c == char:
#                 count += 1
        
#         if count > max_count:
#             max_count = count
#             most_frequent = char
    
#     return most_frequent
# print(most_frequent_char(text))
#?===========================replace_first_symbol===========================
# text = "This is test text"
# def replace_first(arr):
#     first_letter = arr[0]
#     arr = arr.replace(first_letter.lower(),"$")
#     arr = first_letter + arr[1:]
#     return arr
# print(replace_first(text))

#?===========================repeat_letters=================================
# text = "task"
# def repeat_letters(arr):
#     for i in arr:
#         counter = 0
#         for j in arr:
#             if i == ' ':
#                 continue
#             if i == j:
#                 counter += 1
#         if counter > 1:
#             return True
#     return False
# print(repeat_letters(text))
#?===========================repeat_letters=================================
