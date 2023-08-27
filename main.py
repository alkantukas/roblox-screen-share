from PIL import Image
import pyautogui
import requests
import time


while True:
    time.sleep(0.1)

    pyautogui.screenshot('screenshot.png')

    img = Image.open('screenshot.png')

    everything = []

    for row in range(0, 192):
        line = []
        for pixel in range(0, 108):
            line.append(img.getpixel((row*10, pixel*10)))

        if not line:
            pass
        else:
            everything.append(line)


    data_to_send = {
        "mode": everything
    }

    # Send a POST request to the API to update data
    response = requests.post(f"{'https://sharescreen.alkantukas.repl.co'}/", json=data_to_send)
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print("Failed to send data")
