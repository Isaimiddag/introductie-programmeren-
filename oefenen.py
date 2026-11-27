# # #1
# # def absolute_difference(a : int, b: int) -> int:
# #     difference = abs(a - b)
# #     return difference
# # #2
# # def is_even(n: int) ->bool:
# #     if n % 2 == 0:
# #         return True
# #     else:
# #         return False
# #  #3      
# # def discount(age: int) -> bool:
# #     if age < 12: 
# #         return True
# #     elif age >= 65:
# #         return True
# #     else:
# #         return False
# # #4   
# # def sum(n: int) -> int:
# #     total = 0
# #     for i in range(1, n + 1):
# #         total += i
# #     return total

# # #5
# # def count_words(words: list[str], target: str) -> int:
# #     count = 0 
# #     for word in words:
# #         if word == target:
# #             count += 1
# #     return count
# # #6
# # def maximum(numbers: list[int]) -> int:
# #     huidige_max = numbers[0]
# #     for number in numbers:
# #         if number > huidige_max:
# #             huidige_max = number
# #     return huidige_max
    
# # #7
# # def even_numbers(numbers: list[int]) -> list[int]:
# #     even_numbers = []
# #     for number in numbers: 
# #         if number % 2 == 0:
# #             even_numbers.append(number)
# #     return even_numbers
# # #8
# # def meal(time: str) -> str:
# #     uur, minuten = time.split(":")
# #     uur = int(uur)
# #     minuten = int(minuten)
# #     tijd = uur * 60 + minuten
# #     if tijd >= 420 and tijd <= 480:
# #         return "breakfast"
# #     elif tijd >= 720 and tijd <= 780:
# #         return "lunch"
# #     elif tijd >= 1080 and tijd <= 1140:
# #         return "dinner"
# #     else:
# #         return "unknown"

# #1
# def count_a(text: str) -> int:
#     count = 0
#     for char in text: 
#         if char == "a":
#             count += 1
#     return count
# #2
# def average(numbers: list[int]) -> float:
#     totaal = sum(numbers)
#     aantal = len(numbers)
#     average = totaal / aantal
#     return round(average, 2)
# #3
# def index_max(numbers: list[int]) -> int:
#     huidige_max = numbers[0]
#     for number in numbers:
#         if number > huidige_max:
#             huidige_max = number
#     return numbers.index(huidige_max)
# #4
# def long_words(words: list[str]) -> list[str]:
#     new_list = []
#     for word in words:
#         if len(word) > 4:
#             new_list.append(word)
#     return new_list
# #5
# def passed(grades: list[float]) -> bool:
#     for grade in grades:
#         if grade < 4:
#             return False
#     if sum(grades) / len(grades) >= 5.5:
#         return True
#     return False
# #6
# def count_words(sentence: str) -> str:
#     spaties = 0 
#     for word in sentence:
#         if word == " ":
#             spaties += 1
#     aantal_woorden = spaties + 1
#     return aantal_woorden
# #7
# def sum_to_n_while(n: int) -> int:
#     total = 0
#     i = 1
#     while i <= n:
#         total += i
#         i +=1
#     return total
# #8
# def is_palindrome(word: str) -> bool:
#     if word == word[::-1]:
#         return True
#     return False
        
# # 9
# def second_largest(numbers: list[int]) -> int:
#     numbers.sort()
#     return numbers[-2]
# #10
# def discounted_price(price: float, age: int) -> float:
#     if age < 12: 
#         price = price * 0.8
#     elif age >= 65:
#         price = price * 0.9
#     else:
#         price = price
        
