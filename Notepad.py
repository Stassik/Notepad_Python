import datetime
import random
import os
date = datetime.datetime.now().strftime("%Y-%m-%d / %H:%M:%S")


# Добавление заметки
def input_note():
    note_elem = ["заголовок", "текст"]
    new_note = list()
    notepad = dict()
    for i in range(len(note_elem)):
        new_note.insert(i, input(f"Введите {note_elem[i]}: "))
    new_note.insert(2, date)
    notepad[random.randint(1000, 10000)] = new_note 
    export_to_notepad(notepad)
    print("Заметка добавлена...")

def export_to_notepad(notepad):
    with open('notepad.csv', 'a+', encoding='utf-8') as data:
        for item in notepad:
            data.writelines('{};{}'.format(item, ';'.join(notepad[item])) +'\n')


def import_to_notepad():
    notepad = dict()        
    with open('notepad.csv', 'r', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes) == 0:
            print("Нет ни одной записи.\nСоздайте заметку.")
        for i in range(len(notes)):
            notepad[i] = notes[i]
    return notepad


def main_import_to_notepad():
    notepad = dict()        
    with open('notepad.csv', 'r', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes) == 0:
            print("Нет ни одной записи.\nСоздайте заметку.")
        for i in range(len(notes)):
            notepad[i] = notes[i]
        for item in notepad:
            print('{}: {}'.format(item+1, notepad[item]))


# Перезапись 
def replace_notepad(messege, new_notepad):
    with open('notepad.csv', 'w', encoding='utf-8') as data: 
        print(messege)   
        data.writelines(new_notepad)

# Изменение заметки
def edit_note():
    note_elem = ["заголовок", "текст"]
    main_import_to_notepad()
    with open('notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes)>0:
            id_note = int(input('\nВведите номер нужной записи: '))
            if id_note > len(notes): print("Такой заметки не существует.")
            else:
                note = notes[id_note-1].split(sep=";")
                print('\nЧто Вы хотите изменить?')
                user_choice = int(input('\n1 - Заголовок\n2 - Текст\n'))
                for i in range(len(note_elem)):
                    if i == (user_choice-1):    
                        note[user_choice] = input(f'Введите новый {note_elem[i]}: ')
                note[3] = date
                notes[id_note-1] = (';'.join(note)+'\n')
                replace_notepad('Сохранено...', notes)

# Удаление заметки
def delete_note():
    main_import_to_notepad()
    with open('notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes)>0:
            id_note = int(input('\nВведите номер нужной заметки: '))
            if id_note > len(notes): print("Такой заметки не существует.")
            else:
                del notes[id_note-1]
                replace_notepad('Удалено...', notes)

# Меню
def notepad_menu():
    user_choice = input('\n1 - показать все заметки\n2 - создать новую заметку\n3 - удалить заметку\n4 - изменить заметку\nДругой символ - закрыть программу\n')
    if user_choice == '1':
        if os.path.exists("notepad.csv"):
            main_import_to_notepad()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
        
    elif user_choice == '2':
        input_note()
        notepad_menu()
    elif user_choice == '3':
        if os.path.exists("notepad.csv"):
            delete_note()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
    elif user_choice == '4':
        if os.path.exists("notepad.csv"):
            edit_note()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
    else:
        exit



# Пользовательский интерфейс
def user_interface():
    header = 'Заметки'.center(50, '-')
    print(header)
    notepad_menu()
    

user_interface()