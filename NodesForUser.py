import json
import datetime

def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note_id = len(notes) + 1
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "msg": msg, "date": date})
    save_notes()
    print("Заметка успешно сохранена")