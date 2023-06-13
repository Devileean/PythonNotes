class ControllerNotes(object):

    def __init__(self, model, view):
        """
        Получаем модель и вид.
        :param model: object
        :param view: object
        """
        self.model = model
        self.view = view

    def show_notes(self):
        """
        Показываем заметки
        :return: вывод заметок
        """
        notes = self.model.read_notes()
        self.view.show_number_point_list(notes)

    def show_note(self, note_id):
        """
        Показываем заметку по id
        :param note_id:
        :return: view заметки

        """
        try:
            note = self.model.read_note(note_id)
            self.view.show_note(note)
        except ValueError:
            self.view.display_note_id_not_exist(note_id)

    def create_note(self, note):
        """
        Создание заметки
        :param note: object note
        :return: сохранение заметки и вывод отчёта
        """
        self.model.create_note(note)
        self.view.display_note_stored()

    def update_note(self, note_id, note):
        """
        Обновление заметки по id
        :param note_id: string id заметки
        :param note: object заметка
        :return: обновление заметки и вывод отчёта
        """
        self.model.update_note(note_id, note)
        self.view.display_note_updated(note_id)

    def delete_note(self, note_id):
        """
        Удаление заметки по id
        :param note_id: string id заметки
        :return: string id отчёт о удалении заметки
        """
        try:
            self.model.delete_note(note_id)
            self.view.display_note_deletion(note_id)
        except ValueError:
            self.view.display_note_id_not_exist(note_id)

    def delete_all_notes(self):
        """
        Удаление всех заметок
        :return: вывод отчёта о удалении
        """
        self.model.delete_all_notes()
        self.view.display_all_notes_deletion()

    def notes_exist(self):
        """
        Проверка на существование заметок
        :return: boolean true false
        """
        notes = self.model.read_notes()
        if len(notes) == 0:
            self.view.show_empty_list_message()
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        """
        Проверка на существование заметки по id
        :param search_id: string id
        :return: true or false
        """
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            self.view.display_note_id_not_exist(search_id)
            return False