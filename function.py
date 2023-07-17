import file_operation
import Note
import ui

length = 5  # минимальное количество символов


def add():
    note = ui.create_note(length)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Ваша заметка добавлена!')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите Дату в формате дд.мм.гггг: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic:
        print('Заметок нет...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(length)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена!')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена!')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic:
        print('Заметки с таким id не найдено, введите другой id!')
    file_operation.write_file(array, 'a')
