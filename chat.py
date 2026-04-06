import tkinter as tk
from PIL import Image, ImageTk
import requests
from geopy.geocoders import Nominatim

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("1200x600")
root.configure(bg="lightblue")
root.resizable(False, False)

# ---------------- GEO ----------------
geolocator = Nominatim(user_agent="weather_app")

# ---------------- LOAD ICONS ----------------
sun_img = ImageTk.PhotoImage(Image.open("/home/aiat/Downloads/icon/sun.png").resize((100,100)))
cloud_img = ImageTk.PhotoImage(Image.open("/home/aiat/Downloads/icon/cloud.png").resize((100,100)))
rain_img = ImageTk.PhotoImage(Image.open("/home/aiat/Downloads/icon/rain.png").resize((100,100)))

# ---------------- FUNCTION ----------------
def get_weather_icon(code):
    # Open-Meteo weather codes
    if code == 0:
        return sun_img
    elif code in [1, 2, 3]:
        return cloud_img
    else:
        return rain_img

def fetch_weather(location_name):
    location = geolocator.geocode(location_name)

    if location:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": location.latitude,
                "longitude": location.longitude,
                "current": "temperature_2m,relative_humidity_2m,windspeed_10m,pressure_msl,visibility,weather_code",
                "daily": "weather_code,temperature_2m_max",
                "forecast_days": 7,
                "timezone": "auto"
            }
        )

        data = response.json()

        # ---------------- CURRENT ----------------
        Temperature.config(text=f"Temp: {data['current']['temperature_2m']}°C")
        Wind.config(text=f"Wind: {data['current']['windspeed_10m']} km/h")
        Humidity.config(text=f"Humidity: {data['current']['relative_humidity_2m']}%")
        Barometer.config(text=f"Pressure: {data['current']['pressure_msl']} hPa")
        Visibility.config(text=f"Visibility: {data['current']['visibility']} m")

        # ---------------- WEEK ICONS ----------------
        daily_codes = data['daily']['weather_code']

        for i in range(7):
            icon = get_weather_icon(daily_codes[i])
            boxes[i].config(image=icon)
            boxes[i].image = icon

    else:
        print("Location not found")

# ---------------- SEARCH ----------------
search_entry = tk.Entry(root, font=("Arial", 16), width=20)
search_entry.place(x=900, y=60)

search_button = tk.Button(
    root,
    text="Search",
    font=("Arial", 14),
    bg="#BAD7FF",
    command=lambda: fetch_weather(search_entry.get())
)
search_button.place(x=1100, y=55)

# ---------------- LABELS ----------------
Temperature = tk.Label(root, text="Temp", font=("Arial", 16), bg="#BAD7FF")
Temperature.place(x=580, y=90)

Wind = tk.Label(root, text="Wind", font=("Arial", 16), bg="#BAD7FF")
Wind.place(x=380, y=150)

Humidity = tk.Label(root, text="Humidity", font=("Arial", 16), bg="#BAD7FF")
Humidity.place(x=540, y=150)

Barometer = tk.Label(root, text="Pressure", font=("Arial", 16), bg="#BAD7FF")
Barometer.place(x=700, y=150)

Visibility = tk.Label(root, text="Visibility", font=("Arial", 16), bg="#BAD7FF")
Visibility.place(x=450, y=200)

# ---------------- DAYS ----------------
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

boxes = []
for i in range(7):
    tk.Label(root, text=days[i], font=("Arial", 16), bg="#BAD7FF")\
        .place(x=130 + i*110, y=270)

    box = tk.Label(root, image=cloud_img, bg="black")
    box.place(x=110 + i*110, y=320)
    box.image = cloud_img
    boxes.append(box)

# ---------------- RUN ----------------
root.mainloop()