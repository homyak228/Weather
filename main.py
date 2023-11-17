import tkinter
import customtkinter
import requests

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("400x380")
app.title("Погода")
app.resizable(width=False, height=False)


def weather():
    enter = city.get()

    key = "00ea11a21e7516d43cfa39451a4a9eb7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={enter}&appid={key}"
    params = {'APPID': key, 'q': url, 'units': 'imperial'}
    result = requests.get(url, params=params)
    weather = result.json()
    message = "Введите название\n              города"

    if weather['cod'] == '404' and weather['message'] == 'city not found':
        city_title.configure(text="Город не найден")
    elif enter == "":
        city_title.configure(text=f"{message:}")
    else:
        city_title.configure(text=f"{str(weather['name'])}: {str(round(((int((weather['main']['temp'])) - 32) / 1.8)))}C°, {str(weather['main']['humidity'])}%")

M_frame = customtkinter.CTkFrame(master=app)
M_frame.pack(pady=40, padx=40, fill="both", expand=True)

title = customtkinter.CTkLabel(master=M_frame, justify=tkinter.LEFT, text="Погодная информация", font=('Impact', 26))
title.pack(pady=12, padx=10)

city = customtkinter.CTkEntry(master=M_frame, justify=tkinter.LEFT, placeholder_text="Введите город", font=('Impact', 18))
city.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=M_frame, text="Узнать погоду", font=('Impact', 16), command=weather)
button.pack(pady=12, padx=10)

city_title = customtkinter.CTkLabel(master=M_frame, justify=tkinter.LEFT, text="Инфо", font=('Impact', 30))
city_title.pack(pady=12, padx=10)

app.mainloop()