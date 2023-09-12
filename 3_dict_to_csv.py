"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

# Так как я создавал список словарей в Excel, то решил что проще будет сделать csv
# которую потом можно убрать в словарь и использовать для выполнения второго задания
def main():
    with open('output.csv', "w", newline="", encoding="utf-8-sig") as outfile:
        writer = csv.DictWriter(outfile, ["name", "age", "job"])
        writer.writeheader()
        with open('users_table.csv', 'r', encoding='utf-8-sig') as inputfile:
            reader = csv.DictReader(inputfile, delimiter=';')
            for row in reader:
                # print(row)
                writer.writerow(row)

# Но по заданию, нужно было создать список словарей, поэтому словари я скопировал из консоли
# при выполнении предыдущего варианта (оставил закомментированный код), ну а список уже ручками
# Так что выполнение ДЗ после этого комментария

users_table = [
    {'name': 'Ivan', 'age': '19', 'job': 'storekeeper'},
    {'name': 'Maria', 'age': '23', 'job': 'accountant'},
    {'name': 'Petr', 'age': '43', 'job': 'big boss'},
    {'name': 'Afanasy', 'age': '22', 'job': 'driver'},
    {'name': 'Yana', 'age': '35', 'job': 'lawyer'},
    {'name': 'Kirill', 'age': '37', 'job': 'loader'}
    ]


def main2():
    with open('output2.csv', "w", newline="", encoding="utf-8-sig") as outfile:
        writer = csv.DictWriter(outfile, ["name", "age", "job"])
        writer.writeheader()
        for row in users_table:
            writer.writerow(row)


if __name__ == "__main__":
    main()
    main2()
