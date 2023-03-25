import datetime
date = datetime.datetime.today().strftime("%Y-%m-%d / %H:%M:%S")


# Добавление заметки
def input_note():
    note_elem = ["заголовок", "текст"]
    new_note = list()
    for i in range(len(note_elem)):
        new_note.insert(i, input(f"Введите {note_elem[i]}: "))
    new_note.insert(2, date)
    export_to_notepad(new_note)

def export_to_notepad(new_note):
    with open('notepad.csv', 'a+', encoding='utf-8') as data:
        data.writelines(';'.join(new_note)+'\n')


def import_to_notepad():
    notepad = dict()
    with open('notepad.csv', 'r', encoding='utf-8') as data:
        notes = data.readlines()
        for i in range(len(notes)):
            notepad[i] = notes[i]
    return notepad


def main_import_to_notepad():
    notepad = import_to_notepad()
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
        id_note = int(input('\nВведите номер нужной записи: '))
        note = notes[id_note-1].split(sep=";")
        print('\nЧто Вы хотите изменить?')
        user_choice = int(input('\n1 - Заголовок\n2 - Текст'))
        for i in range(len(note_elem)):
            if i == (user_choice-1):    
                note[i] = input(f'Введите новый {note_elem[i]}: ')
        note[2] = date
        notes[id_note-1] = (';'.join(note)+'\n')
    replace_notepad('Сохранено...', notes)

# Удаление заметки
def delete_note():
    main_import_to_notepad()
    with open('notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        id_note = int(input('\nВведите номер нужной заметки: '))
        del notes[id_note-1]
    replace_notepad('Удалено...', notes)

# Меню
def notepad_menu():
    user_choice = input('\n1 - показать все заметки\n2 - создать новую заметку\n3 - удалить заметку\n4 - изменить заметку\n0 - закрыть программу\n')
    if user_choice == '1':
        main_import_to_notepad()
        notepad_menu()
    elif user_choice == '2':
        input_note()
        notepad_menu()
    elif user_choice == '3':
        delete_note()
        notepad_menu()
    elif user_choice == '4':
        edit_note()
        notepad_menu()
    elif user_choice == '0':
        exit



# Пользовательский интерфейс
def user_interface():
    header = 'Заметки'.center(50, '-')
    print(header)
    notepad_menu()
    

user_interface()