#     return price
# #1
# def first_a(text: str) -> int:
#     return text.index("a")
# #2
# def sum_even(n: int) ->int:
#     total = 0
#     even = []
#     for n in range(0, n+1):
#         if n % 2 == 0:
#             even.append(n)
#     return sum(even)
# #3
# def index_of_min(numbers: list[int]) -> int:
#     huidige_min = numbers[0]
#     for number in numbers:
#         if number < huidige_min:
#             huidige_min = number
#     return nuumbers.index(huidige_min)
# #4
# def count_max(numbers: list[int]) -> int:
#     count = 0
#     maximum = max(numbers)
#     for number in numbers:
#         if number == maximum:
#             count +=1
#     return count
# #5
# def countdown(n:int) -> list[int]:
#     result = []
#     while n >= 1:
#         result.append(n)
#         n -= 1
#     return result

# #6
# def middle(numbers: list[int]) -> int:
#     aantal = len(numbers)
#     mid = aantal // 2
#     return numbers[mid]
# #9
# def reverse_list(numbers: list[int]) -> list[int]:
#     result = [] 
#     i = len(numbers) -1
#     while i >= 0:
#         result.append(numbers[i])
#         i -+ 1
#     return result

# def encrypt(s: str) -> str:
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     resultaat = ""
#     for letter in s:
#         for i in range(len(alfabet)):
#             if letter == alfabet[i]:
#                 positie = i
#                 nieuwe_postie = 25 - i
#                 nieuwe_letter = alfabet[nieuwe_postie]
#                 resultaat += nieuwe_letter
#     return resultaat
    
# def vowely_words(words: list[str]) -> list[str]:
#     resultaat = []
#     klinkers = "aeiou"

#     for woord in words:
#         aantal_klinkers = 0

#         for letter in woord:
#             if letter.lower() in klinkers:
#                 aantal_klinkers += 1

#         if aantal_klinkers >= 2:
#             resultaat.append(woord)

# #1
# def shortest_word_length(s: str) -> int:
#     huidig_woord = 0
#     kortste_woord = 0
#     aantal_woorden = 0
#     for letter in s:
#         if letter != " ":
#             huidig_woord += 1
#         else:
#             if aantal_woorden == 0 or huidig_woord < kortste_woord:
#                 kortste_woord = huidig_woord
#             aantal_woorden += 1
#             huidig_woord = 0
#     if aantal_woorden == 0 or huidig_woord < kortste_woord:
#         kortste_woord = huidig_woord

#     return kortste_woord
# #2
# def shift_forward(s: str) ->str :
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     resultaat = ""
#     for letter in s:
#         for i in range(len(alfabet)):
#             if letter == alfabet[i]:
#                 positie = i
#                 nieuwe_positie = (positie + 1) % 26 
#                 nieuwe_letter = alfabet[nieuwe_positie]
#                 resultaat += nieuwe_letter
#     return resultaat
    
# #3
# def three_vowel_words(words: list[str]) -> list[str]:
#     lijst = []
#     klinkers = "aeiouAEIOU"
#     for word in words: 
#         aantal_klinkers = 0
#         for letter in word:
#             if letter in klinkers:
#                 aantal_klinkers += 1
                
#         if aantal_klinkers == 3:
#             lijst.append(word)
#     return lijst
    
    
# #4
# def longer_than_average(words: list[str]) -> list[str]:
#     lijst = []
#     totaal_letters = 0
#     aantal_woorden = 0
#     for word in words:
#         aantal_letters = 0
        
#         for letter in word:
#             if letter.isalpha():
#                 aantal_letters += 1
#         totaal_letters += aantal_letters
#         aantal_woorden += 1
#     gemiddelde = totaal_letters / aantal_woorden
    
#     lijst = []
#     for word in words:
#         aantal_letter = 0

#         for letter in word:
#             if letter.isalpha():
#                 aantal_letter += 1

#         if aantal_letter > gemiddelde:
#             lijst.append(word)

#     return lijst

# #5
# # (aantal klinkers × 2) + aantal medeklinkers
# def word_score(word: str) ->int:
#     klinkers = "aeiouAEIOU"
#     aantal_klinkers = 0 
#     medeklinkers = 0
#     for letter in word:
#         if letter in klinkers:
#             aantal_klinkers += 1
#         else:
#             medeklinkers +=1
        
