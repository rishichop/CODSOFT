import tkinter as tk
from save import ReadWriteVar


class TaskList:

    def __init__(self, task_list=None, date=None):
        if date is None:
            date = ""
        self.date = date
        if task_list is None:
            task_list = []
        self.task_list = task_list
        self.new_task_date = ""
        self.selected_task = ""
        self.selected_task_index = None

        print(self.task_list)

        self.new_task_window = tk.Tk()
        self.new_task_window.title("TO-DO Config!!")
        self.new_task_window.geometry("480x550")
        self.new_task_window.config(background="black", padx=20, pady=20)

        self.enter_name = tk.Label(master=self.new_task_window,
                                   text="Enter name:",
                                   background="black",
                                   foreground="white",
                                   width=30,
                                   height=1,
                                   anchor="w")

        self.enter_name.grid(row=0, column=0, columnspan=2, sticky="W")

        self.date_entry = tk.Entry(master=self.new_task_window, width=50)
        self.date_entry.insert(0, self.date)
        self.date_entry.focus()
        self.date_entry.grid(row=1, column=0, sticky="W")

        self.save_button = tk.Button(master=self.new_task_window,
                                     text="Save",
                                     command=self.save_button_clicked,
                                     width=15,
                                     height=3)

        self.save_button.grid(row=1, column=1, sticky="W", padx=(20, 0))

        self.to_do_task_label = tk.Label(master=self.new_task_window,
                                         text="Enter task",
                                         background="black",
                                         foreground="white",
                                         width=30,
                                         height=1,
                                         anchor="w")

        self.to_do_task_label.grid(row=2, column=0, columnspan=2, sticky="W")

        self.task_textbox = tk.Text(master=self.new_task_window, width=55, height=2)
        self.task_textbox.grid(row=3, column=0, columnspan=2, sticky="W", pady=(20, 0))

        self.button_frame = tk.Frame(master=self.new_task_window, background="black")
        self.button_frame.grid(row=4, column=0, columnspan=2)

        self.add_button = tk.Button(master=self.button_frame,
                                    text="Add",
                                    command=self.add_button_clicked,
                                    width=15,
                                    height=3)

        self.add_button.grid(row=-0, column=0, sticky="W", pady=(20, 0))

        self.done_button = tk.Button(master=self.button_frame,
                                     text="✔",
                                     command=self.tick_button_clicked,
                                     width=5,
                                     height=3,
                                     state="disabled")

        self.done_button.grid(row=0, column=1, sticky="W", pady=(20, 0), padx=(20, 0))

        self.edit_button = tk.Button(master=self.button_frame,
                                     text="Edit",
                                     command=self.edit_button_clicked,
                                     width=15,
                                     height=3,
                                     state="disabled")

        self.edit_button.grid(row=0, column=2, sticky="E", pady=(20, 0), padx=(20, 0))

        self.delete_button = tk.Button(master=self.button_frame,
                                       text="Delete",
                                       command=self.delete_button_clicked,
                                       width=15,
                                       height=3,
                                       state="disabled")

        self.delete_button.grid(row=0, column=3, pady=(20, 0), padx=(20, 0), sticky="E")

        self.task_listbox = tk.Listbox(master=self.new_task_window, height=15, width=73)
        self.task_listbox.grid(row=5, column=0, columnspan=2, sticky="W", pady=(20, 0))
        self.update_listbox()

        self.new_task_window.mainloop()

    def tick_button_clicked(self):
        temp = self.selected_task
        self.edit_button_clicked()
        self.task_textbox.delete("1.0", "end")
        temp = temp.rstrip("\n")
        self.task_textbox.insert("1.0", temp + "  ✔\n")
        self.add_button_clicked()

    def save_button_clicked(self):
        if self.date == self.date_entry.get():
            pass
        elif self.date in ReadWriteVar.tasks:
            ReadWriteVar.write(self.date, "d")
        ReadWriteVar.write({self.date_entry.get(): self.task_list}, "u")
        self.new_task_window.destroy()

    def add_button_clicked(self):
        task = self.task_textbox.get(index1="1.0", index2="end")
        task = task.rstrip("\n") + "\n"
        if task not in self.task_list:
            if self.selected_task_index is None:
                self.task_list.append(task)
            else:
                self.task_list.insert(self.selected_task_index, task)
        self.task_textbox.delete(index1="1.0", index2="end")
        self.selected_task_index = None
        self.selected_task = None
        self.edit_button.config(state="disabled")
        self.update_listbox()

    def edit_button_clicked(self):
        self.done_button.config(state="disabled")
        self.delete_button.config(state="disabled")
        self.add_button.config(state="active")

        self.task_textbox.insert("1.0", self.selected_task)
        self.selected_task_index = self.task_list.index(self.selected_task)
        self.task_list.remove(self.selected_task)
        self.selected_task = None

    def delete_button_clicked(self):
        self.task_list.remove(self.selected_task)
        self.selected_task = None
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, "end")
        for task in self.task_list:
            self.task_listbox.insert(self.task_list.index(task), task)

        self.task_listbox.bind("<<ListboxSelect>>", self.listbox_used)

    def listbox_used(self, selection):
        print(selection)
        if self.task_listbox.curselection():
            self.selected_task = self.task_listbox.get(self.task_listbox.curselection())
            self.done_button.config(state="active")
            self.edit_button.config(state="active")
            self.delete_button.config(state="active")
