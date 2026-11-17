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
        if char == "a":
            count += 1
    return count
#2
def average(numbers: list[int]) -> float:
    totaal = sum(numbers)
    aantal = len(numbers)
    average = totaal / aantal
    return round(average, 2)
#3
def index_max(numbers: list[int]) -> int:
    huidige_max = numbers[0]
    for number in numbers:
        if number > huidige_max:
            huidige_max = number
    return numbers.index(huidige_max)
#4
def long_words(words: list[str]) -> list[str]:
    new_list = []
    for word in words:
        if len(word) > 4:
            new_list.append(word)
    return new_list
#5
def passed(grades: list[float]) -> bool:
    for grade in grades:
        if grade < 4:
            return False
    if sum(grades) / len(grades) >= 5.5:
        return True
    return False
#6
def count_words(sentence: str) -> str:
    spaties = 0 
    for word in sentence:
        if word == " ":
            spaties += 1
    aantal_woorden = spaties + 1
    return aantal_woorden
#7
def sum_to_n_while(n: int) -> int:
    total = 0
    i = 1
    while i <= n:
        total += i
        i +=1
    return total
#8
def is_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    return False
        
# 9
def second_largest(numbers: list[int]) -> int:
    numbers.sort()
    return numbers[-2]
#10
def discounted_price(price: float, age: int) -> float:
    if age < 12: 
        price = price * 0.8
    elif age >= 65:
        price = price * 0.9
    else:
        price = price
        
    return price
#1
def first_a(text: str) -> int:
    for char in text:
        if char == "a":
            char = char_a
        return text.index(char_a)
#2
def sum_even(n: int) ->int:
    total = 0
    for n in range(0, n, 1):
        if n % 2 == 0:
            
    

    
    