#     score = (aantal_klinkers *2) + medeklinkers
#     return score
# #6
# def same_letter(a: str, b:str) -> bool:
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     for letter in alfabet:
#         count_a = 0
#         count_b = 0
#         for teken in a:
#             if teken == letter:
#                 count_a += 1
#         for teken in b:
#             if teken == letter:
#                 count_b += 1
#         if count_a != count_b:
#             return False
#         else:
#             return True
                
# #1
# def count_long_words(words: list[str], minimum: int) -> int:
#     """
#     >>> count_long_words(["kat", "hallo", "ik", "poep"], 5)
#     1
#     >>> count_long_words(["HALLO", "ik", "hoi"], 2)
#     3
#     >>> count_long_words(["poep", "bal", "vless"], 8)
#     0
#     """
#     aantal_woorden = 0
#     for word in words:
#         if len(word) >= minimum:
#             aantal_woorden +=1 
#     return aantal_woorden
# #2            
# def replace_vowels(word: str) -> str:
#     """
#     >>> replace_vowels("Hallo")
#     'H*ll*'
#     >>> replace_vowels("ho")
#     'h*'
#     >>> replace_vowels("a")
#     '*'
#     >>> replace_vowels("b")
#     'b'
#     """
#     new_word = ""
#     klinkers = "aeiouAEIOU"
#     for letter in word:
#         if letter in klinkers:
#             letter = "*"
#         else:
#             letter = letter
#         new_word += letter
            
#     return new_word
# #3
# def average_word_length(words: list[str]) -> float:
#     aantal_woorden = len(words)
#     aantal_letters = 0 
#     for word in words:
#         for letter in word:
#             if letter.isalpha():
#                 aantal_letters +=1
    
#     score = aantal_letters / aantal_woorden
#     return score
    
# #4
# def longest_consonant_word(words: list[str]) -> str:
#     klinkers = "aeiouAEIOU"
#     langste = ""
#     for word in words:
#         bevat_klinker = False
#         for letter in word:
#             if letter in klinkers:
#                 bevat_klinker = True
#         if not bevat_klinker: 
#             if len(word) > len(langste):
#                     langste = word
                    
#     return langste
# #5
# def word_count(sentence: str) -> int:
#     aantal_spaties = 0
#     for char in sentence:
#         if char == " ":
#             aantal_spaties += 1
#     aantal_woorden = aantal_spaties + 1
#     return aantal_woorden
    
# #6
# def shift_by_one(word: str) -> str:
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     resultaat = ""
#     for letter in word:
#         for i in range(len(alfabet)):
#             if letter == alfabet[i]:
#                 positie = i
#                 nieuwe_positie = (positie + 1) % 26 
#                 nieuwe_letter = alfabet[nieuwe_positie]
#                 resultaat += nieuwe_letter
#     return resultaat
# #7
# def two_vowel(words: list[str]) -> list[str]:
#     klinkers= "aeiouAEIOU"
#     new_list = []
#     for word in words:
#         aantal_klinkers = 0
#         for letter in word:
#             if letter in klinkers:
#                 aantal_klinkers +=1
#         if aantal_klinkers == 2:
#             new_list.append(word)
#     return new_list
# #9
# POINTS = [1,2,3,4,5]
# LETTERS = "abcde"
# def compute_word_score(word: str) -> int:
#     score = 0
#     for letter in word:
#         if letter == "a":
#             score +=1
#         elif letter == "b":
#             score += 2
#         elif letter == "c":
#             score += 3
#         elif letter == "d":
#             score+= 4
#         elif letter =="e":
#             score += 5
#         else:
#             score += 0
#     return score

# #10
# def same_letters(a:str, b:str) -> bool:
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     for letter in alfabet:
#         aantal_a = 0
#         aantal_b = 0
#         for teken in a:
#             if teken == letter:
#                 aantal_a +=1
#         for teken in b:
#             if teken == letter:
#                 aantal_b +=1
# #         if aantal_a != aantal_b:
# #             return False
# #         else:
# #             return True

