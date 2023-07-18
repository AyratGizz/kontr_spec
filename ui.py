import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите - Название заметки: '), number)
    body = check_len_text_input(
        input('Введите - Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nПеред вами контрольная работа по блоку специализация - Программа 'Заметки'. \n"
          "Описание функций программы:\n"
          "1 - Вывод всех заметок из файла;\n"
          "2 - Добавление заметки;\n"
          "3 - Удаление заметки;\n"
          "4 - Редактирование заметки;\n"
          "5 - Выборка заметок по дате;\n"
          "6 - Показать заметку по id;\n"
          "7 - Выход из программы;\n\n"
          "Введите номер нужной функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть не менее {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbuy():
    print("Спасибо за использование программы созданной Гиззатуллиным Айратом Искандаровичем")
