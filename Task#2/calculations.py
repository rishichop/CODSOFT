temp_index = None


class Calculation:

    def __init__(self):
        self.combined_numbers = []
        self.bracket_open_counter = 0
        self.format_error = ""

    def break_down(self, literals_list):
        number = str()
        bracket = ["0", " + "]
        i = 0
        try:
            while i <= len(literals_list) - 1:
                if literals_list[i] in [" + ", " - ", " / ", " * ", " ( ", " ) ", " = "]:

                    if literals_list[i] == " ( ":
                        if number != "":
                            self.combined_numbers.append(number)
                            print(f"Current bracket {self.combined_numbers}")
                        print("round bracket detected!")
                        number = str()
                        temp = Calculation()
                        if literals_list[i - 1] not in [" + ", " - ", " / ", " * ", " ( ", " ) ", " = "]:
                            self.combined_numbers.append(" * ")
                            print(f"Current bracket {self.combined_numbers}")
                        self.bracket_open_counter += 1
                        j = i + 1
                        while literals_list[j] != " ) " or self.bracket_open_counter != 0:
                            if literals_list[j + 1] == " ) ":
                                self.bracket_open_counter -= 1
                            if literals_list[j] == " ( ":
                                self.bracket_open_counter += 1
                            bracket.append(literals_list[j])
                            print(bracket)
                            j += 1
                            if literals_list[j] == " = " and self.bracket_open_counter != 0:
                                break
                        bracket.append(" = ")
                        self.combined_numbers.append(temp.calculate(bracket))
                        bracket = ["0", " + "]
                        print("j", j)
                        i = j + 1
                        continue

                    if number != "":
                        self.combined_numbers.append(number)
                        print(f"Current bracket {self.combined_numbers}")
                    self.combined_numbers.append(literals_list[i])
                    print(f"Current bracket {self.combined_numbers}")
                    number = str()
                    print("i", i)
                    i += 1
                    continue

                number += literals_list[i]
                print("i", i)
                i += 1

            print(f"Current bracket {self.combined_numbers}")

        except ValueError:
            self.format_error = "Error: Format wrong"
        except IndexError:
            self.format_error = "Error: Format wrong"

    def calculate(self, literal_list):
        global temp_index
        self.combined_numbers.clear()
        self.break_down(literal_list)
        result = 0
        while True:
            if " / " in self.combined_numbers:
                try:
                    temp_index = self.combined_numbers.index(" / ")
                    result = int(self.combined_numbers[temp_index - 1])
                    result = int(result / int(self.combined_numbers[temp_index + 1]))
                except ValueError:
                    result = round(result / int(self.combined_numbers[temp_index + 2]) * -1)
                    self.combined_numbers.pop(temp_index + 2)
                finally:
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.insert(temp_index - 1, str(result))
                    result = 0

            elif " * " in self.combined_numbers:
                try:
                    temp_index = self.combined_numbers.index(" * ")
                    result = int(self.combined_numbers[temp_index - 1])
                    result = result * int(self.combined_numbers[temp_index + 1])
                except ValueError:
                    result = result * int(self.combined_numbers[temp_index + 2]) * -1
                    self.combined_numbers.pop(temp_index + 2)
                finally:
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.insert(temp_index - 1, str(result))
                    result = 0

            elif " + " in self.combined_numbers:
                try:
                    temp_index = self.combined_numbers.index(" + ")
                    result = int(self.combined_numbers[temp_index - 1])
                    result = result + int(self.combined_numbers[temp_index + 1])
                except ValueError:
                    result = result + int(self.combined_numbers[temp_index + 2]) * -1
                    self.combined_numbers.pop(temp_index + 2)
                finally:
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.pop(temp_index - 1)
                    self.combined_numbers.insert(temp_index - 1, str(result))
                    result = 0

            elif " - " in self.combined_numbers:
                temp_index = self.combined_numbers.index(" - ")
                result = int(self.combined_numbers[temp_index - 1])
                result = result - int(self.combined_numbers[temp_index + 1])
                self.combined_numbers.pop(temp_index - 1)
                self.combined_numbers.pop(temp_index - 1)
                self.combined_numbers.pop(temp_index - 1)
                self.combined_numbers.insert(temp_index - 1, str(result))
                result = 0

            elif " = " in self.combined_numbers:
                print(self.combined_numbers)
                return self.combined_numbers[0]

            print(self.combined_numbers)
