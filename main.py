from customtkinter import *
import customtkinter
import pyautogui as pag
from PIL import Image
flag = ''
w,h = pag.size()
customtkinter.set_appearance_mode("Dark")
def Landing():
    global w,h
    win1 = CTk()
    old = Image.open('Assets\\Wallpaper.jpg')
    new_image = old.resize((w, h))
    new_image.save('Assets\\Wallpaper.jpg')
    background = customtkinter.CTkImage(light_image = Image.open('Assets\\Wallpaper.jpg'),
                        dark_image = Image.open('Assets\\Wallpaper.jpg'),
                        size=(w, h))
    back = CTkLabel(win1,text = ' ', image = background).pack()
    win1.attributes('-fullscreen',True)
    win1.mainloop()
Landing()