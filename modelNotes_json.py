import json

from viewNotes import ViewNotes
from note import Note


class NotesModelJSON(object):

    def __init__(self, filename):
        """
        Получаем название файла
        :param filename: string
        """
        self.filename = filename
        self.notes = list()

    def create_note(self, note):
        """
        Создаем заметку
        :param note: object note
        :return: записывает в файл
        """
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.note_id > max_id:
                max_id = item.note_id
        note_id = max_id + 1
        note.note_id = note_id

        self.notes.append(note)
        self.write_json(self.notes)

    def read_note(self, search_id):
        """
        Возвращает заметку по id.
        :param search_id: int id
        :return: object note
        """
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
        else:
            ViewNotes.display_note_id_not_exist(search_id)

    def read_notes(self):
        """
        Посмотреть все заметки.
        :return: note
        """
        return self.read_json()

    def update_note(self, search_id, note):
        """
        Редактирование заметки по id.
        :param search_id: int
        :param note: object
        :return: запись в файл
        """
        self.notes = self.read_notes()
        for item in self.notes:
            if item.note_id == search_id:
                item.date = note.date
                item.title = note.title
                item.text = note.text

        self.write_json(self.notes)

    def delete_note(self, search_id):
        """
        Удаление заметок.
        :param search_id: int
        :return: запись в файл
        """
        self.notes = self.read_notes()

        for index, note in enumerate(self.notes):
            if note.note_id == search_id:
                del self.notes[index]

        self.write_json(self.notes)

    def delete_all_notes(self):
        """
        Удаление всех заметок.
        :return: запись в файл
        """
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json(self.notes)

    def write_json(self, notes):
        """
        Запись данных в файл note.json
        :param notes: object
        :return: запись в файл
        """
        json_strings_list = list()
        for note in notes:
            json_strings_list.append({'id': note.note_id, 'date': note.date, 'title': note.title, 'text': note.text})

        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        """
        Чтение файла
        :return: object
        """
        notes_list = list()
        try:
            with open(self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))

            return notes_list
        except ValueError:
            return self.notes