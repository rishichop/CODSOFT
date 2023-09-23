import tkinter as tk
from save import ReadWriteVar
from tasklist import TaskList


class GUI:

    def __init__(self):
        self.dates = []
        self.selected_date = ""
        self.task_list_dict = {}

        self.main_window = tk.Tk()
        self.main_window.title("TO-DO Lists!!")
        self.main_window.geometry("525x525")
        self.main_window.config(padx=20, pady=20, background="black")

        self.to_do_list_label = tk.Label(master=self.main_window,
                                         text="Select a To-Do List",
                                         background="black",
                                         foreground="white",
                                         width=30,
                                         height=1,
                                         anchor="w")

        self.to_do_list_label.grid(row=0, column=0, columnspan=2, sticky="W")

        self.task_listbox = tk.Listbox(height=10, width=35)
        self.task_listbox.grid(row=1, column=0, sticky="W", rowspan=2)

        self.tasks_overview = tk.Listbox(master=self.main_window, height=18, width=40)
        self.tasks_overview.grid(row=3, column=0, sticky="news", columnspan=3, pady=(20, 0))

        self.update_listbox()

        self.new_button = tk.Button(master=self.main_window,
                                    text="Create New",
                                    command=self.new_button_clicked,
                                    width=15,
                                    height=3,
                                    font=("Arial", 9, "bold"))

        self.new_button.grid(row=1, column=1, padx=(20, 0))

        self.delete_button = tk.Button(master=self.main_window,
                                       text="Delete Selected",
                                       command=self.delete_button_clicked,
                                       width=15,
                                       height=3,
                                       font=("Arial", 9, "bold"))

        self.delete_button.grid(row=1, column=2, padx=(20, 0))

        self.edit_button = tk.Button(master=self.main_window,
                                     text="Edit Selected",
                                     command=self.edit_button_clicked,
                                     width=15,
                                     height=3,
                                     font=("Arial", 9, "bold"))

        self.edit_button.grid(row=2, column=1, padx=(20, 0))

        self.exit_button = tk.Button(master=self.main_window,
                                     text="Exit",
                                     command=self.exit_button_clicked,
                                     width=15,
                                     height=3,
                                     font=("Arial", 9, "bold"))

        self.exit_button.grid(row=2, column=2, padx=(20, 0))

        self.main_window.after(500, func=self.update_listbox())

        self.main_window.mainloop()

    def update_listbox(self):
        self.read_file()
        self.task_listbox.delete(0, "end")
        # print(self.dates)
        for date in self.dates:
            self.task_listbox.insert(self.dates.index(date), date)

        self.task_listbox.bind("<<ListboxSelect>>", self.listbox_used)

    def update_overview(self):
        self.tasks_overview.delete(0, "end")
        if self.selected_date not in [None, ""]:
            for task in self.task_list_dict[self.selected_date]:
                self.tasks_overview.insert(self.task_list_dict[self.selected_date].index(task), task)

        self.tasks_overview.bind("<<ListboxSelect>>")

    def listbox_used(self, selection):
        print(selection)
        if self.task_listbox.curselection():
            self.selected_date = self.task_listbox.get(self.task_listbox.curselection())
        self.update_overview()

    def new_button_clicked(self):
        self.main_window.destroy()
        TaskList()

    def delete_button_clicked(self):
        self.task_list_dict.pop(self.selected_date)
        ReadWriteVar.write(self.selected_date, "d")
        self.selected_date = None
        self.update_listbox()

    def edit_button_clicked(self):
        self.main_window.destroy()
        TaskList(self.task_list_dict[self.selected_date], self.selected_date)

    def exit_button_clicked(self):
        self.main_window.destroy()

    def read_file(self):
        self.dates = []
        self.task_list_dict = ReadWriteVar.read()

        if not self.task_list_dict:
            self.task_list_dict = {}

        for date in self.task_list_dict:
            self.dates.append(date)


main_window = GUI()
