class ViewNotes(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(f'\nЗаметка: {note.note_id}\n'
                  f'Создания/редактирования(дата): {note.date}\n'
                  f'Заголовок: {note.title}\n'
                  f'Содержимое: {note.text}\n')

    @staticmethod
    def show_note(note):
        print(f'\nЗаметка: {note.note_id}\n' 
              f'Создания/редактирования(дата): {note.date}\n' 
              f'Заголовок: {note.title}\n' 
              f'Содержимое: {note.text}\n')
        # print(note)

    @staticmethod
    def show_empty_list_message():
        print('--> пусто!')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(f'--> {note_id} не найдена!')

    @staticmethod
    def display_note_id_exist(note_id):
        print(f'--> {note_id} уже есть!')

    @staticmethod
    def display_note_stored():
        print('--> заметка добавлена!')

    @staticmethod
    def display_note_updated(note_id):
        print(f'--> {note_id} обновлена!')

    @staticmethod
    def display_note_deletion(note_id):
        print(f'--> {note_id} удалена!')

    @staticmethod
    def display_all_notes_deletion():
        print('--> всё удалено!')

    def display_note_id_not_exist(search_id):
        return search_id
