# Автор Беляев Александр
# Модуль для логирования контактов
# Данный модуль записывает данные в файлыPhonebook.csv иPhonebook.txt поля как в модуле Дмитрия data_in.
from data_in import input_data as id

info = id()


def writing_scv():
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{info[5]};{info[6]};\n')


def writing_txt():
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия:{info[0]}\n\n Имя:{info[1]}\n\n Jnxtcndj:{info[2]}\n\n Дата рождения:{info[3]}\n\nНомер телефона: {info[4]}\n\n Адрес: {info[5]}\n\nПримичание: {info[6]}\n\n\n')
