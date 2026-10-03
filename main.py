users = {
    "Олег": "підліток",
    "Марія": "дорослий",
    "Андрюха": "дитина",
    "Анна": "підліток"
}

try:
    name = input("Enter name: ")
    print("Вікова група:", users[name])
except KeyError:
    print("Користувача не найдено")
finally:
    print("Програма завершена")