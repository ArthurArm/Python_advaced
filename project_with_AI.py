import tkinter as tk
import json
import urllib.request
import requests
from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)

    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image


def get_image_url():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzFkMmY2NjQtOWM4Mi00NDc1LThlNWYtNThkMTg2NmY0MzBjIiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.CNx_oOAe5wnoFfUFac4vLIRrF7RAii2_l3CZxR8vyz4"}
    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": entry.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['items'][0]["image_resource_url"]


def render_image():
    print("clicked")
    try:
        error_label.place_forget()
        image_url = get_image_url()
        display_image(image_url)
    except KeyError:
        error_label.place(x=200, y=150)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("AI image generator")
window.geometry("900x550")

error_label = tk.Label(window, text="CHUTIA", fg="green")

entry = tk.Entry(window, width=45)
entry.place(x=230, y=50)

image_label = tk.Label(window)
image_label.place(x=125, y=80)

generate_button = tk.Button(window, text="Press me KURVA !", height=1, command=render_image)
generate_button.place(x=650, y=48)


window.mainloop()
