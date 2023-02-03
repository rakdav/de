import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

from AddEditWindow import Add_people
from Connect import Connect
from global_vars import con


class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.selected = None
        self.master.title("Лабораторная работа №3")
        self.master.resizable(False, False)
        self.master.geometry("1000x400")
        self.master.rowconfigure(index=0, weight=1)
        self.master.columnconfigure(index=0, weight=1)

        # self.con = Connect("python", "user14", "user14", "LisenseServer\\sqlexpress")
        self.people = con.get_staff_all()

        columns = ("T_Number", "Surname", "Lastname", "BirthDay",
                   "Phone", "Post", "Date_input", "Type_post")
        self.tree = ttk.Treeview(columns=columns, show="headings",
                                 displaycolumns=(1, 2, 3, 4, 5, 6, 7),
                                 selectmode="browse")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.heading("T_Number", text="Номер", anchor=W)
        self.tree.heading("Surname", text="Имя", anchor=W)
        self.tree.heading("Lastname", text="Фамилия", anchor=W)
        self.tree.heading("BirthDay", text="Дата рождения", anchor=W)
        self.tree.heading("Phone", text="Телефон", anchor=W)
        self.tree.heading("Post", text="Должность", anchor=W)
        self.tree.heading("Date_input", text="Дата трудоустройства", anchor=W)
        self.tree.heading("Type_post", text="Тип должности", anchor=W)

        self.tree.column("#0", stretch=YES, width=100)
        self.tree.column("#1", stretch=YES, width=100)
        self.tree.column("#2", stretch=YES, width=100)
        self.tree.column("#3", stretch=YES, width=60)
        self.tree.column("#4", stretch=YES, width=60)
        self.tree.column("#5", stretch=YES, width=60)
        self.tree.column("#6", stretch=YES, width=60)
        self.tree.column("#7", stretch=YES, width=30)

        for person in self.people:
            self.tree.insert("", END, values=list(person))

        scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        btn_add = ttk.Button(text="Добавить")
        btn_add.bind("<ButtonRelease>", self.add_people)
        btn_add.grid(row=1, column=0)
        self.tree.bind("<<TreeviewSelect>>", self.item_selected)

        self.popup = Menu(self, tearoff=0)
        self.popup.add_command(label="Delete", command=self.selection_delete)
        self.popup.add_command(label="Update", command=self.selection_update)
        self.tree.bind("<Button-3>", self.do_popup)

    def add_people(self, evt):
        res = Add_people(master=tkinter.Toplevel(), parent=self)
        self.update_table(res)

    def item_selected(self, event):
        selected_people = ""
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            self.selected = item["values"]

    def selection_delete(self):
        con.delete_staff(self.popup.selection["T_Number"])
        self.tree.delete(self.tree.selection())

    def selection_update(self):
        res=Add_people(master=tkinter.Toplevel(), parent=self, staff=self.popup.selection)
        self.update_table(res)

    def update_table(self, res):
        if res.open() == "OK":
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.people = con.get_staff_all()
            for person in self.people:
                self.tree.insert("", END, values=list(person))
            self.update()

    def do_popup(self, event):
        # display the popup menu
        try:
            self.popup.selection = self.tree.set(self.tree.identify_row(event.y))
            self.popup.post(event.x_root, event.y_root)
        finally:
            # make sure to release the grab (Tk 8.0a1 only)
            self.popup.grab_release()


root = tkinter.Tk()
app = Application(master=root)
root.mainloop()
