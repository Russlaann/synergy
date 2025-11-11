# Задание 1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Введите число: "))
fact_num = factorial(num)
result_list = []

for i in range(fact_num, 0, -1):
    result_list.append(factorial(i))

print(result_list)

# Задание 2

import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец добавлен с ID: {new_id}")


def read():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)
    if not pet_info:
        print("Питомец с таким ID не найден")
        return

    for pet_name, info in pet_info.items():
        pet_type = info["Вид питомца"]
        pet_age = info["Возраст питомца"]
        owner_name = info["Имя владельца"]
        age_word = get_suffix(pet_age)

        print(
            f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')


def update():
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet_info = get_pet(pet_id)
    if not pet_info:
        print("Питомец с таким ID не найден")
        return

    for pet_name in pet_info.keys():
        print("Введите новые данные (оставьте пустым чтобы не менять):")

        new_type = input(f"Вид питомца [{pet_info[pet_name]['Вид питомца']}]: ")
        new_age = input(f"Возраст питомца [{pet_info[pet_name]['Возраст питомца']}]: ")
        new_owner = input(f"Имя владельца [{pet_info[pet_name]['Имя владельца']}]: ")

        if new_type:
            pet_info[pet_name]["Вид питомца"] = new_type
        if new_age:
            pet_info[pet_name]["Возраст питомца"] = int(new_age)
        if new_owner:
            pet_info[pet_name]["Имя владельца"] = new_owner

    print("Данные обновлены")


def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    if pet_id in pets:
        del pets[pet_id]
        print("Питомец удален")
    else:
        print("Питомец с таким ID не найден")


def pets_list():
    if not pets:
        print("База данных пуста")
        return

    for pet_id, pet_info in pets.items():
        for pet_name, info in pet_info.items():
            pet_type = info["Вид питомца"]
            pet_age = info["Возраст питомца"]
            owner_name = info["Имя владельца"]
            age_word = get_suffix(pet_age)

            print(
                f'ID: {pet_id}. Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')


command = ""
while command != "stop":
    print("\nДоступные команды: create, read, update, delete, list, stop")
    command = input("Введите команду: ").lower()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Работа завершена")
    else:
        print("Неизвестная команда")