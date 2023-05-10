from customtkinter import *
import time
from PIL import Image
def Landing():
    win1 = CTk()
    old = Image.open('Assets\\Wallpaper.jpg')
    new_image = old.resize((w, h))
    new_image.save('Assets\\Wallpaper.jpg')
    background = CTkImage(light_image = Image.open('Assets\\Wallpaper.jpg'),
                        size=(w, h))   
    time.sleep(100)
Landing()