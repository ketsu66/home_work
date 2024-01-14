#1
# def anagrams(word1, word2):
#     word1 = word1.lower().replace(" ", "")
#     word2 = word2.lower().replace(" ", "")
#
#
#     if len(word1) != len(word2):
#         return False
#
#
#     letter_count = {}
#
#
#     for letter in word1:
#         if letter in letter_count:
#             letter_count[letter] += 1
#         else:
#             letter_count[letter] = 1
#
#
#     for letter in word2:
#         if letter in letter_count:
#             letter_count[letter] -= 1
#         else:
#             return False
#
#     for count in letter_count.values():
#         if count != 0:
#             return False
#
#     return True
#
# word1 = "binary"
# word2 = "brainy"
# print(f"Are '{word1}' and '{word2}' anagrams? {anagrams(word1, word2)}")
#
# word3 = "роздвоєння"
# word4 = "дозрівання"
# print(f"Are '{word3}' and '{word4}' anagrams? {anagrams(word3, word4)}")
#2
# def taxiFare(km, min_price=2.0, price_per_km=0.3):
#     if km <= 3:
#         total_fare = min_price
#     else:
#         additional_km = km - 3
#         total_fare = min_price + (additional_km * price_per_km)
#
#     return total_fare
#
#
# distance = 17.5
# fare = taxiFare(km=distance)
#
#
# print(f"Вартість поїздки на таксі за {distance} км становить {fare} у.о.")
#3

import random

# def generate_random_password():
#     password_length = random.randint(8, 15)
#     all_characters = list(map(str, list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))))
#     password = ''.join(random.choice(all_characters) for _ in range(password_length))
#     return password
#
# for _ in range(3):
#     password = generate_random_password()
#     print(f"Випадковий пароль: {password}")
#4
# def find_gcd(*numbers):
#     def gcd(x, y):
#         while y:
#             x, y = y, x % y
#         return x
#
#
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = gcd(result, num)
#
#     return result
#
#
# numbers_to_find_gcd = (165, 435, 300)
# result_gcd = find_gcd(*numbers_to_find_gcd)
# print(f"Найбільший спільний дільник чисел {numbers_to_find_gcd} є: {result_gcd}")
#5
# numbers = [30, 45, 60, 75, 90, 105, 120]
# result = list(filter(lambda x: x % 15 == 0, numbers))
# print("Числа, поділені на 15:", result)

