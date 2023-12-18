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

def read_notes():
    filter_date = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    if not notes:
        print("Заметок нет")
        return
    if not filter_date:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
    else:
        filtered_notes = [note for note in notes if note["date"].startswith(filter_date)]
        if filtered_notes:
            for note in filtered_notes:
                print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
        else:
            print("Заметок с указанной датой нет")