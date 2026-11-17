# #1
# def absolute_difference(a : int, b: int) -> int:
#     difference = abs(a - b)
#     return difference
# #2
# def is_even(n: int) ->bool:
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#  #3      
# def discount(age: int) -> bool:
#     if age < 12: 
#         return True
#     elif age >= 65:
#         return True
#     else:
#         return False
# #4   
# def sum(n: int) -> int:
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# #5
# def count_words(words: list[str], target: str) -> int:
#     count = 0 
#     for word in words:
#         if word == target:
#             count += 1
#     return count
# #6
# def maximum(numbers: list[int]) -> int:
#     huidige_max = numbers[0]
#     for number in numbers:
#         if number > huidige_max:
#             huidige_max = number
#     return huidige_max
    
# #7
# def even_numbers(numbers: list[int]) -> list[int]:
#     even_numbers = []
#     for number in numbers: 
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers
# #8
# def meal(time: str) -> str:
#     uur, minuten = time.split(":")
#     uur = int(uur)
#     minuten = int(minuten)
#     tijd = uur * 60 + minuten
#     if tijd >= 420 and tijd <= 480:
#         return "breakfast"
#     elif tijd >= 720 and tijd <= 780:
#         return "lunch"
#     elif tijd >= 1080 and tijd <= 1140:
#         return "dinner"
#     else:
#         return "unknown"

#1
def count_a(text: str) -> int:
    count = 0
    for char in text: 
        if "a" in text:
            count += 1
    return count
#2
def average(numbers: list[int]) -> float:
    totaal = numbers.sum()
    aantal = len(numbers)
    average = totaal / aantal
    return round(average, 2)
#3
def 
