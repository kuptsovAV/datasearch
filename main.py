from tkinter import *
from tkinter import ttk
from request import search_contacts_by_surname, search_contacts_by_phone, search_contacts_by_passport

def clear_entry():
    entry.delete(0, END)
    for item in treeview.get_children():
        treeview.delete(item)

def search_contacts():
    search_type = search_type_var.get()
    search_text = entry_var.get()
    clear_entry()

    if search_type == "По фамилии":
        results = search_contacts_by_surname(search_text)
    elif search_type == "По телефону":
        results = search_contacts_by_phone(search_text)
    elif search_type == "По паспорту":
        results = search_contacts_by_passport(search_text)

    for contact in results:
        contact_values = [
            getattr(contact, 'fullname', ''),
            getattr(contact, 'inn', ''),
            getattr(contact, 'birthdate', ''),
            getattr(contact, 'phonenum', ''),
            getattr(contact, 'passp', ''),
            getattr(contact, 'snils', ''),
            getattr(contact, 'city', '')
        ]
        treeview.insert('', 'end', values=contact_values)


root = Tk()
root.title("СПД(Система поиска данных)")
root.geometry("1600x400")


# Создаем стили 
light_style = ttk.Style()
light_style.theme_use("clam")  


# Метка и поле для ввода запроса
label = Label(root, text="Запрос:")
label.grid(row=0, column=0, padx=6, pady=6, sticky='e')

entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, width=100)  
entry.grid(row=0, column=1, padx=6, pady=6, sticky='w')  

# Выбор типа поиска
search_type_var = StringVar()
search_type_var.set("По фамилии")
search_type_label = Label(root, text="Тип поиска:")
search_type_label.grid(row=0, column=2, padx=6, pady=6)

search_type_menu = OptionMenu(root, search_type_var, "По фамилии", "По телефону", "По паспорту")
search_type_menu.grid(row=0, column=3, padx=6, pady=6)

# Кнопка поиска и очистки
btn_search = Button(root, text="Поиск", command=search_contacts)
btn_search.grid(row=0, column=4, padx=6, pady=6)

btn_clear = Button(root, text="Очистить", command=clear_entry)
btn_clear.grid(row=0, column=5, padx=6, pady=6)

# Создаем Treeview
treeview = ttk.Treeview(root, columns=('Фамилия', 'ИНН', 'Дата рождения', 'Телефон', 'Паспорт', 'СНИЛС', 'Город'), show='headings')
treeview.grid(row=1, column=0, columnspan=6, padx=6, pady=6, sticky='nsew')

# Добавляем возможность изменения размеров окна
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Заголовки столбцов
treeview.heading('Фамилия', text='Фамилия')
treeview.heading('ИНН', text='ИНН')
treeview.heading('Дата рождения', text='Дата рождения')
treeview.heading('Телефон', text='Телефон')
treeview.heading('Паспорт', text='Паспорт')
treeview.heading('СНИЛС', text='СНИЛС')
treeview.heading('Город', text='Город')


root.mainloop()
