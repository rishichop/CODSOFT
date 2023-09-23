import tkinter as tk
from calculations import Calculation

calculation = Calculation()

WIDTH = 525
HEIGHT = 600

BUTTON_WIDTH = 15
BUTTON_HEIGHT = 4
CALCULATE_LIST = []


def get_result():
    CALCULATE_LIST.insert(0, "0")
    CALCULATE_LIST.insert(1, " + ")
    if len(CALCULATE_LIST) == 3:
        CALCULATE_LIST.clear()
        return
    result = calculation.calculate(CALCULATE_LIST)
    CALCULATE_LIST.clear()
    result_canvas.itemconfig(result_text, text=result)
    if "Error" not in result:
        CALCULATE_LIST.append(result)
    calculation.format_error = ""


def button_clicked(value):
    if value == "clear":
        CALCULATE_LIST.clear()
        calculation.format_error = ""

    elif value == "del":
        try:
            CALCULATE_LIST.pop(len(CALCULATE_LIST) - 1)
        except IndexError:
            pass

    elif value == "exit":
        main_window.destroy()
        return

    result_canvas.itemconfig(result_text, text="")

    if value not in ["clear", "del"]:
        CALCULATE_LIST.append(value)

    display_text = ""

    if value == " = ":
        get_result()
        return

    for i in CALCULATE_LIST:
        display_text += i
    result_canvas.itemconfig(result_text, text=display_text)


main_window = tk.Tk()
main_window.title("Calculator")
main_window.minsize(width=WIDTH, height=HEIGHT)
main_window.maxsize(width=WIDTH, height=HEIGHT)

result_canvas = tk.Canvas(master=main_window, background="black", width=WIDTH, height=150)
result_canvas.pack(fill="both")

button_frame = tk.Frame(master=main_window, padx=20, pady=20)
button_frame.pack(fill="both")

result_text = result_canvas.create_text((50, 50),
                                        text="",
                                        anchor="w",
                                        width=WIDTH - 100,
                                        font=("Arial", 20),
                                        fill="white")

BUTTON = [["7", "8", "9", " + "],
          ["4", "5", "6", " - "],
          ["1", "2", "3", " * "],
          ["0", "del", "clear", " / "],
          [" ( ", " ) ", "exit", " = "]]

for row in range(0, 5):
    for column in range(0, 4):
        number_button = tk.Button(master=button_frame,
                                  text=f"{BUTTON[row][column]}",
                                  width=BUTTON_WIDTH,
                                  height=BUTTON_HEIGHT,
                                  command=lambda value=BUTTON[row][column]: button_clicked(value),
                                  font=("Arial", 9, "bold"))

        number_button.grid(row=row, column=column, padx=(5, 0), pady=(10, 0), sticky="w")

main_window.mainloop()
