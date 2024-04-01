# Импорт библиотек

import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from request import Base, User

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Админская панель")
        self.root.geometry("600x400")
        
        self.create_database_connection()
        self.create_logs_table()
        
        self.create_widgets()
    
    def create_database_connection(self):
        self.engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-RCOTVQJ;DATABASE=contacts;UID=cont;PWD=contact")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def create_logs_table(self):
        # код создания таблицы логов
    
        def create_widgets(self):
        # код создания виджетов
        
        # Кнопка для создания пользователя
            self.create_user_button = tk.Button(self.root, text="Создать пользователя", command=self.create_user_window)
        self.create_user_button.pack(pady=10)
    
    def create_user_window(self):
        self.user_window = tk.Toplevel(self.root)
        self.user_window.title("Создать пользователя")
        self.user_window.geometry("300x200")
        
        self.create_user_widgets()
    
    def create_user_widgets(self):
        self.user_fio_label = tk.Label(self.user_window, text="ФИО:")
        self.user_fio_label.pack()
        self.user_fio_entry = tk.Entry(self.user_window)
        self.user_fio_entry.pack()
        
        self.user_access_rights_label = tk.Label(self.user_window, text="Права доступа (admin/user):")
        self.user_access_rights_label.pack()
        self.user_access_rights_entry = tk.Entry(self.user_window)
        self.user_access_rights_entry.pack()
        
        self.create_user_confirm_button = tk.Button(self.user_window, text="Создать", command=self.add_user)
        self.create_user_confirm_button.pack(pady=10)
    
    def add_user(self):
        fio = self.user_fio_entry.get()
        access_rights = self.user_access_rights_entry.get()
        
        if fio and access_rights in ("admin", "user"):
            new_user = User(fio=fio, access_rights=access_rights)
            self.session.add(new_user)
            self.session.commit()
            tk.messagebox.showinfo("Успех", "Пользователь успешно создан!")
            self.user_window.destroy()
        else:
            tk.messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля корректно.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