# def count_short_words(words: list[str], maximum: int) -> int:
#     """
#     >>> count_short_words(["hallo", "ik", "jo"], 1)
#     0
#     >>> count_short_words(["Ha", "hoi"] ,5)
#     2
#     >>> count_short_words(["ik"], 4)
#     1
#     """
#     aantal_woorden = 0
#     for word in words: 
#         if len(word) <= maximum:
#             aantal_woorden +=1
#     return aantal_woorden

# def remove_vowels(word: str) -> str:
#     """
#     >>> remove_vowels("hallo")
#     'hll'
#     >>> remove_vowels("ho")
#     'h'
#     >>> remove_vowels("ik")
#     'k'
#     """
#     klinkers = "aeiouAEIOU"
#     new_word = ""
#     for letter in word:
#         if letter not in klinkers:
#             new_word += letter
#     return new_word


# def totaal_letters(words: list[str]) -> int:
#     """
#     >>> total_letters(["hoi", "doei"])
#     7
#     >>> totaal_letters(["ik"])
#     2
#     >>> totaal_letters(["kat", "pap"])
#     6
#     """
#     totaal = 0
#     for word in words:
#         for letter in word:
#             if letter.isalpha():
#                 totaal += 1
#     return totaal
    
# def shortest_vowel_word(words: list[str]) -> str:
#     klinkers = "aeiouAEIOU"
#     shortest = ""
#     woorden_klinker = []
#     for word in words:
#         for letter in word:
#             if letter in klinkers:
#                 woorden_klinker.append(word)
#     for word in woorden_klinker:
#         woorden_klinker[0] = shortest
#         if len(word) < len(shortest):
#             shortest = word
#     return shortest

# def space_count(sentence: str) -> int:
#     aantal_spaties = 0
#     for char in sentence:
#         if char == " ":
#             aantal_spaties += 1
#     return aantal_spaties

# def shift_by_two(word: str) -> str:
#     alfabet = "abcdefghijklmnopqrstuvwxyz"
#     new_word = ""
#     for letter in word:
#         for i in range(len(alfabet)):
#             if i == letter:
#                 new_letter = (i + 2) % 26
#                 new_word.append(new_letter)
#     return new_word
    
# def three_consonant_words(words: list[str]) -> list[str]:
#     klinkers = "aeiouAEIOU"
#     aantal_medeklinkers = 0
#     new_list = []
#     for word in words:
#         aantal_medeklinkers = 0
#         for letter in word:
#             if letter not in klinkers:
#                 aantal_medeklinkers += 1
#         if aantal_medeklinkers == 3:
#             new_list.append(word)
        
#     return new_list

            
 
# def count_uppercase(word:str) -> int:
#     count = 0
#     uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for letter in word:
#         if letter in uppercases:
#             count += 1
#     return count

# def words_with_four_letters(words: list[str]) -> list[str]:
#     result = []
#     for word in words:
#         aantal_letters = 0
#         for letter in word:
#             aantal_letters +=1
#         if aantal_letters == 4:
#             result.append(word)
#     return result
# print(words_with_four_letters(["hallo", "boom", "auto" ]))

# def shortest_word(words: list[str]) -> str:
#     kortste = words[0]
#     for word in words:
#         if len(word) < len(kortste):
#             kortste = word
#         if len(word) < len(kortste):
#             kortste = word
#     return kortste

# def one_vowel_words(words: list[str]) -> list:
#     klinkers = "aeiou"
#     result = []
#     for word in words:
#         aantal_klinkers = 0 
#         for letter in word:
#             if letter in klinkers:
#                 aantal_klinkers +=1
#         if aantal_klinkers == 1:
#             result.append(word)
#     return result
        

            
       
# def tweede_letter(woord):
#     return woord[1]

# def laatste_letter(woord):
#     return woord[-1]
    
# def derde_getal(getallen):
#     return getallen[2]

# def print_getallen():
#     for i in range(5):
#         print(i)
        
