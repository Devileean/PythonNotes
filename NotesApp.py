from controllerNotes import ControllerNotes
from modelNotes_json import NotesModelJSON
from viewNotes import ViewNotes
from note import Note

import datetime

# запускает controller и передаёт в него модель в которую передается название файла для чтения заметок - note.json
# затем передает представления из файла viewNotes
def run():
    c = ControllerNotes(NotesModelJSON("note.json"), ViewNotes())
# запуск меню
    while True:
        user_input = input(
                        '1 --------- Добавить новую заметку\n'
                        '2 --------- Показать заметку\n'
                        '3 --------- Показать все заметки\n'
                        '4 --------- Редактировать заметку\n'
                        '5 --------- Удалить заметку\n'
                        '6 --------- Удалить все заметки\n'
                        '7 --------- Выход\n'
                        'Выберите действие: ')

        if user_input == '1':
            print(' Создание заметки.')
            c.create_note(set_note())

        elif user_input == '2':
            print(' Показать заметку.')
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif user_input == '3':
            if c.notes_exist():
                print(' Показать все заметки.')
                c.show_notes()

        elif user_input == '4':
            if c.notes_exist():
                print(' Редактировать заметку.')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, set_note())

        elif user_input == '5':
            if c.notes_exist():
                print(' Вы удаляете заметку!')
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif user_input == '6':
            if c.notes_exist():
                print(' Удалить все заметки!')
                if input('Уверены!!! (Y/N): ').capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif user_input == '7':
            break

        else:
            print('\tНеверный ввод!')

def set_note():
    """
    Создание новой заметки
    :return: object Note
    """
    note_id = 0
    date = datetime.datetime.now()
    title = input('  Дайте имя заметке: ')
    text = input('  Заполните заметку: ')
    return Note(note_id, date, title, text)

def get_number():
    """
    Возвращение числа id заметки
    :return: int||string
    """
    while True:
        get_choice = input('  Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('  неверное id заметки!')
