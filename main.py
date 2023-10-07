from csv import DictReader, DictWriter
from os.path import exists


def create_file():
    with open("phone.csv", "w", encoding="UTF-8") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res


def write_file(file_name, lst):
    with open(file_name, mode='a', encoding='utf-8', newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        # Обработка входных данных перед записью
        surname, name, number = lst
        surname = surname.strip()  # Убираем лишние пробелы
        name = name.strip()
        number = number.strip()

        # Проверка наличия данных перед записью
        if surname and name and number:
            f_writer.writerow({"Фамилия": surname, "Имя": name, "Номер": number})
            print("Данные успешно добавлены.")
        else:
            print("Неверный ввод. Попробуйте снова.")


def update_data(file_name, old_name, new_data):
    data = read_file(file_name)
    for entry in data:
        if entry['Имя'] == old_name or entry['Фамилия'] == old_name:
            entry.update(new_data)
    with open(file_name, mode='w', encoding='utf-8', newline="") as data_file:
        f_writer = DictWriter(data_file, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(data)


def delete_data(file_name, name):
    data = read_file(file_name)
    updated_data = [entry for entry in data if entry['Имя'] != name and entry['Фамилия'] != name]
    with open(file_name, mode='w', encoding='utf-8', newline="") as data_file:
        f_writer = DictWriter(data_file, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(updated_data)


def main():
    while True:
        command = input('Введите команду (r - чтение, w - запись, u - обновление, d - удаление, q - выход): ')
        if command == "q":
            break
        elif command == "r":
            if not exists('phone.csv'):
                print("Телефонный справочник пуст.")
            else:
                print(read_file("phone.csv"))
        elif command == "w":
            if not exists("phone.csv"):
                create_file()
            data = get_info()
            write_file("phone.csv", data)
        elif command == "u":
            name_to_update = input('Введите имя или фамилию для обновления: ')
            new_name = input('Введите новое имя: ')
            new_surname = input('Введите новую фамилию: ')
            new_number = input('Введите новый номер: ')
            if new_name and new_surname and new_number:
                new_data = {"Фамилия": new_surname, "Имя": new_name, "Номер": new_number}
                update_data("phone.csv", name_to_update, new_data)
                print("Данные обновлены.")
            else:
                print("Неверный ввод. Попробуйте снова.")
        elif command == "d":
            name_to_delete = input('Введите имя или фамилию для удаления: ')
            delete_data("phone.csv", name_to_delete)
            print("Данные удалены.")
        else:
            print("Неверная команда. Попробуйте снова.")


def get_info():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    return surname, name, number


main()