import tkinter as tk
import ttkbootstrap as ttk

from api import API
from PIL import ImageTk, Image
from io import BytesIO

api = API()
FONT = ("Arial", 20)

prev_icon = None


def update_canvas(weather_info):
    global prev_icon

    response_icon = weather_info["icon"]
    print(response_icon)
    if response_icon.status_code == 200:
        image = Image.open(BytesIO(response_icon.content))
        new_icon = ImageTk.PhotoImage(image)
        icon_canvas.itemconfig(icon, image=new_icon)
        prev_icon = new_icon


def display_info():
    api.get_coords()
    weather_info = api.get_weather_info()
    name_result_label.config(text=weather_info["name"])
    lat_result_label.config(text=str(weather_info["lat"]) + " °")
    lon_result_label.config(text=str(weather_info["lon"]) + " °")
    temp_result_label.config(text=str(weather_info["temperature"]) + " °C")
    press_result_label.config(text=str(weather_info["pressure"]) + " hPa")
    humi_result_label.config(text=str(weather_info["humidity"]) + " %")
    dew_result_label.config(text=str(weather_info["dew point"]) + " °C")
    clouds_result_label.config(text=str(weather_info["clouds"]) + " %")
    wind_result_label.config(text=str(weather_info["wind speed"]) + " m/s")
    des_result_label.config(text=str(weather_info["description"]))

    update_canvas(weather_info)


def search_button_clicked():
    api.set_api_input(input_entry.get().title())
    input_entry.delete(0, "end")
    display_info()


def radio_button_used():
    if radio_state.get() == 1:
        api.set_search_params("name")
    else:
        api.set_search_params("zip")


main_window = ttk.Window(themename="morph")
main_window.title("Weather")
main_window.geometry()
main_window.config(padx=25, pady=25)

style = ttk.Style("morph")

info_frame = ttk.Frame(master=main_window)
info_frame.grid(column=0, row=0, sticky="WE")

name_label = ttk.Label(master=info_frame, text="Location:", font=FONT)
name_label.grid(column=0, row=0, sticky="W")

lat_label = ttk.Label(master=info_frame, text="Latitude:", font=FONT)
lat_label.grid(column=0, row=1, sticky="W")

lon_label = ttk.Label(master=info_frame, text="Longitude:", font=FONT)
lon_label.grid(column=0, row=2, sticky="W")

temp_label = ttk.Label(master=info_frame, text="Temperature:", font=FONT)
temp_label.grid(column=0, row=3, sticky="W")

press_label = ttk.Label(master=info_frame, text="Pressure:", font=FONT)
press_label.grid(column=0, row=4, sticky="W")

humi_label = ttk.Label(master=info_frame, text="Humidity:", font=FONT)
humi_label.grid(column=0, row=5, sticky="W")

dew_label = ttk.Label(master=info_frame, text="Dew Point:", font=FONT)
dew_label.grid(column=0, row=6, sticky="W")

clouds_label = ttk.Label(master=info_frame, text="Clouds:", font=FONT)
clouds_label.grid(column=0, row=7, sticky="W")

wind_label = ttk.Label(master=info_frame, text="Wind Speed:", font=FONT)
wind_label.grid(column=0, row=8, sticky="W")

des_label = ttk.Label(master=info_frame, text="Description:", font=FONT)
des_label.grid(column=0, row=9, sticky="W")

name_result_label = ttk.Label(master=info_frame, text="", font=FONT)
name_result_label.grid(column=1, row=0, sticky="W", padx=(50, 0))

lat_result_label = ttk.Label(master=info_frame, text="", font=FONT)
lat_result_label.grid(column=1, row=1, sticky="W", padx=(50, 0))

lon_result_label = ttk.Label(master=info_frame, text="", font=FONT)
lon_result_label.grid(column=1, row=2, sticky="W", padx=(50, 0))

temp_result_label = ttk.Label(master=info_frame, text="", font=FONT)
temp_result_label.grid(column=1, row=3, sticky="W", padx=(50, 0))

press_result_label = ttk.Label(master=info_frame, text="", font=FONT)
press_result_label.grid(column=1, row=4, sticky="W", padx=(50, 0))

humi_result_label = ttk.Label(master=info_frame, text="", font=FONT)
humi_result_label.grid(column=1, row=5, sticky="W", padx=(50, 0))

dew_result_label = ttk.Label(master=info_frame, text="", font=FONT)
dew_result_label.grid(column=1, row=6, sticky="W", padx=(50, 0))

clouds_result_label = ttk.Label(master=info_frame, text="", font=FONT)
clouds_result_label.grid(column=1, row=7, sticky="W", padx=(50, 0))

wind_result_label = ttk.Label(master=info_frame, text="", font=FONT)
wind_result_label.grid(column=1, row=8, sticky="W", padx=(50, 0))

des_result_label = ttk.Label(master=info_frame, text="", font=FONT)
des_result_label.grid(column=1, row=9, sticky="W", padx=(50, 0))

label = ttk.Label(master=main_window,
                  text="Please Enter the Name or Zip code of the location: ",
                  font=("Arial", 16))
label.grid(column=0, row=1, pady=(50, 0))

input_entry = ttk.Entry(master=main_window, font=("Arial", 16))
input_entry.focus()
input_entry.grid(column=0, row=2, sticky="WE")

radio_state = tk.IntVar(value=1)

name_radio = tk.Radiobutton(master=main_window, text="Search with Name of the location", variable=radio_state,
                            command=radio_button_used,
                            value=1,
                            font=("Arial", 16))
name_radio.grid(column=0, row=3, sticky="W")

zip_radio = tk.Radiobutton(master=main_window,
                           text="Search with Zip code (with ISO 3166 country codes) of the location",
                           variable=radio_state,
                           command=radio_button_used,
                           value=2,
                           font=("Arial", 16))
zip_radio.grid(column=0, row=4, sticky="W")

# noinspection PyArgumentList
search_button = ttk.Button(master=main_window, text="Search", command=search_button_clicked, width=10,
                           bootstyle="INFO, OUTLINE")
search_button.grid(column=0, row=5, pady=(5, 0))

icon_canvas = ttk.Canvas(master=info_frame, width=100, height=100)
icon_canvas.grid(column=2, row=9)

placeholder = ttk.PhotoImage()
icon = icon_canvas.create_image(0, 0, anchor="nw", image=placeholder)

main_window.mainloop()
