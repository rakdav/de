import tkinter
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime

from global_vars import con


class Add_people(tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None, staff=None):
        super().__init__(master)
        self.staff = staff
        self.parent = parent
        if staff is not None:
            self.T_Number=staff["T_Number"]
        self.pack(fill="both", padx=4, pady=4)

        label = tkinter.ttk.Label(self, text="Введите имя")
        label.pack(fill="x", padx=4)
        self.entry_name = tkinter.ttk.Entry(self)
        self.entry_name.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите фамилию")
        label.pack(fill="x", padx=4)
        self.entry_surname = tkinter.ttk.Entry(self)
        self.entry_surname.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите дату рождения")
        label.pack(fill="x", padx=4)
        self.today = datetime.today().year
        self.birth_day = DateEntry(self, width=12, background='darkblue',
                                   foreground='white', borderwidth=2, year=self.today)
        self.birth_day.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите телефон")
        label.pack(fill="x", padx=4)
        self.entry_phone = tkinter.ttk.Entry(self)
        self.entry_phone.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите должность")
        label.pack(fill="x", padx=4)
        self.entry_post = tkinter.ttk.Entry(self)
        self.entry_post.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите дату поступления")
        label.pack(fill="x", padx=4)
        self.date_input = DateEntry(self, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, year=self.today)
        self.date_input.pack(fill="x", padx=4)

        label = tkinter.ttk.Label(self, text="Введите тип должности")
        label.pack(fill="x", padx=4)
        self.entry_type = tkinter.ttk.Entry(self)
        self.entry_type.pack(fill="x", padx=4)

        btn_ok = tkinter.ttk.Button(self, text="Ok", command=self.add_to_database)
        btn_ok.pack(side=tkinter.LEFT, pady=10, padx=30)

        btn_cancel = tkinter.ttk.Button(self, text="Cancel", command=self.master.destroy)
        btn_cancel.pack(side=tkinter.RIGHT, pady=10, padx=30)

        if staff is not None:
            print(staff["Surname"])
            self.entry_name.insert(0, staff["Surname"])
            self.entry_surname.insert(0, staff["Lastname"])
            date = datetime.strptime(staff["BirthDay"], "%Y-%m-%d")
            self.birth_day.set_date(date)
            self.entry_phone.insert(0, staff["Phone"])
            self.entry_post.insert(0, staff["Post"])
            date = datetime.strptime(staff["Date_input"], "%Y-%m-%d")
            self.date_input.set_date(date)
            self.entry_type.insert(0, staff["Type_post"])
            self.master.title("Изменение записи")
        else:
            self.master.title("Добавление записи")
        self.master.resizable(False, False)
        self.master.geometry("300x340")
        self.master.transient(parent)
        self.grab_set()

    def add_to_database(self):
        slave = dict()
        slave["Surname"] = self.entry_name.get()
        slave["Lastname"] = self.entry_surname.get()
        day = self.birth_day.get().split("/")
        slave["BirthDay"] = datetime(self.today, int(day[0]), int(day[1]))
        slave["Phone"] = self.entry_phone.get()
        slave["Post"] = self.entry_post.get()
        day = self.date_input.get().split("/")
        slave["Date_input"] = datetime(self.today, int(day[0]), int(day[1]))
        slave["Type_post"] = self.entry_type.get()
        if self.staff is not None:
            slave["T_Number"] = self.T_Number
            con.update_staff(slave)
        else:
            con.insert_staff(slave)
        self.master.destroy()

    def open(self):
        self.grab_set()
        self.wait_window()
        return "OK"
