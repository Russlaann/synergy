# Задание 1

pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

for pet_name, pet_info in pets.items():
    pet_type = pet_info['Вид питомца']
    pet_age = pet_info['Возраст питомца']
    owner_name = pet_info['Имя владельца']

    if pet_age % 10 == 1 and pet_age % 100 != 11:
        age_word = "год"
    elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
        age_word = "года"
    else:
        age_word = "лет"

    print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')

# Задание 2

my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i ** i

print(my_dict)