# def som_tot_vijf(getal):
#     som = 0
#     for i in range(5):
#         som += i
#     return som
        

# def tel_letters(woord):
#     return len(woord)

# def alle_letters(woord):
#     lijst = []
#     for i in range(len(woord)):
#         lijst.append(woord[i])

# def posities(woord):
#     lijst = []
#     for i in range(len(woord)):
#         lijst.append(i)
#     return lijst
        
# def letters_met_index(woord):
#     for i in range(len(woord)):
#         print(i, woord[i])

# def klinkers(woord):
#     lijst = []
#     klinkers = "aeiou"
#     for letter in (woord):
#         if letter in klinkers: 
#             lijst.append(letter)
#     return lijst
        
# def posities_van_a(woord):
#     lijst = []
#     for i in range(len(woord)):
#         if woord[i] == "a":
#             lijst.append(i)
#     return lijst
# print(posities_van_a("halloa"))

# def posities_van_klinkers(woord):
#     lijst = []
#     klinkers = "aeiou"
#     for i in range(len(woord)):
#         if woord[i] in klinkers:
#             lijst.append(i)
#     return lijst


# def hoofdletters_posities(woorden):
#     lijst = []
    
#     for i in range(len(woorden)):
#         if woorden[i][0].isupper():
#             lijst.append(i)
#     return lijst
# print(hoofdletters_posities(["Hallo", "hoi", "Hha", "pp", "Poeo"]))
    

# def eerste_letter(woorden: list) -> list[str]:
#     lijst = []
#     for letter in woorden:
#         lijst.append(letter[0])
#     return lijst

# print(eerste_letter(["fiets", "auto", "trein"]))

# def posities_van_e(woord: str) -> list[str]:
#     lijst = []
#     for i in range(len(woord)):
#         if woord[i] == "e":
#             lijst.append(i)
#     return lijst
# print(posities_van_e("element"))

# def woorden_met_hoofdletter(woorden: list) -> list[str]:
#     lijst = []
#     for i in range(len(woorden)):
#         if woorden[i][0].isupper():
#             lijst.append(i)
#     return lijst
# print(woorden_met_hoofdletter(["Amsterdam", "fiets", "Utrecht", "boot"]))
    
    
# def alle_klinkers(woord):
#     lijst = []
#     klinkers = "aeiou"
#     for letter in woord:
#         if letter in klinkers:
#             lijst.append(letter)
#     return lijst
# print(alle_klinkers("programmeren"))

# def combineer(namen, leeftijden): 
#     lijst = []
#     for i in range(len(namen, leeftijden)):
#         lijst.append(namen[i] , leeftijden[i])
#     return lijst
# print(combineer(
# ["Jan", "Piet", "Klaas"],
# [20, 25, 18]
# ))
#1
def lange_woorden(woorden):
    lijst = []
    for i in range(len(woorden)):
        if len(woorden[i]) >= 5:
            lijst.append(i)
    return lijst
#2
def woorden_met_beginletter(woorden, letter):
    lijst = []
    for woord in woorden:
        if woord[0] == letter:
            lijst.append(woord)
    return lijst
#3
def dubbele_letters(woord): 
    lijst = []
    for letter in woord:
        for letter in range(len(woord)):
            if woord[letter] == woord[letter +1]:
                lijst.append(letter[i])
    return lijst

#4
def woorden_met_klinker(woorden):
    lijst = []
    klinkers = "aeiou"
    for woord in woorden:
        for letter in woord:
            if letter in klinkers and woord not in lijst:
                huidig = woord
                lijst.append(woord)
                
    return lijst
print(woorden_met_klinker(["rhythm", "fiets", "auto", "sky"]))

#5
def rapport(namen, cijfers):
    lijst = []
    for naam in namen:
        lijst.append(naam)
    for cijfer in cijfers:
        lijst.append(cijfer)
    return (naam)
           
        












            
            
        
    
            
        
            
            
                
            

        


            
            
            
            
    
                
            
                
        
                
        
            
            

            
        
        

        

            
    

    
    
