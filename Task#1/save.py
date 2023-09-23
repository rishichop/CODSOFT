import json


class ReadWrite:

    def __init__(self):
        self.tasks = {}

    def read(self):
        try:
            with open("lists.json", "r") as self.task_file:
                self.tasks = json.load(self.task_file)
        except FileNotFoundError:
            return None
        return self.tasks

    def write(self, data, type_update):
        try:
            self.read()
            if type_update == "u":
                self.tasks.update(data)
            else:
                self.tasks.pop(data)
            with open("lists.json", "w") as self.task_file:
                json.dump(self.tasks, self.task_file, indent=4)
        except FileNotFoundError:
            pass


ReadWriteVar = ReadWrite()
