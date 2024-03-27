i = 0
numbers = []

while i < 6:
    print(f"В начале значение i равно {i}")
    numbers.append(i)
    
    i += 1
    print("Текущие значения: ", numbers)
    print(f"В конце значение i равно {i}")

print("Значения: ")

for i in numbers:
    print(i)


################################################################

# def first_while():
#     i = 0
#     numbers = []
    
#     while i < 6:
#         print(f"В начале значение i равно {i}")
#         numbers.append(i)
    
#         i += 1
#         print("Текущие значения: ", numbers)
#         print(f"В конце значение i равно {i}")
#     return numbers

# def create_list():
#     i = 0
#     numbers = []
    
#     for i in range(6):
#         print(f"В начале значение i равно {i}")
#         numbers.append(i)
    
#         i += 1
#         print("Текущие значения: ", numbers)
#         print(f"В конце значение i равно {i}")
#     return numbers


# def cou(numbers):
#     print("Значения: ")

#     for num in numbers:
#         print(num)

# numbers_list = create_list()
# cou(numbers_list)
